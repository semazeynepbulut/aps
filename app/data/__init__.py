from app.core.utils import create_directory
from app.core.config import settings
import subprocess


def vis_task(args):
    if args.v:
        process = subprocess.Popen(
            [
                "streamlit",
                "run",
                create_directory(settings.VISUALIZATION_WORK_FILE),
            ]
        )
