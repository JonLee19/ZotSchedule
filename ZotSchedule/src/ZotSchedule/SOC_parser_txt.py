from sys import argv
from bs4 import BeautifulSoup
import csv, requests, os
import sqlite3

#use pandas!

SOC_columns = {'id', 'name', 'department', 'number'}

courses_list = []

POST_data = {'Submit': 'Display Text Results', 'YearTerm': '2023-92', 'Dept': 'COMPSCI', 'Division': 'ANY'}

def get_cursor():
    return conn.cursor()

def commit_cursor(cur):
    cur.execute('commit')

def print_all_subjects():
    conn = sqlite3.connect(r"..\db.sqlite3")
    # conn = sqlite3.connect(r"C:\Users\leejo\Personal\Coding Projects\ZotSchedule\ZotSchedule\src\db.sqlite3")
    cur = conn.cursor()
    res = cur.execute("SELECT * FROM schedule_builder_subject")
    for row in res:
        print(row)
    cur.close()
    conn.close()

def insert_subject(cur, **kwargs):
    task = (kwargs['name'], kwargs['department'], kwargs['number'])
    cur.execute(f"INSERT INTO schedule_builder_subject(name, department, number) \
                    VALUES (?, ?, ?)",
                    task)
        

def validate_args():
    if len(argv) <= 1:
        print("InputError: No SOC file (csv) specified.")
        return False
    elif len(argv) > 2:
        print("InputError: Too many arguments specified, please only list the SOC file.")
        return False
    else:
        csv_fn = argv[1]
        try:
            with open(csv_fn) as csv_file:
                pass
        except Exception as e:
            print(e)
            print(f"Error: File {csv_fn} could not be opened!")
            return False
    return True

def main():
    if validate_args():
        txt_fn = argv[1]
            
    with open(txt_fn, 'r+') as txt_file:
        soup = BeautifulSoup(txt_file, 'html.parser')
        course_list_table = soup.find('div', class_='course-list').find('table')
        if course_list_table:
            course_data_list = course_list_table.find_all("td", class_="CourseTitle")
            for course_data in course_data_list:
                course_txt = course_data.text.strip().rstrip('(Prerequisites)').strip()
                course_components = course_txt.split(maxsplit=2)
                courses_list.append({'department': course_components[0], 'number': course_components[1], 'name': course_components[2]})
        
        conn = conn = sqlite3.connect(r"..\db.sqlite3")
        cur = conn.cursor()
        for course in courses_list:
            insert_subject(cur, **course)
        commit_cursor(cur)
        conn.close()

    print_all_subjects()

    # cur = get_cursor()
    # insert_subject(cur, name="test django again", department="default", number="defaultnum")
    # commit_cursor(cur)
    # print_all_subjects()
    
if __name__ == "__main__":
    #for ease of debugging
    argv[1] = (r'C:\Users\leejo\Personal\Coding Projects\ZotSchedule\ZotSchedule\src\src_data\WebSoc-request-html.txt')
    main()

