  """
    1.Create a dictionary of student names and their corresponding scores.
""" 
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
"""
    2.Write a program to add a new student and their score to the dictionary."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
print(students)
"""
    3.Implement a function to remove a student from the dictionary."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
del students['Medine']
print(students)
"""
    4.Create a program to update the score of a specific student in the dictionary."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
del students['Medine']
students["Lale"] = 85
print(students)
"""
    5.Write a function to calculate the average score of all students in the dictionary."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
del students['Medine']
students["Lale"] = 85
all_score_students = students["Leyla"] + students["Lale"] + students["Aysel"]
length = len(students)
average_students = all_score_students/length
print(average_students)

"""
    6.Implement a program to find the student with the highest score in the dictionary."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
del students['Medine']
students["Lale"] = 85
max_score = max(students.values())
print(f"Highest score is: >> {max_score}" )

"""  
    7.Create a function to find the student with the lowest score in the dictionary. """
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
del students['Medine']
students["Lale"] = 85
min_score = min(students.values())
print(f"Lowest score is: >> {min_score}" )

"""
    8.Write a program to check if a given student is present in the dictionary. """
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
students["Aysel"] = 80 
del students['Medine']
students["Lale"] = 85
if "Leyla" in students:
    print(f"Leyla is on the list of students.")
"""
    9.Implement a function to print all students who scored above a certain threshold."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}
x = 60
scored_above = {k:v for (k,v) in students.items() if v > x}
print(scored_above)
    """  
    10.Create a program to print the names of students who scored below a certain threshold."""
students = {
    "Leyla": 58,
    "Lale": 65,
    "Medine": 75
}  
y = 80
scored_below = {k:v for (k,v) in students.items() if v < y}
print(scored_below)
    """"""
