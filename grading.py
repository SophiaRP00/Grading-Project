import numpy as np
import matplotlib.pyplot as plt

def roundGrade(grades):
    grades = np.round(grades)

    return grades

def computeFinalGrades(grades):
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
    print("hey")
    grades = np.array([1.2, 3.4, 5.6, 7.8, 9.0, 11.2, 13.4])
    gradesPlot(grades)
main()
