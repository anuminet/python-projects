FILENAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = [line.strip() for line in f if line.strip()]
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("  No tasks yet!")
    else:
        print()
        for i, task in enumerate(tasks, start=1):
            print(f"  {i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'  Added: "{task}"')
    else:
        print("  Task cannot be empty.")


def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter task number to remove: ").strip()) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f'  Removed: "{removed}"')
        else:
            print("  Invalid task number.")
    except ValueError:
        print("  Please enter a valid number.")


def main():
    tasks = load_tasks()

    print("=" * 40)
    print("         To-Do List Manager")
    print("=" * 40)

    menu = """
  1. View tasks
  2. Add task
  3. Remove task
  4. Quit
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("  Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
