from app.classification.task import classification_task


def cls_task(args):
    if args.c:
        classification_task()
