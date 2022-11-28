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

def roundGrade(grades):
    legalGrades = [-3, 0, 2, 4, 7, 10, 12]
    return legalGrades[np.argmin(np.abs(np.array(legalGrades) - grades))]


    return grades

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
    return 0
def gradesPlot(grades):
    FinalGrades = computeFinalGrades(grades)
    xgrades = np.array([1,3,5,7,9,11,13])
    ygrades = np.array([len(FinalGrades[FinalGrades == -3]),len(FinalGrades[FinalGrades == 0]),len(FinalGrades[FinalGrades == 2]),len(FinalGrades[FinalGrades == 4]),len(FinalGrades[FinalGrades == 7]),len(FinalGrades[FinalGrades == 10]),len(FinalGrades[FinalGrades == 12])])
    plt.xticks(xgrades, ('-3', '0', '2', '4', '7', '10', '12'))
    plt.bar(xgrades,ygrades)
    plt.xlabel('grades')
    plt.ylabel('Final Grades')
    plt.title('Final Grades')
    plt.show()


def main():
    print(roundGrade(6.3))
    grades = np.array([1.2, 3.4, 5.6, 7.8, 9.0, 11.2, 13.4])
    gradesPlot(grades)

    while True:
        print("Welcome to the Grading Program \n")
        print( "MENU \n")
        print("Please choose one of the following options: \n")
        print("1. Load New Data \n")
        print("2. Check for Data Erros \n")
        print("3. Generate Plots \n")
        print("4. Display list of grades \n")
        print("5. Quit \n")

        choice = input("Your choice: ")

        if choice == "1":
            print("Load New Data \n")
            filename = input("Please enter the name of the file: ")
            dataLoad(filename)
            print("Data loaded (◕ᴥ◕ʋ)\n")
        
        elif choice == "2":
            print 
        elif choice == "3":
            print 
        elif choice == "4":
            print 
        elif choice == "5":
            if input("Are you certain you want to quit now? [y/n]\n") == "y":
                print(credits)
                break 
            else:
                print("Returning to main menu \n")
            
main()
