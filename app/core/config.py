from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AIRLINE_PASSENGER_SATISFACTION"

    # log settings
    LOG_LEVEL: str = "INFO"
    LOG_ADD_CONSOLE_HANDLER: bool = True
    LOG_ADD_FILE_HANDLER: bool = False
    LOG_FILE_PATH: str = ".temp/logs/aifare.log"

    MAIN_WORK_FOLDER: str = ".temp"
    INPUT_WORK_FOLDER: str = ".temp/input"
    OUTPUT_WORK_FOLDER: str = ".temp/output"
    VISUALIZATION_WORK_FILE: str = "app/data/data_visualize/__init__.py"
    INPUT_FILE_NAME: str = "aps.csv"

    LR_MODEL_FILE_NAME: str = "logistic_reg.sav"
    RF_MODEL_FILE_NAME: str = "random_forest.sav"
    SVM_MODEL_FILE_NAME: str = "svm.sav"
    LR_CLS_REPORT_FILE_NAME: str = "logistic_reg_cls_report.png"
    RF_CLS_REPORT_FILE_NAME: str = "random_forest_cls_report.png"
    SVM_CLS_REPORT_FILE_NAME: str = "svm_cls_report.png"
    CORR_FILE_NAME: str = "correlation_matrix.png"


settings = Settings()
