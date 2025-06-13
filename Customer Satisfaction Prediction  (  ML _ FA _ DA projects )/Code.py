# Import Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the Dataset
file_path= "C:\\Users\\loges\\OneDrive\\Documents\\VSCodes\\PYTHON\\Unified Mentor\\Unified-Mentor\\Customer Satisfaction Prediction  (  ML _ FA _ DA projects )\\customer_support_tickets.csv"
df = pd.read_csv(file_path)  # actual path
print(df.shape)
print(df.columns)

# Preprocessing
# Drop rows with missing target variable
df = df.dropna(subset=['Customer Satisfaction Rating'])

# Handle remaining missing values
df = df.dropna()

# Encode categorical variables
le = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    df[col] = le.fit_transform(df[col].astype(str))

# Feature Selection
X = df.drop(columns=['Ticket ID', 'Customer Satisfaction Rating'])  # Drop non-useful features
y = df['Customer Satisfaction Rating']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model Training
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Feature Importance
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh', color='teal')
plt.title("Top 10 Important Features")
plt.xlabel("Importance")
plt.show()
