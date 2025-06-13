# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the Dataset
df = pd.read_csv('C:\\Users\\loges\\OneDrive\\Documents\\VSCodes\\PYTHON\\Unified Mentor\\Unified-Mentor\\Supermart Grocery Sales - Retail Analytics Dataset_ (Data Analyst)\\Supermart Grocery Sales - Retail Analytics Dataset.csv')  # <- replace with your actual file path
print(df.head())

# Data Cleaning
df.drop_duplicates(inplace=True)

# Convert 'Order Date' to datetime (coerce errors to NaT)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Order Month'] = df['Order Date'].dt.month
df['Order Year'] = df['Order Date'].dt.year

# Drop rows with any NaN values (after date conversion)
df.dropna(inplace=True)

# Label Encoding
le = LabelEncoder()
for col in ['Category', 'Sub Category', 'City', 'Region', 'State']:
    df[col] = le.fit_transform(df[col].astype(str))

# EDA - Sales by Category
sns.boxplot(x='Category', y='Sales', data=df, palette='Set2')
plt.title('Sales Distribution by Category')
plt.show()

# EDA - Sales Over Time
df.groupby('Order Date')['Sales'].sum().plot()
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Correlation Heatmap (only numeric columns)
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Prepare Data for ML
features = df.drop(columns=['Order ID', 'Customer Name', 'Order Date', 'Sales'])
target = df['Sales']

# Ensure there are no NaN values in final dataset
df = df.dropna(subset=features.columns.tolist() + ['Sales'])

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate Model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")

# Actual vs Predicted Plot
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.show()
