"""تدريب نموذج شجرة القرار وتقييمه باستخدام بيانات اصطناعية."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data.csv"
FEATURES = ["phishing_score", "privacy_score", "password_score", "errors"]
LABELS = ["التصيد الإلكتروني", "حماية الخصوصية", "كلمات المرور"]

def train_and_evaluate():
    data = pd.read_csv(DATA_PATH)
    X = data[FEATURES]
    y = data["recommended_topic"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=47, stratify=y
    )

    model = DecisionTreeClassifier(
        max_depth=4, min_samples_leaf=3, random_state=47
    )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, average="weighted", zero_division=0),
        "recall": recall_score(y_test, predictions, average="weighted", zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, predictions, labels=LABELS),
        "labels": LABELS,
        "train_size": len(X_train),
        "test_size": len(X_test),
        "total_size": len(data),
    }
    return model, metrics

def predict_topic(model, phishing_score, privacy_score, password_score, errors):
    sample = pd.DataFrame([{
        "phishing_score": phishing_score,
        "privacy_score": privacy_score,
        "password_score": password_score,
        "errors": errors
    }])
    prediction = model.predict(sample)[0]
    probabilities = model.predict_proba(sample)[0]
    confidence = float(max(probabilities))
    return prediction, confidence
