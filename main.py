from source.database import get_connection
from source.repository import TaskRepository
from source.service import TaskService

def main():
	connection = get_connection()
	repository = TaskRepository(connection)
	repository.create_table()
	service = TaskService(repository)

	while True:
		print("todo app")

		print("create task press 1")

		user_input = input(">")
		if user_input.isnumeric() and int(user_input) == 1:
			user_input_name = input("Enter a name\n>")
			user_input_description = input("enter a description (blank for none)\n>")
			service.create_task(user_input_name, user_input_description)
	
		tasks = service.get_all_tasks()
	
		for task in tasks:
			print(f"{task.id} | {task.name} | {task.description}")

if __name__ == "__main__":
	main()
	