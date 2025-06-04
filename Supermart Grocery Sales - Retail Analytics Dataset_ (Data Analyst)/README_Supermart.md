
# 🛒 Supermart Grocery Sales – Data Analysis & Sales Prediction

This project analyzes sales data from a fictional Supermart grocery dataset. It involves data cleaning, exploration, visualization, and predictive modeling using linear regression.

---

## 📁 Dataset Overview

- **Source**: Supermart Grocery Sales - Retail Analytics Dataset
- **Records**: ~10,000 transactions  
- **Features**: Order ID, Customer Name, Category, Sub-Category, City, Order Date, Region, Sales, Discount, Profit, State, Month, Year  
- **Target Variable**: `Sales`

---

## 🧰 Tools & Libraries Used

- Python (Pandas, NumPy)
- Matplotlib & Seaborn for Visualization
- Scikit-learn (Label Encoding, Standardization, Linear Regression)

---

## 🔍 Project Workflow

### 1. Data Cleaning
- Removed missing and duplicate records.
- Converted `Order Date` to datetime format.
- Extracted `Order Month` and `Order Year`.

### 2. Label Encoding
- Encoded categorical features: Category, Sub-Category, City, Region, State.

### 3. Exploratory Data Analysis (EDA)
- **Boxplot**: Sales distribution by Category
- **Line Plot**: Total Sales over time
- **Heatmap**: Correlation among numerical features

### 4. Model Building
- **Features Used**: Category, Sub-Category, City, Region, State, Order Month, Order Year, Discount, Profit
- **Target**: Sales
- **Model**: Linear Regression
- **Train/Test Split**: 80/20

### 5. Model Evaluation
- **Mean Squared Error (MSE)**: Measures average prediction error.
- **R-squared Score**: Indicates how well the model explains variance in Sales.

### 6. Visualization
- Scatter plot comparing Actual vs Predicted sales with a reference line.

---

## 📝 How to Run

1. Clone the repository or copy the notebook/script.
2. Install the required libraries using:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Run the Python script or Jupyter Notebook in your preferred IDE.
4. Ensure `supermart_grocery_sales.csv` is in the same directory.

---

## 🔮 Possible Extensions

- Use other ML models like Decision Tree, Random Forest, or XGBoost.
- Perform hyperparameter tuning.
- Build a dashboard with Streamlit for live predictions.
