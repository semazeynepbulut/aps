from app.data.data_process.task import data_preprocessing_task
from app.classification.cls import ClassificationModel


def classification_task():
    X_train, X_test, Y_train, Y_test = data_preprocessing_task()
    ClassificationModel.run_models(X_train, X_test, Y_train, Y_test)
