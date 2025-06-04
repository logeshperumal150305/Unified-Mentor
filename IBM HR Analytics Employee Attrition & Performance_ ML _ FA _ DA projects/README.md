
# 📊 IBM HR Analytics – Employee Attrition & Performance Analysis

This project focuses on analyzing employee attrition data from a fictional IBM dataset. Using Python, we explore the demographics, tenure, and department trends that influence employee attrition, with clear visualizations and statistical insights.

---

## 📁 Dataset Overview

- **Source**: WA_Fn-UseC_-HR-Employee-Attrition Dataset  
- **Records**: 1,470 employees  
- **Target Variable**: `Attrition` (Yes/No)  
- **Features**: 35 features including Age, Gender, Department, JobRole, YearsAtCompany, etc.

---

## 🧰 Tools & Libraries Used

- Python (Pandas, NumPy)
- Matplotlib & Seaborn for Visualization
- Jupyter Notebook

---

## 🔍 Project Objectives

- Understand key demographic and organizational factors driving employee attrition.
- Calculate overall attrition rate.
- Visualize trends by age, gender, and department.
- Correlate numerical features to detect patterns.
- Identify insights for improving employee retention.

---

## 📌 Key Steps & Analysis

### 1. **Data Exploration**
- Checked for missing and duplicate entries.
- Displayed dataset summary and types.

### 2. **Attrition Rate**
- **Overall Attrition Rate**: ~16.12%
- Calculated as the percentage of employees marked as `Attrition = Yes`.

### 3. **Tenure**
- **Average Years at Company**: ~7 years

### 4. **Demographic Distributions**
- **Age Distribution**: Most employees are between 30–40 years old.
- **Gender**: Slightly more males than females.
- **Department**: Highest count in R&D.

### 5. **Attrition by Age**
- Younger employees (under 35) are more likely to leave the company.

### 6. **Attrition by Gender**
- Male and female employees have similar attrition patterns with slight variations.

### 7. **Correlation Heatmap**
- Strongest positive correlations:
  - TotalWorkingYears vs Age
  - MonthlyIncome vs JobLevel
- Moderate negative correlation between YearsAtCompany and Attrition.

---

## 📊 Visualizations

- Bar plots, histograms, and KDE plots for distribution analysis.
- Heatmap for numerical correlations.
- Grouped bar plots to compare attrition by gender and age.

---

## 📁 Files

- `hr_attrition_analysis.ipynb`: Jupyter notebook containing full code and visualizations.
- `WA_Fn-UseC_-HR-Employee-Attrition.csv`: Dataset used (not included here, please download separately).

---

## 🚀 How to Run

1. Clone the repository or download the notebook.
2. Install dependencies (if needed):  
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run the notebook in Jupyter or any Python IDE.

---

## 📌 Future Work

- Build predictive models using classification algorithms (e.g., Logistic Regression, Random Forest).
- Perform feature importance analysis.
- Create dashboards using Plotly/Streamlit for interactive exploration.

---

## 📎 References

- IBM HR Attrition Dataset – [Kaggle Link](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
