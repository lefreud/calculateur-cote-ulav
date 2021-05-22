import pandas as pd

GRADE_MAPPING = {
    "A+": 4.33,
    "A": 4.00,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.00,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.00,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.00,
    "E": 0.00
}

grades = pd.read_csv("grades.csv")
filtered_grades = grades.loc[grades["grade"] != "P"].copy()
filtered_grades["score"] = filtered_grades["grade"].map(GRADE_MAPPING)
print(filtered_grades)

cumulative_score = round(
    (filtered_grades["score"] * filtered_grades["credits"]).sum() / filtered_grades["credits"].sum(), 2
)
print("Your cumulative score for all semesters:", cumulative_score)
