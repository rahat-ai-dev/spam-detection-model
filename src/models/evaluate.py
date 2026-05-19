from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

def evaluate_model(model,x_test,y_test):
    y_pred=model.predict(x_test)

    print(f'Accuracy: {accuracy_score(y_test,y_pred):.4f}')
    print(f'Precision: {precision_score(y_test,y_pred):.4f}')
    print(f'Recall: {recall_score(y_test,y_pred):.4f}')
    print(f'F1 Score: {f1_score(y_test,y_pred):.4f}')
    print()
    print(classification_report(y_test,y_pred,target_names=['Ham','Spam']))
    