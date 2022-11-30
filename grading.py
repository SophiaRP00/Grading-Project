import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

credits = "Created by Adam(s224202), Gunnar(s183737) and Sophia(s224222)"

#######################################################
### Function for loading data from a csv file       ###
### By using Pandas library                         ###
### Returning grades for each person into an array  ###
#######################################################

def dataLoad(filename):
    filename = pd.read_csv('grade.csv')
    return filename.to_numpy()[:,2:]

# Adam
def roundGrade(grades):
    legalGrades = [-3, 0, 2, 4, 7, 10, 12]
    return legalGrades[np.argmin(np.abs(np.array(legalGrades) - grades))]

#Adam
def computeFinalGrades(grades):
    finalGrades = np.zeros(grades.shape[0])
    for i, studentGrades in enumerate(grades):
        if studentGrades.size() == 1:
            finalGrades[i] = studentGrades[0]
        elif -3 in studentGrades:
            finalGrades[i] = -3
        else:
            studentGrades = np.sort(studentGrades)
            finalGrades[i] = roundGrade(np.mean(studentGrades[1:]))
    return finalGrades
def gradesPlot(grades):
    FinalGrades = computeFinalGrades(grades)
    xgrades = np.array([1,3,5,7,9,11,13])
    ygrades = np.array([len(FinalGrades[FinalGrades == -3]),len(FinalGrades[FinalGrades == 0]),len(FinalGrades[FinalGrades == 2]),len(FinalGrades[FinalGrades == 4]),len(FinalGrades[FinalGrades == 7]),len(FinalGrades[FinalGrades == 10]),len(FinalGrades[FinalGrades == 12])])
    plt.xticks(xgrades, ('-3', '0', '2', '4', '7', '10', '12'))
    plt.bar(xgrades,ygrades)
    plt.xlabel('grades')
    plt.ylabel('Occurences')
    plt.title('Final Grades')
    plt.show()

    GradesperAssignment = np.zeros((grades.shape[1],grades.shape[0]))
    for i, studentGrades in enumerate(grades):
        for j, assignmentGrades in enumerate(studentGrades):
            GradesperAssignment[j,i] = assignmentGrades
    x = []
    y=[]
    Assignmentmeans=[]
    Assignments=[]
    for i, assignment in enumerate(GradesperAssignment):
        Assignmentmeans.append(np.mean(assignment))
        Assignments.append(i+1)
        for grade in assignment:
            x.append(1+i+np.random.uniform(-0.1,0.1))
            y.append(grade+np.random.uniform(-0.1,0.1))
    plt.scatter(x,y)
    plt.plot(Assignments,Assignmentmeans,color='turquoise')
    plt.xlabel('Assignments')
    plt.ylabel('Grades')
    plt.title('Grades per Assignment')
    plt.show()
    
    



##############################################
### There is no requirement                ###
### that errors are removed from the data, ###
### so we only decided to detect them      ###
##############################################

def detectErrors(data):
    studentids = data[:,0]
    foundStudentids = []

#####################################################
### Checking if student id appears multiple times ###
### Printing message to user                      ###
#####################################################

    for studentid in studentids:
        if not studentid in foundStudentids:
            foundStudentids.append(studentid)
        else:
            print(f"Duplicate student id: {studentid}")

###############################################
### Checking if grades are legal            ###
### according to the 7 point grading scale  ###
### If not printing message to user         ###
###############################################

    legalGrades = [-3, 0, 2, 4, 7, 10, 12]
    for studentGrades in data[:,2:]:
        for grade in studentGrades:
            if not grade in legalGrades:
                print(f"Illegal grade: {grade}")

#Adam
def displayGrades(fulldata):
    sortedGrades = fulldata[fulldata[:,1].argsort()]
    for student in sortedGrades:
        print(f"{student[1]}, Grades: {student[2:]}, Final grade: {np.mean(student[2:]) if -3 not in student[2:] else -3}")

#Sophia and Gunnar
def main():
    while True:
        print("Welcome to the Grading Program \n")
        print(credits)
        print( "MENU \n")
        print("Please choose one of the following options: \n")
        print("1. Load New Data \n")
        print("2. Check for Data Errors \n")
        print("3. Generate Plots \n")
        print("4. Display list of grades \n")
        print("5. Quit \n")

        choice = input("Your choice: ")
        loaded = False
######################################
### If user enters value 1         ###
### Loading data from csv file     ###
### And checking if valid filename ###
### By using try and except        ###
### Prints error message if wrong  ###
######################################
        if choice == "1":
            print("Load New Data \n")
            filename = input("Please enter the name of the file: ")
            try:
                fulldata = dataLoad(filename)
                grades = fulldata[:,2:]
                loaded = True
                print("Data loaded succesfully (◕ᴥ◕ʋ)\n")
                print("Number of students: ", len(grades))
                print("Number of assignments: ", len(grades[0]))
            except:
                print("Error: File not found (◕︵◕✿)\n")
                print("Please try again \n")
        
        elif choice == "2" and loaded:
            detectErrors(fulldata)
        elif choice == "3" and loaded:
            gradesPlot(grades)
        elif choice == "4" and loaded:
            displayGrades(fulldata)
        elif choice == "5":
            if input("Are you certain you want to quit now? [y/n]\n") == "y":
                print(credits)
                break 
            else:
                print("Returning to main menu \n")
            
main()
