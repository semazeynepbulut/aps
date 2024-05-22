from app.data.data_process.data_preprocess import DataPreprocess
from app.data.data_generation.generate_data import GenerateData


def data_preprocessing_task():
    data = GenerateData().generate()
    X_train, X_test, Y_train, Y_test = DataPreprocess.generate(data=data)
    return X_train, X_test, Y_train, Y_test
