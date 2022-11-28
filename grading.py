import numpy as np
import pandas as pd

def dataLoad(filename):
    filename = pd.read_csv('grade.csv')
    return filename.to_numpy()[:,2:]

def roundGrade(grades):
    return 0

def computeFinalGrades(grades):
    return 0
def gradesPlot(grades):
    return 0

def main():
    print("hey")
main()