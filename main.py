import argparse
from task_manager import TaskManager


def main():
    parser = argparse.ArgumentParser(
        description="Python CLI Task Manager"
    )

    parser.add_argument(
        "command",
        help="Command to execute (add, list, delete)"
    )

    parser.add_argument(
        "task",
        nargs="?",
        help="Task description"
    )

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        if args.task:
            task_manager.add_task(args.task)
        else:
            print("Please provide a task.")

    elif args.command == "list":
        task_manager.list_tasks()

    else:
        print(f"Unknown command: {args.command}")
        print("Available commands: add, list, delete")


if __name__ == "__main__":
    main()