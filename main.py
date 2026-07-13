import argparse
from task_manager import TaskManager


def main():

    parser = argparse.ArgumentParser(
        description="Python CLI Task Manager"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Add command
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new task"
    )

    add_parser.add_argument(
        "task",
        help="Task description"
    )

    # List command
    subparsers.add_parser(
        "list",
        help="Display all tasks"
    )

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task"
    )

    delete_parser.add_argument(
        "task_number",
        type=int,
        help="Task number to delete"
    )

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        task_manager.add_task(args.task)

    elif args.command == "list":
        task_manager.list_tasks()
    elif args.command == "delete":
        task_manager.delete_task(args.task_number)

    # Delete command
   


if __name__ == "__main__":
    main()