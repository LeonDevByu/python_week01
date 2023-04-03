import csv

COMPANY_NAME_INDEX = 0
NUM_EMPS_INDEX = 1
NUM_PATIENTS_INDEX = 2


def main():
    with open("listname.csv", "rt") as listname_file:
        reader = csv.reader(listname_file)
        next(reader)
        running_max = 0
        most_office = None
        for row_list in reader:
            company = row_list[COMPANY_NAME_INDEX]
            num_employees = row_list[NUM_EMPS_INDEX]
            num_patients = row_list[NUM_PATIENTS_INDEX]

            # patients_per_emp = num_patients / num_employees
            #
            # if patients_per_emp > running_max:
            #     running_max = patients_per_emp
            #     most_office = company

    # print(f"{most_office} has {running_max:.1f}"
    #       " patients per employee")
            print(f"{num_employees}")

if __name__ == "__main__":
    main()
