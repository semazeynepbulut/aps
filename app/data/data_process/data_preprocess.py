import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from app.core.config import settings
from app.core.utils import create_directory_for_file
from app.core.logger import logger


class DataPreprocess:
    def __init__(self, data):
        self.data = data
        self.categorical_features = [
            "Gender",
            "Customer Type",
            "Type of Travel",
            "Class",
        ]
        self.imputer = SimpleImputer(strategy="median")
        self.label_encoder = LabelEncoder()
        self.preprocessor = None
        self.correlation_treshold = 0.9
        self.correlation_matrix = None
        self.numeric_features = None
        self.numeric_transformer = None
        self.categorical_encoder = None
        self.X = None
        self.Y = None
        self.X_train = None
        self.X_test = None
        self.Y_train = None
        self.Y_test = None

    def handle_missing_values(self):
        # Handle missing values for "Arrival Delay in Minutes" column, they are just 83 rows and we can use "median"
        self.data["Arrival Delay in Minutes"] = self.imputer.fit_transform(
            self.data[["Arrival Delay in Minutes"]]
        )

    def target_encoder(self):
        self.data["satisfaction_encoded"] = self.label_encoder.fit_transform(
            self.data["satisfaction"]
        )

    def correlation_analysis(self):
        # Correlation analysis
        self.correlation_matrix = self.data.corr(numeric_only=True)
        plt.figure(figsize=(15, 10))
        sns.heatmap(self.correlation_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.savefig(
            create_directory_for_file(
                settings.OUTPUT_WORK_FOLDER, settings.CORR_FILE_NAME
            )
        )
        logger.info(f"Correlation matrix file saved as {settings.CORR_FILE_NAME}")
        plt.show()

    # Define features and target
    def set_X_Y(self):
        self.Y = self.data["satisfaction_encoded"]
        self.X = self.data.drop(["satisfaction_encoded", "satisfaction"], axis=1)

    # Drop one of each pair of highly correlated columns
    def drop_highly_correlated(self):
        self.correlation_matrix = self.X.corr(numeric_only=True).abs()
        upper = self.correlation_matrix.where(
            np.triu(np.ones(self.correlation_matrix.shape), k=1).astype(bool)
        )
        to_drop = [
            column
            for column in upper.columns
            if any(upper[column] > self.correlation_treshold)
        ]
        logger.info(f"Dropped columns:{to_drop}")
        self.X.drop(columns=to_drop, inplace=True)

    # Encode categorical variables
    def categorical_columns_encoder(self):

        self.categorical_encoder = ColumnTransformer(
            transformers=[("cat", OneHotEncoder(), self.categorical_features)],
            remainder="passthrough",
        )

    # Create a pipeline for preprocessing numerical features
    def create_pipeline_for_numeric(self):
        # Create a pipeline for preprocessing numerical features
        self.numeric_features = self.X.select_dtypes(
            include=["int64", "float64"]
        ).columns
        self.numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

    # Combine transformers into a preprocessing pipeline
    def preprocessor_pipeline(self):
        self.preprocessor = ColumnTransformer(
            transformers=[
                ("num", self.numeric_transformer, self.numeric_features),
                ("cat", self.categorical_encoder, self.categorical_features),
            ]
        )

    # Split the data into training and testing sets
    def split(self):

        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.X, self.Y, test_size=0.2, random_state=42
        )

    def preprocess_x(self):
        self.X_train = self.preprocessor.fit_transform(self.X_train)
        self.X_test = self.preprocessor.transform(self.X_test)

    def _get(self):
        return (
            self.X_train,
            self.X_test,
            self.Y_train,
            self.Y_test,
        )

    @staticmethod
    def generate(data):
        prep = DataPreprocess(data=data)
        prep.handle_missing_values()
        prep.target_encoder()
        prep.set_X_Y()
        prep.correlation_analysis()
        prep.drop_highly_correlated()
        prep.categorical_columns_encoder()
        prep.create_pipeline_for_numeric()
        prep.preprocessor_pipeline()
        prep.split()
        prep.preprocess_x()
        return prep._get()
