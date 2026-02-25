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

        # tasks = service.get_all_tasks()

        # for task in tasks:
        #     print(f"{task.id} | {task.name} | {task.description}")


if __name__ == "__main__":
    main()
