#!/usr/bin/env python3
"""
Docstring for math.plotting.4-frequency
"""
import numpy as np
import matplotlib.pyplot as plt

def frequency():
    """
    Docstring for frequency
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))
    plt.hist(student_grades, bins=6, edgecolor='black')
    plt.xticks(range(0, 101, 10))
    plt.yticks(range(0, 31, 5))
    plt.xlim(0, 100)
    plt.xlabel("Grades")
    plt.ylabel("Number of Students")
    plt.title("Project A")
