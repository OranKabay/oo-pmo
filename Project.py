from Task import Task
from Person import Person

class Project:
    nextProjectId = 1
    def __init__(self,_title,_description,_start,_end):
        self.projectId = self.nextProjectId
        Project.nextProjectId += 1
        self.title = _title
        self.description = _description
        self.start = _start
        self.end = _end
        self.team = {}
        self.sprints = {}
        self.releases = {}

    def addToTeam(self,_person):
        self.team[_person.name] = _person
