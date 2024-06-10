import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import tkinter as tk
from tkinter import messagebox

file_path = 'mix_hand_and_screw_data.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip', sep=',')

X = data[['GX', 'GY', 'GZ', 'AX', 'AY', 'AZ']]
y = data['group']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

param_grid = {
    'C': [1, 10],
    'gamma': [0.01, 0.001],
    'kernel': ['rbf']
}

grid_search = GridSearchCV(SVC(random_state=42), param_grid, cv=3, scoring='accuracy')
grid_search.fit(X_train, y_train)
svm_model = grid_search.best_estimator_


def predict():
    try:
        input_data = [float(x) for x in entry.get().split(',')]
        if len(input_data) != 6:
            raise ValueError("Please enter 6 position data")
        new_data = [input_data]
        prediction = classify_new_data(new_data)
        result_label.config(text=f"Prediction: {prediction[0]}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def classify_new_data(new_data):
    new_df_scaled = scaler.transform(new_data)
    predictions = svm_model.predict(new_df_scaled)
    return predictions


# Tkinter GUI
root = tk.Tk()
root.title("Prediction Application")

tk.Label(root, text="Enter values 'GX', 'GY', 'GZ', 'AX', 'AY', 'AZ' in order:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

tk.Button(root, text="Predict", command=predict).pack(pady=10)
result_label = tk.Label(root, text="Predict: ")
result_label.pack(pady=10)

root.mainloop()
