# HR Employee Attrition Analysis

## Project Overview
Analysis of the IBM HR Employee Attrition dataset to identify key drivers of employee turnover 
and provide actionable retention recommendations using Python, Pandas, and Matplotlib.

## Business Questions Answered
- Which department has the highest attrition rate?
- Does age affect employee attrition?
- What is the gender distribution of employees?
- How are monthly incomes distributed across the workforce?

## Tools Used
- Python
- Pandas
- Matplotlib

## Data Cleaning Highlights
- Removed 3 useless columns with single unique values (EmployeeCount, Over18, StandardHours)
- Validated all 35 columns for missing values, duplicates, and data type issues
- Dataset confirmed clean with zero missing values after inspection

## Key Findings
- Research & Development department has the highest attrition, with 133 employees leaving
- Younger employees aged 20-35 are significantly more likely to leave
- Male employees represent 63% of attrition cases
- Most employees earn between 2,300 and 5,000 monthly

## Recommendation
The company should focus retention strategies on younger employees through better career 
growth opportunities, mentorship programs, and competitive salary reviews for junior staff.

## Files
- hr_cleaning.py — Full data inspection and cleaning pipeline
- hr_visualization.py — Attrition dashboard and charts
- HR-Employee-Attrition.csv — Raw dataset
- HR-Employee-Attrition-Cleaned-Data.csv — Cleaned dataset
- Netflix_Business_Dashboard.png — Visual dashboard
