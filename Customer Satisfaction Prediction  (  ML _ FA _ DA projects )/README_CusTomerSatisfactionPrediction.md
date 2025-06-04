# 😊 Customer Satisfaction Prediction – Machine Learning Project

This project aims to predict customer satisfaction based on historical support ticket data. It uses supervised learning (Random Forest Classifier) to classify satisfaction ratings and identify the most influential features.

---

## 📁 Dataset Overview

- **Source**: customer_support_tickets Dataset  
- **Records**: ~8,400+ entries  
- **Target Variable**: `Customer Satisfaction Rating` (1 to 5 scale)  
- **Features**: Includes customer age, gender, ticket type, channel, response time, resolution time, etc.

---

## 🧰 Tools & Libraries Used

- Python (Pandas, NumPy)
- Seaborn & Matplotlib for Visualization
- Scikit-learn (Label Encoding, Scaling, Random Forest, Metrics)

---

## 🔍 Project Workflow

### 1. Data Preprocessing
- Removed records with missing satisfaction ratings or other fields.
- Encoded categorical variables using `LabelEncoder`.

### 2. Feature Selection
- Removed unnecessary columns such as Ticket ID.
- Selected relevant predictors for model training.

### 3. Model Building
- **Algorithm**: Random Forest Classifier
- **Train/Test Split**: 70% training, 30% testing
- **Scaling**: Standardized features using `StandardScaler`

### 4. Model Evaluation
- **Accuracy Score**: Measures overall prediction accuracy.
- **Confusion Matrix**: Visualizes prediction errors.
- **Classification Report**: Includes precision, recall, and F1-score for each satisfaction level.

### 5. Feature Importance
- Visualized the top 10 features impacting satisfaction prediction.

---

## 📊 Visualization

- Bar plot of the top 10 most important features affecting customer satisfaction.
- Helps understand which features (e.g., ticket type, response time) matter most.

---

## 🚀 How to Run

1. Download or clone the project.
2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
