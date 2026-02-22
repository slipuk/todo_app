from dataclasses import dataclass

@dataclass
class Task:
	id: int
	name: str
	description: str

#allows to use service fucntion output more effiecintly
#can access task row with task.name, task.id, which helps to use output whatever smb want