from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from app.core.logger import logger
from app.core.config import settings
from app.core.utils import save_model, create_directory_for_file
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class ClassificationModel:
    def __init__(
        self,
        X_train: np.ndarray,
        X_test: np.ndarray,
        Y_train: pd.Series,
        Y_test: pd.Series,
    ):
        self.X_train = X_train
        self.X_test = X_test
        self.Y_train = Y_train
        self.Y_test = Y_test
        self.y_pred_list = []
        self.accuracy_list = []
        self.log_reg_model = LogisticRegression(random_state=42)
        self.ran_for_model = RandomForestClassifier(random_state=42)
        self.svc_model = SVC(random_state=42)

    @staticmethod
    def run_model(model, X_train, Y_train, filename):
        model.fit(X_train, Y_train)
        save_model(model, filename)
        logger.info(f"Model file saved as {filename}")
        return model

    @staticmethod
    def calculate_accuracy(model, X_test, Y_test) -> float:
        Y_pred = model.predict(X_test)
        return Y_pred, accuracy_score(Y_test, Y_pred)

    @staticmethod
    def save_classification_report_as_png(Y_test, Y_pred, filename):
        report = classification_report(Y_test, Y_pred, output_dict=True)
        report_df = pd.DataFrame(report).transpose()

        plt.figure(figsize=(10, 6))
        sns.heatmap(report_df.iloc[:-1, :].T, annot=True, cmap="Blues", cbar=False)
        plt.title("Classification Report")
        plt.savefig(create_directory_for_file(settings.OUTPUT_WORK_FOLDER, filename))
        logger.info(f"Classification report saved as {filename}")
        plt.close()

    def run_log_reg(self):
        self.log_reg_model = self.run_model(
            self.log_reg_model, self.X_train, self.Y_train, settings.LR_MODEL_FILE_NAME
        )
        p, a = self.calculate_accuracy(self.log_reg_model, self.X_test, self.Y_test)
        self.y_pred_list = self.y_pred_list + [p]
        self.accuracy_list = self.accuracy_list + [a]
        logger.info(f"Logistic Regression Accuracy:{a}")
        self.save_classification_report_as_png(
            self.Y_test, p, settings.LR_CLS_REPORT_FILE_NAME
        )

    def run_ran_for(self):
        self.ran_for_model = self.run_model(
            self.ran_for_model, self.X_train, self.Y_train, settings.RF_MODEL_FILE_NAME
        )
        p, a = self.calculate_accuracy(self.ran_for_model, self.X_test, self.Y_test)
        self.y_pred_list = self.y_pred_list + [p]
        self.accuracy_list = self.accuracy_list + [a]
        logger.info(f"Random Forrest Accuracy:{a}")
        self.save_classification_report_as_png(
            self.Y_test, p, settings.RF_CLS_REPORT_FILE_NAME
        )

    def run_svc(self):
        self.svc_model = self.run_model(
            self.svc_model, self.X_train, self.Y_train, settings.SVM_MODEL_FILE_NAME
        )
        p, a = self.calculate_accuracy(self.svc_model, self.X_test, self.Y_test)
        self.y_pred_list = self.y_pred_list + [p]
        self.accuracy_list = self.accuracy_list + [a]
        logger.info(f"SVM Accuracy:{a}")
        self.save_classification_report_as_png(
            self.Y_test, p, settings.SVM_CLS_REPORT_FILE_NAME
        )

    @staticmethod
    def run_models(X_train, X_test, Y_train, Y_test):
        cls_models = ClassificationModel(X_train, X_test, Y_train, Y_test)
        cls_models.run_log_reg()
        cls_models.run_ran_for()
        cls_models.run_svc()
