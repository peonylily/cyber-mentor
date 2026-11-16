"""يمكن تشغيل هذا الملف يدويًا لتدريب النموذج وعرض نتائج التقييم."""
from model import train_and_evaluate

if __name__ == "__main__":
    model, metrics = train_and_evaluate()
    print("تم تدريب نموذج شجرة القرار على بيانات اصطناعية.")
    print(f"عدد سجلات التدريب: {metrics['train_size']}")
    print(f"عدد سجلات الاختبار: {metrics['test_size']}")
    print(f"Accuracy: {metrics['accuracy']:.3f}")
    print(f"Precision (weighted): {metrics['precision']:.3f}")
    print(f"Recall (weighted): {metrics['recall']:.3f}")
    print("Confusion matrix:")
    print(metrics["confusion_matrix"])
