#second layer of todo list app, allow to control database

class TaskRepository:
	def __init__(self, connection):
		#establish connection, firstly called inside the main.py and gives as argument connection from database.py
		self.connection = connection

		#connects to cursor object, which allows to control the database through the established connection 
		self.cursor = connection.cursor()

	#table creation inside the database
	def create_table(self):
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS todo_list (
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					name TEXT NOT NULL,
					description TEXT
				);
		""")
		self.connection.commit()

	#adds rows to table
	def insert_entry(self, entry_name, entry_description):
		self.cursor.execute("INSERT INTO todo_list (name, description) VALUES (?, ?);",
												   (entry_name, entry_description))
		self.connection.commit()

	#remove row by id
	def delete_entry(self, entry_id):
		self.cursor.execute("DELETE FROM todo_list WHERE id = ?",
							(entry_id,))
		self.connection.commit()

	#edit row by id, also need to edit descrition 
	def edit_entry(self, entry_id, entry_description):
		self.cursor.execute("UPDATE todo_list SET description = ? WHERE id = ?",
							(entry_description, entry_id))
		self.connection.commit()

	#show all rows
	def get_all_entries(self):
		self.cursor.execute("SELECT * from todo_list")
		return self.cursor.fetchall()

	#show row by id
	def get_entry_by_id(self, entry_id):
		self.cursor.execute("SELECT * FROM todo_list WHERE id = ?",
							(entry_id,))
		return self.cursor.fetchone()
	
