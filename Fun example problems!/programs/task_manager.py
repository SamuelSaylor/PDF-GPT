import json
import os

DATA_FILE = "tasks.json"

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["completed"])


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        data = json.load(f)
        return [Task.from_dict(t) for t in data]


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)


def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return

    for i, t in enumerate(tasks):
        status = "✓" if t.completed else "✗"
        print(f"{i}: [{status}] {t.title}")


def add_task(tasks):
    title = input("Task title: ")
    tasks.append(Task(title))


def complete_task(tasks):
    idx = int(input("Index: "))
    if 0 <= idx < len(tasks):
        tasks[idx].completed = True


def delete_task(tasks):
    idx = int(input("Index: "))
    if 0 <= idx < len(tasks):
        tasks.pop(idx)


def main():
    tasks = load_tasks()

    while True:
        print("\n1:Add 2:List 3:Done 4:Delete 5:Quit")
        choice = input("> ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            print_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid")

        save_tasks(tasks)


if __name__ == "__main__":
    main()