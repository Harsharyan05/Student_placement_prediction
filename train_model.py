import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from xgboost import XGBClassifier

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv("placement.csv")

# Remove unnecessary columns
df.drop(["sl_no", "salary"], axis=1, inplace=True)

# Convert target column
df["status"] = df["status"].map({
    "Placed": 1,
    "Not Placed": 0
})

# ==========================
# One Hot Encoding
# ==========================
categorical_cols = [
    "gender",
    "ssc_b",
    "hsc_b",
    "hsc_s",
    "degree_t",
    "workex",
    "specialisation"
]

df = pd.get_dummies(df, columns=categorical_cols)

# ==========================
# Features & Target
# ==========================
X = df.drop("status", axis=1)
y = df["status"]

# Save feature names for FastAPI
joblib.dump(X.columns.tolist(), "feature_names.pkl")

# ==========================
# Train Test Split
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# ==========================
# Models
# ==========================
models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=1000,
        max_depth=15,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42    
    ),

    "Gradient Boosting": GradientBoostingClassifier(
        n_estimators=300,
        learning_rate=0.05,
        random_state=42
    ),

    "XGBoost": XGBClassifier(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=5,
        random_state=42,
        eval_metric="logloss"
    )
}

best_model = None
best_accuracy = 0
best_name = ""

# ==========================
# Training Loop
# ==========================
for name, model in models.items():

    print("\n" + "="*50)
    print(f"Training {name}")
    print("="*50)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nAccuracy: {accuracy:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model
        best_name = name

# ==========================
# Save Best Model
# ==========================
joblib.dump(best_model, "placement_model.pkl")

print("\n" + "="*50)
print(f"Best Model: {best_name}")
print(f"Best Accuracy: {best_accuracy:.4f}")
print("Model Saved Successfully")
print("="*50)