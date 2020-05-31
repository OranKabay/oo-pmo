from Task import *

class Person:
    nextPersonId = 1
    def __init__(self,_name,_title,_joinDate):
        self.personId = self.nextPersonId
        Person.nextPersonId += 1
        self.name = _name
        self.title = _title
        self.joined = _joinDate
        self.dependencies = []
        self.statuses = []
        self.comments = []

    def createTask(self,_task: Task):
        _task.owner = self
        Project.tasks.append(_task)