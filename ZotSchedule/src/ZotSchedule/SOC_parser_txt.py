from sys import argv
from bs4 import BeautifulSoup
from django import setup
from django.conf import settings
from django.db import connections
import csv, requests, os
import sqlite3

# db_info = {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
SOC_columns = {'id', 'name', 'department', 'number'}

courses_list = []

POST_data = {'Submit': 'Display Text Results', 'YearTerm': '2023-92', 'Dept': 'COMPSCI', 'Division': 'ANY'}

def get_cursor():
    conn = sqlite3.connect(r"..\db.sqlite3")
    return conn.cursor()

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
                courses_list = {'department': course_components[0], 'number': course_components[1], 'name': course_components[2]}
                print(courses_list)

    # setup()
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZotSchedule.settings')

    # settings.configure(DATABASE={'default':db_info})
    #insert into database
    # conn = connections.create_connection('default')
    # cur = conn.cursor()

    print_all_subjects()
    # conn = sqlite3.connect(r"..\db.sqlite3")
    # # conn = sqlite3.connect(r"C:\Users\leejo\Personal\Coding Projects\ZotSchedule\ZotSchedule\src\db.sqlite3")
    # cur = conn.cursor()
    # res = cur.execute("SELECT * FROM schedule_builder_subject")
    # for row in res:
    #     print(row)
    cur = get_cursor()
    insert_subject(cur, name="test django again", department="default", number="defaultnum")
    # task = ['default django insert', 'default', 'defaultnum']
    # cur.execute("INSERT INTO schedule_builder_subject(name, department, number) \
    #             VALUES ('default django 1', 'default', 'defaultnum')")
    
    # res = cur.execute("SELECT * FROM schedule_builder_subject")
    # for row in res:
    #     print(row)

    # conn.commit()
    cur.execute("commit")
    print_all_subjects()
    
    # task = ['default django insert', 'default', 'defaultnum']
    # cur.execute('''INSERT INTO schedule_builder_subject(name, department, number)
    #             VALUES (?, ?, ?)''',
    #                     task)

    # print([i for i in course_list.children])
        # print("Existing records: ")
        # # csv_reader = csv.DictReader(csv_file, fieldnames=SOC_columns)
        # for row in txt_file:
        #     print(row)

    # with open(csv_fn, 'a+') as csv_file:
    #     csv_writer = csv.DictWriter(csv_file, fieldnames=SOC_columns)
    #     csv_writer.writeheader()
    #     csv_writer.writerows()
            
    

if __name__ == "__main__":
    #for ease of debugging
    argv[1] = (r'C:\Users\leejo\Personal\Coding Projects\ZotSchedule\ZotSchedule\src\src_data\WebSoc-request-html.txt')

    main()

