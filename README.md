# Student_FA_Mark_Report

📊 **Student Attendance Grouping and FA Marks Report**

A Streamlit application designed to automate student performance tracking, attendance categorization, and FA marks reporting from Excel workbooks.

## 🚀 Recent Updates
- **Dual Processing Modes**: Toggle between Standard (Test 1-4) and Extended (Test 1-4 + T1-4) marks calculation.
*   **Multi-Format Export**: Download reports as **Excel (.xlsx)**, **PDF**, or **Word (.docx)**.
- **Strict Validation**: Intelligent column detection with anti-conflict errors in Standard mode and mandatory column checks in Extended mode.
- **Dynamic Filenaming**: Exports now automatically include the original uploaded filename for better organization.

## 🛠️ Features
- **Attendance Grouping**: Categorizes students into four groups: ≥75%, 65-75%, 50-65%, and <50%.
- **Flexible FA Marks Calculation**:
    - **Standard Mode formula**: `(Test 1 + Test 2 + Test 3 + Test 4) * 0.75`
    - **Extended Mode formula**: `((Test 1 + Test 2 + Test 3 + Test 4) * 0.75 + (T1 + T2 + T3 + T4)) / 2`
- **Performance Distribution**: Generates a matrix report showing students count across attendance groups and FA mark ranges (0 to 60).
- **Supports Multiple Sheets**: Automatically processes every sheet in the uploaded workbook.

## 📂 File Upload Requirements

### **Base Columns (Required for all modes)**
- `S.NO.`
- `REGD.` (Registration Number)
- `CGPA`
- `Attendance` (e.g., `75%`)

### **Mode-Specific Test Columns**
- **Standard Mode**: Requires strictly either [`Test 1`, `Test 2`, `Test 3`, `Test 4`] OR [`T1`, `T2`, `T3`, `T4`].
- **Extended Mode**: Requires **all 8 columns**: [`Test 1`, `Test 2`, `Test 3`, `Test 4`, `T1`, `T2`, `T3`, `T4`].

## 🚀 Installation & Running

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## 📂 How It Works
1. **Upload**: Select an Excel file matching the required column formats.
2. **Switch Modes**: Use the buttons at the top to select the correct processing logic for your data.
3. **Analyze**: View the live-rendered Student Data, FA Marks Report, and Attendance Summary.
4. **Export**: Choose your format (Excel, PDF, or Word) and download the final report.
