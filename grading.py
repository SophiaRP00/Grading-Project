import numpy as np

def roundGrade(grades):
    legalGrades = [-3, 0, 2, 4, 7, 10, 12]
    return legalGrades[np.argmin(np.abs(np.array(legalGrades) - grades))]

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
    return 0

def main():
    print(roundGrade(6.3))
main()