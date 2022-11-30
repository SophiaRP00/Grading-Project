import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dataLoad(filename):
    grades = pd.read_csv(filename)
    return grades.to_numpy()[:,2:]

def roundGrade(grades):
    legalGrades = [-3, 0, 2, 4, 7, 10, 12]
    return legalGrades[np.argmin(np.abs(np.array(legalGrades) - grades))]

def computeFinalGrades(grades):
    finalGrades = np.zeros(grades.shape[0])
    for i, studentGrades in enumerate(grades):
        if studentGrades.size == 1:
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
    
    




def main():
    grades = dataLoad('grade.csv')
    gradesPlot(grades)
main()
