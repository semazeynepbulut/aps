from pathlib import Path
from typing import Union
from app.core.config import settings
import joblib


def create_directory(item: str) -> Path:
    return Path().resolve().joinpath(item)


def create_directory_for_file(parent_folder: Union[str, Path], file_name: str) -> Path:
    if isinstance(parent_folder, str):
        file_path_str = parent_folder + "/" + file_name
        return create_directory(item=file_path_str)
    if isinstance(parent_folder, Path):
        return parent_folder.joinpath(file_name)


def save_model(model, filename):
    joblib.dump(model, create_directory_for_file(settings.OUTPUT_WORK_FOLDER, filename))


def upload_model(filename):
    return joblib.load(create_directory_for_file(settings.OUTPUT_WORK_FOLDER, filename))
