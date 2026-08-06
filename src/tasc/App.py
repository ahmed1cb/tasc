# Python Mods
import json
import os

# Lib To manage files for all platforms
from platformdirs import user_data_dir


class Tasc:
    def __init__(self) -> None:

        self.tasks = {}
        self.tasks_file_dir = os.path.join(user_data_dir("Tasc"), "Stored")
        self.tasks_file_path = os.path.join(
            user_data_dir("Tasc"), "Stored", "tasks.json"
        )

        self.allowed = {
            "add": "Add A new Task , usage: tasc add :content",
            "del": "Delete Task By id , usage: tasc del :id",
            "list": "List all Tasks , usage: tasc list",
            "edit": "Edit Task By id , usage: tasc edit :id :newContent",
            "complete": "Complete a Task By Id , usage: tasc complete :id",
        }
        if not os.path.exists(self.tasks_file_path):
            self._init_app()
        if not self.tasks:
            self.load_tasks()

    def handle(self, argv: list):
        allowed = list(self.allowed.keys())
        handlers = {
            "add": self._add,
            "del": self._drop,
            "edit": self._update,
            "list": self._list,
            "complete": self._complete,
        }
        if argv[0] not in allowed:
            print(f"Option Not Found {argv[0]}")
            print("*" * 10 + " Allowed Actions " + "*" * 10)
            for key in allowed:
                print(f"{key} => {self.allowed[key]}")
            return
        handlers[argv[0]](*argv[1:])

    def _init_app(self):
        os.makedirs(self.tasks_file_dir, exist_ok=True)
        with open(self.tasks_file_path, "w") as file:
            file.write("{}")

    def _add(self, *body: str):
        if not body:
            print("Add Action Requires Task Body, Usage tasc add :body")
            return
        id = len(self.tasks) + 1
        task = {"body": " ".join(body), "completed": False}
        self.tasks[id] = task
        self._edit_json(self.tasks)

    def _drop(self, id: int): ...
    def _update(self, id: int, body: str): ...
    def _complete(self, id: int):
        target = self.tasks.get(id)
        if target is None:
            print("The Target Task is Not Found Try: tasc list")
            return
        new = self.tasks[id]
        new["completed"] = True
        self.tasks[id] = new
        self._edit_json(self.tasks)

    def _list(self):
        print("*" * 10 + " Tasks " + "*" * 10)
        for id in self.tasks:
            task = self.tasks.get(id)
            print(
                f"{'[x]' if task['completed'] is True else '[]'} {id} : {task['body']}"
            )

    def _edit_json(self, newData: dict):
        with open(self.tasks_file_path, "w", encoding="utf-8") as file:
            json.dump(newData, file)

    def load_tasks(self):
        with open(self.tasks_file_path, "r", encoding="utf-8") as file:
            self.tasks = json.loads(file.read())
