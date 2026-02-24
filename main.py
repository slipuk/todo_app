from source.database import get_connection
from source.repository import TaskRepository
from source.service import TaskService

def main():
	connection = get_connection()
	repository = TaskRepository(connection)
	repository.create_table()

	service = TaskService(repository)

	# service.create_task("Hooking", "for bed")
	# service.delete_task(1)
	# service.edit_task(1, "pasta")
	
	# print(service.find_task(1))

	# task = service.get_task(1)

	# print(f"{task.id} | {task.name} | {task.description}")
	
	tasks = service.get_all_tasks()
	
	for task in tasks:
		print(f"{task.id} | {task.name} | {task.description}")

if __name__ == "__main__":
	main()
	