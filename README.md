# Student_FA_Mark_Report

📊 Student Attendance Grouping and FA Marks Report
This Streamlit application processes student attendance and test scores from an uploaded Excel file and categorizes students based on their attendance percentages and total test marks.

🛠️ Features
Attendance Grouping: Categorizes students into four attendance groups:

≥75%
≥65% - <75%
≥50% - <65%
<50%
FA Marks Calculation: Sums up marks from Test 1, Test 2, Test 3, and Test 4.

Performance Distribution: Generates a report showing the distribution of students across different attendance groups and FA mark ranges:

<=20
>20 & <=40
>40 & <=60
>60 & <=70
>70 & <=80

📂 File Upload Requirements
Ensure the uploaded Excel file contains the following columns:

S.NO.
REGD. (Registration Number)
CGPA
Attendance (as a percentage, e.g., 75%)
Test 1, Test 2, Test 3, Test 4
🚀 How It Works
Upload the File:
Upload an Excel file with the specified columns.

Data Cleaning:

Duplicates are removed based on the "REGD." column.
Attendance values with percentages (e.g., 75%) are converted to numeric form.
Attendance Categorization:
Attendance is grouped into one of the four predefined categories.

FA Marks Calculation:
Marks from Test 1 to Test 4 are summed to calculate the total FA marks.

FA Marks Report:
Displays a table with rows for attendance categories and columns for different FA marks ranges.
