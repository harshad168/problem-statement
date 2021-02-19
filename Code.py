
# ! /usr/bin/python

import time, os, json
from threading import Timer

employee_details = []

def writedata_delay():
    with open('original_employee_data.json', 'w') as o:
        o.write(json.dumps(employee_details))
    with open('sorted_employee_data.json', 'w+') as s:
        s.write(json.dumps(sort_employee))
    with open('sorted_employee_expage_data.json', 'w+') as ex:
        ex.write(json.dumps(sort_employee2))


while (True):
    print "Press 1 to enter employee details."
    print "Press 2 to SORT employee details."
    print "Press 3 to exit."
    try:
        inp = input("Please enter 1 option in above 3 options -")
        if int(inp) == 1:
            # below code will take employee details input
            temp_employee = {}
            temp_employee["FirstName"] = raw_input("Please input FirstName - ")
            temp_employee["LastName"] = raw_input("Please input LastName - ")
            temp_employee["Organisation"] = raw_input("Please input your organisation - ")
            while (True):
                try:
                    temp_employee["Experience"] = int(raw_input("Please input experience in months - "))
                    while (True):
                        try:
                            temp_employee["Age"] = int(raw_input("Please input your age in years - "))
                            break
                        except:
                            print "invalid age, please provide age in years - "
                            pass
                    break
                except:
                    print "invalid experience, please provide experience in months."
                    pass
            employee_details.append(temp_employee)
            print "\n"
        elif int(inp) == 2:
            # below code will sort employee details as per requirement
            try:
                os.mkdir("Problem Statement")
            except:
                pass
            os.chdir("Problem Statement")
            tem = "Employee Details_"+str(int(time.time()))
            os.mkdir(str(tem))
            os.chdir(str(tem))
            sort_employee = []
            sort_employee2=[]
            sort_employee_orgname = []
            sort_expage_ratio = []
            for x in range(len(employee_details)):
                sort_employee_orgname.append(employee_details[x]["Organisation"])
                sort_expage_ratio.append(employee_details[x]["Experience"]/employee_details[x]["Age"])
            sort_employee_orgname = sorted(sort_employee_orgname)
            sort_expage_ratio = sorted(sort_expage_ratio)
            for x in sort_employee_orgname:
                for y in employee_details:
                    if y["Organisation"] == x:
                        sort_employee.append(y)
            print "\n"
            for x in sort_expage_ratio:
                for y in employee_details:
                    if (y["Experience"]/y["Age"]) == x:
                        sort_employee2.append(y)
            print "\n"
            thr = Timer(5.0,writedata_delay)
            thr.start()
        elif int(inp) == 3:
            # below code will exit application
            break
        else:
            print "Invalid input. Please provide a valid input either 1,2 or 3."
            print "\n"
    except:
        print "\n"
        pass

