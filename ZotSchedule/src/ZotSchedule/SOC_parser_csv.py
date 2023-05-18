from sys import argv
from bs4 import BeautifulSoup
import csv, requests

SOC_columns = {'id', 'name', 'department', 'number'}

POST_data = {'Submit': 'Display Text Results', 'YearTerm': '2023-92', 'Dept': 'COMPSCI', 'Division': 'ANY'}

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


if __name__ == "__main__":
      argv[1] = (r'C:\Users\leejo\Personal\Coding Projects\ZotSchedule\ZotSchedule\src\src_data\new_subjects_database.csv')
      if validate_args():
        csv_fn = argv[1]
                

        with open(csv_fn, 'r+') as csv_file:
            print("Existing records: ")
            csv_reader = csv.DictReader(csv_file, fieldnames=SOC_columns)
            for row in csv_reader:
                print(row)

        with open(csv_fn, 'a+') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=SOC_columns)
            csv_writer.writeheader()
            csv_writer.writerows()
            
    


