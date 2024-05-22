import argparse

from app.core.config import settings
from app.data.__init__ import vis_task
from app.classification.__init__ import cls_task


def add_visualization(parser):
    parser.add_argument(
        "--v",
        action="store_true",
        help="visualize descriptive analytics detail.",
    )
    parser.set_defaults(func=vis_task)


def add_classification(parser):
    parser.add_argument(
        "--c",
        action="store_true",
        help="preprocess data and run 3 models",
    )
    parser.set_defaults(func=cls_task)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--aps")

    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    parser_visualization = subparsers.add_parser(
        "visualize",
        help="Starts visualization tasks.",
    )
    parser_classification = subparsers.add_parser(
        "classify", help="Starts classification tasks."
    )
    add_visualization(parser=parser_visualization)
    add_classification(parser=parser_classification)
    args = parser.parse_args()
    args.func(args)
