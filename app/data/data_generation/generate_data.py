from app.core.utils import create_directory_for_file
from app.core.config import settings
import pandas as pd


class GenerateData:
    deleted_columns = ["Unnamed: 0", "id"]

    def __init__(self):
        self.folder_path = None
        self.df = None

    def _read_csv(self):
        self.folder_path = create_directory_for_file(
            parent_folder=settings.INPUT_WORK_FOLDER, file_name=settings.INPUT_FILE_NAME
        )
        self.df = pd.read_csv(self.folder_path)
        self.df.drop(self.deleted_columns, axis=1, inplace=True)

    @staticmethod
    def generate():
        data = GenerateData()
        data._read_csv()
        return data.df
