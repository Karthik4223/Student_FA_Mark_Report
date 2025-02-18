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

def categorize_attendance_per(percentage):
    if percentage >= 75:
        return "75% and above"
    elif 65 <= percentage < 75:
        return "65–74%"
    elif 50 <= percentage < 65:
        return "50–64%"
    else:
        return "0–49%"

def process_sheet(sheet_name, df):
    st.write(f"### Processing Sheet: {sheet_name}")

    # Ensure the required columns exist
    if not set(["S.NO.", "REGD.", "CGPA", "Attendance", "Test 1", "Test 2", "Test 3", "Test 4"]).issubset(df.columns):
        st.error(f"The sheet '{sheet_name}' must contain the required columns.")
        return

    # Drop duplicates based on student registration number
    df = df.drop_duplicates(subset="REGD.")

    # Convert attendance to percentage if needed
    df["Attendance"] = df["Attendance"].apply(lambda x: float(str(x).strip('%')) if isinstance(x, str) and x.endswith('%') else x)

    # Add a category column
    df['Attendance_Percents'] = df["Attendance"].apply(lambda x: x * 100)
    df["Group"] = df["Attendance"].apply(categorize_attendance)

    # Convert test marks to integers, handling missing values
    for col in ["Test 1", "Test 2", "Test 3", "Test 4"]:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)
        df[col] = df[col].replace(-1, 0).apply(lambda x: int(x))

    # Calculate total marks
    df["Total Marks"] = df[["Test 1", "Test 2", "Test 3", "Test 4"]].sum(axis=1).astype(int)
    df["Total Marks"] = df["Total Marks"]*(3/4)

    # Display the entire data with total marks
    st.write("### Student Data with Total Marks")
    st.dataframe(df)

    # Create a report structure
    attendance_ranges = ["≥75%", "≥65% - <75%", "≥50% - <65%", "<50%"]
    columns = ["<=10", ">10 & <=20", ">20 & <=30", ">30 & <=40", ">40 & <=50",">50 & <=60", "Total"]

    # Initialize report data with zeros
    report_data = {col: [0] * len(attendance_ranges) for col in columns}

    # Count students based on attendance and marks
    for index, row in df.iterrows():
        group = row["Group"]
        total_marks = row["Total Marks"]

        if total_marks <= 10:
            column = "<=10"
        elif 10 < total_marks <= 20:
            column = ">10 & <=20"
        elif 20 < total_marks <= 30:
            column = ">20 & <=30"
        elif 30 < total_marks <= 40:
            column = ">30 & <=40"
        elif 40 < total_marks <= 50:
            column = ">40 & <=50"
        elif 50 < total_marks <= 60:
            column = ">50 & <=60"
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

    # Add attendance category
    df["Attendance_Category"] = df["Attendance_Percents"].apply(categorize_attendance_per)

    # Count students in each category
    attendance_counts = df["Attendance_Category"].value_counts().reindex([
        "0–49%", "50–64%", "65–74%", "75% and above"
    ], fill_value=0)

    # Display the report as a table
    st.write("### Attendance Range Report")
    report1_df = pd.DataFrame({
        "Attendance Range": attendance_counts.index,
        "No. of Students": attendance_counts.values
    })
    st.table(report1_df)

def main():
    st.title("Student FA Marks Report")

    # Add instructions for the required Excel format
    st.markdown(
        """
        **📂 Excel File Requirements:**  
        The uploaded file must contain the following columns:  
        - `S.NO.`  
        - `REGD.` (Registration Number)  
        - `CGPA`  
        - `Attendance` (as a percentage, e.g., `75%`)  
        - `Test 1`, `Test 2`, `Test 3`, `Test 4`
        - ✅ **Supports multiple sheets**: The application will process and display reports for each sheet in the uploaded Excel file.
        """
    )

    uploaded_file = st.file_uploader("Upload the Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Read all sheets from the Excel file
        xls = pd.read_excel(uploaded_file, sheet_name=None)

        # Process each sheet
        for sheet_name, df in xls.items():
            process_sheet(sheet_name, df)

if __name__ == "__main__":
    main()
