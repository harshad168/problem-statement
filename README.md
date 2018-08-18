# problem-statement
Code for problem statement as per below requirement.

Problem Statement 1:
Input to be read from command line. Input is split into multiple lines. Each line of input can
be any of below types
1. Employee data in the string format as below : FirstName (String), LastName(String),
Experience(Months), Age(Years), Organization(String)
2. “SORT” keyword
3. “EXIT” keyword
Employee data needs to be captured for as many as records user wants to input (input type 1
above). Once “SORT” keyword (input type 2 above) is encountered, employee data needs to
be sorted and stored in three different files according to following conditions
● Organization, Experience, FirstName, LastName
● Experience/age ratio, Organization
● Append all the fields of each record.
When writing to a file, simulate a delay of 5 seconds for network latency. User should never
be blocked from entering inputs.
Program execution should be stopped when “EXIT” keyword is received.
There may be some illegal data which should be handled. List down the possible corner cases,
and try to handle them. Try to use best practices wherever is possible.
Eg Input:
Naveen, Chandra, 50, 25, Fission
Virat, Kohli, 74, 55, HCL
Ravi, Ashwin, 77, 35, Cricket
Naveen, Ramesh, 27, 25, Fission
Virat, Kohli, 14, 22, HCL
SORT
Naveen, Bindra, 37, 44, Fission
Ashok, Verma, 17, 17, Fission
Naveen, Chandra, 14, 19, Fission


Steps to run the code:
prerequisite - 
1. python 2.7 installed
2. python added to path

open a command prompt where code.py file is located and run the below command.
#python code.py
