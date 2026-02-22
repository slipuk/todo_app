import sqlite3

class ToDo:
	def __init__(self):
		#establish connection
		self.connection = sqlite3.connect("todo_list.db")

		#create cursor object
		self.cursor = self.connection.cursor()

		#create table with
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS todo_list (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					description TEXT,
					created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
				);
		""")

	#adds row to table
	def add_entry(self, entry_name, entry_description):
		self.cursor.execute("INSERT INTO todo_list (name, description) VALUES (?, ?);",
												   (entry_name, entry_description))
		self.connection.commit()
		print("values inserted")

	#list all 
	def view_entries(self):
		self.cursor.execute("SELECT * FROM todo_list")
		return "\n".join(
			" ".join(map(str, row))
			for row in self.cursor.fetchall()
		)

	def delete_entries(self, id, entry_name):
		self.cursor.execute("")

	def drop_database(self):
		question = True
		while question:
			user_input = input("Do you really want to drop your task database: [yes/no] ")
			if user_input == "yes":
				self.cursor.execute("DROP TABLE todo_list")
				print("table droped successfully")
				question = False
			elif user_input == "no":
				print("canceled")
				question = False
			else:
				print("Enter yes/no answer")

	def close(self):
		self.connection.close()

if __name__ == "__main__":
	todo = ToDo()
	print(todo.view_entries())
	todo.close()



