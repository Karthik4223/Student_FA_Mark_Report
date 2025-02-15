import streamlit as st
import pandas as pd
import numpy as np

def categorize_attendance(percentage):
    percentage = percentage * 100
    if percentage >= 75:
        return "≥75%"
    elif 65 <= percentage < 75:
        return "≥65% - <75%"
    elif 50 <= percentage < 65:
        return "≥50% - <65%"
    else:
        return "<50%"

def main():
    st.title("Student FA Marks Report")

    uploaded_file = st.file_uploader("Upload the Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Read the Excel file
        df = pd.read_excel(uploaded_file)

        # Ensure the required columns exist
        if not set(["S.NO.", "REGD.", "CGPA", "Attendance", "Test 1", "Test 2", "Test 3", "Test 4"]).issubset(df.columns):
            st.error("The file must contain 'S.NO.', 'REGD.', 'CGPA', 'Attendance', 'Test 1', 'Test 2', 'Test 3', 'Test 4' columns.")
            return

        # Drop duplicates based on student registration number
        df = df.drop_duplicates(subset="REGD.")

        # Convert attendance to percentage if needed
        df["Attendance"] = df["Attendance"].apply(lambda x: float(str(x).strip('%')) if isinstance(x, str) and x.endswith('%') else x)

        # Add a category column
        df["Group"] = df["Attendance"].apply(categorize_attendance)

        # Convert test marks to integers, handling missing values
        for col in ["Test 1", "Test 2", "Test 3", "Test 4"]:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

        # Calculate total marks
        df["Total Marks"] = df[["Test 1", "Test 2", "Test 3", "Test 4"]].sum(axis=1).astype(int)

        # Display the entire data with total marks
        st.write("### Student Data with Total Marks")
        st.dataframe(df)

        # Create a report structure
        attendance_ranges = ["≥75%", "≥65% - <75%", "≥50% - <65%", "<50%"]
        columns = ["<=20", ">20 & <=40", ">40 & <=60", ">60 & <=70", ">70 & <=80", "Total"]

        # Initialize report data with zeros
        report_data = {col: [0] * len(attendance_ranges) for col in columns}

        # Count students based on attendance and marks
        for index, row in df.iterrows():
            group = row["Group"]
            total_marks = row["Total Marks"]

            if total_marks <= 20:
                column = "<=20"
            elif 20 < total_marks <= 40:
                column = ">20 & <=40"
            elif 40 < total_marks <= 60:
                column = ">40 & <=60"
            elif 60 < total_marks <= 70:
                column = ">60 & <=70"
            elif 70 < total_marks <= 80:
                column = ">70 & <=80"
            else:
                continue

            report_data[column][attendance_ranges.index(group)] += 1
            report_data["Total"][attendance_ranges.index(group)] += 1

        # Calculate the total row
        report_df = pd.DataFrame(report_data, index=attendance_ranges)
        report_df.loc['Total'] = [sum(report_df[col]) for col in columns]

        report_df.reset_index(inplace=True)
        report_df.rename(columns={'index': 'Attendance'}, inplace=True)
        
        # Display the FA Marks Report
        st.write("### FA Marks Report")
        st.table(report_df)

if __name__ == "__main__":
    main()