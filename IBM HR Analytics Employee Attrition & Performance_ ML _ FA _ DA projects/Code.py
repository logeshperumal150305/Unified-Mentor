# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

# Load Dataset
file_path= "C:\\Users\\loges\\OneDrive\\Documents\\VSCodes\\PYTHON\\Unified Mentor\\IBM HR Analytics Employee Attrition & Performance_ ML _ FA _ DA projects\\WA_Fn-UseC_-HR-Employee-Attrition.csv"
df = pd.read_csv(file_path)

# Basic Info
print("Dataset shape:", df.shape)
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())
print("\nData Types:\n", df.dtypes)

# Summary Statistics
print("\nSummary:\n", df.describe(include='all'))

# Attrition Rate
attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
print("\nAttrition Rate:\n", attrition_rate)

# Plot Attrition Rate
plt.figure(figsize=(6,4))
sns.barplot(x=attrition_rate.index, y=attrition_rate.values)
plt.title("Employee Attrition Rate")
plt.ylabel("Percentage")
plt.xlabel("Attrition")
plt.show()

# Average Tenure
print("Average years at company:", round(df['YearsAtCompany'].mean(), 2))

# Demographics Distribution
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

sns.histplot(df['Age'], kde=True, ax=axes[0])
axes[0].set_title("Age Distribution")

sns.countplot(data=df, x='Gender', ax=axes[1])
axes[1].set_title("Gender Distribution")

sns.countplot(data=df, x='Department', ax=axes[2])
axes[2].set_title("Department Distribution")

plt.tight_layout()
plt.show()

# Attrition by Age
plt.figure(figsize=(8, 4))
sns.kdeplot(data=df[df['Attrition'] == 'Yes'], x='Age', fill=True, label='Attrition = Yes')
sns.kdeplot(data=df[df['Attrition'] == 'No'], x='Age', fill=True, label='Attrition = No')
plt.title("Attrition by Age")
plt.legend()
plt.show()

# Attrition Rate by Gender
gender_attrition = df.groupby('Gender')['Attrition'].value_counts(normalize=True).unstack().fillna(0)['Yes'] * 100

plt.figure(figsize=(6, 4))
sns.barplot(x=gender_attrition.index, y=gender_attrition.values)
plt.title("Attrition Rate by Gender")
plt.ylabel("Attrition Rate (%)")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12,10))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()
