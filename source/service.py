# third layer of todo list app, controls the data that enter database,

from source.models import Task


class TaskService:
    def __init__(self, repository):
        self.repository = repository

    # function for id out-of-range user call, answer to user
    def no_task_promt(self, id):
        return f"no task with id: {id}"

    # check if task is in database by id or name
    def find_task(self, id):
        for task in self.repository.get_all_entries():
            if id in [element for element in task]:
                return True
        return False

    # creates task with name and optional description
    def create_task(self, name, description=""):
        if not self.find_task(name):
            self.repository.insert_entry(name, description)
        else:
            return "task is already exists"

    # deletes task by id
    def delete_task(self, id):
        if self.find_task(id):
            self.repository.delete_entry(id)
        else:
            self.no_task_promt(id)

    # edit task by id, need to change description
    def edit_task(self, id, description):
        if self.find_task(id):
            self.repository.edit_entry(id, description)
        else:
            self.no_task_promt(id)

    # lists all tasks, returns Task(id={task_id},name={task_name}, decription={task_description})
    # check models.py
    def get_all_tasks(self):
        rows = self.repository.get_all_entries()
        return [Task(*row) for row in rows]

    # returns task by id
    def get_task_by_id(self, id):
        if self.find_task(id):
            row = self.repository.get_entry_by_id(id)
            return Task(*row)
        else:
            return self.no_task_promt(id)

    def print_task(self, task_list):
        if isinstance(task_list, list):
            for task in task_list:
                print(f"{task.id} | {task.name} | {task.description}")
