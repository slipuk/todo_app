from source.database import get_connection
from source.repository import TaskRepository
from source.service import TaskService


def main():
    connection = get_connection()
    repository = TaskRepository(connection)
    repository.create_table()
    service = TaskService(repository)

    print("todo app")

    while True:
        print("view all tasks press 1")
        print("create task press 2")
        print("edit task press 3")
        print("delete task press 4")
        print("find task by id press 5")

        try:
            user_input = int(input(">"))
        except ValueError:
            print("Enter a valid number(")
            continue

        if user_input == 1:
            service.print_task(service.get_all_tasks())

        if user_input == 2:
            user_input_name = input("Enter a name\n>")
            user_input_description = input("enter a description (blank for none)\n>")
            print(service.create_task(user_input_name, user_input_description))

        if user_input == 3:
            try:
                user_input_id = int(input("Enter task id\n> "))
            except ValueError:
                print("Enter a proper number")
                continue
            if user_input_id <= 0:
                print("Enter a proper number")
                continue
            user_input_description = input("Enter a new description\n> ")
            print(service.edit_task(user_input_id, user_input_description))

        if user_input == 4:
            try:
                user_input_id = int(input("Enter task id\n> "))
            except ValueError:
                print("Enter a proper number")
                continue
            if user_input_id <= 0:
                print("Enter a proper number")
                continue
            print(service.delete_task(user_input_id))

        if user_input == 5:
            try:
                user_input_id = int(input("Enter task id\n> "))
            except ValueError:
                print("Enter a proper number")
                continue
            if user_input_id <= 0:
                print("Enter a proper number")
                continue
            task = service.get_task_by_id(user_input_id)
            print(f"{task.id} | {task.name} | {task.description}")


if __name__ == "__main__":
    main()
