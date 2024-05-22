import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from catboost import CatBoostClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# Load your data from the CSV file
data = pd.read_csv(r'C:\Users\nimma\OneDrive\Desktop\Book2.csv')

# Assuming 'X' contains 24 features, and 'y' contains the labels
columns_to_drop = ['0', '1', '2', ..., '95']
X = data.drop(columns='96', axis=1)
y = data['96']

# Split your data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Models
models = {

    #'SVM': SVC(),
    #'KNN': KNeighborsClassifier(),
    'XGBoost': GradientBoostingClassifier(),
    #'CatBoost': CatBoostClassifier(),
    'AdaBoost': AdaBoostClassifier(),
    'XtraGradientBoost': XGBClassifier(),
    'RandomForest': RandomForestClassifier()
}

for model_name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)
   
    # Make predictions on the testing data
    y_pred = model.predict(X_test)
    print(f"{model_name} predictions: {y_pred}")

    # Calculate accuracy (uncomment the following lines if you have the true labels for the new data)
    # accuracy = accuracy_score(y_pred, y_test)
    #print(f"{model_name} - Accuracy on the new data: {accuracy:.2f}")