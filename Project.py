from Action import *
from Person import Person

class Project:
    nextProjectId = 1
    def __init__(self,_title,_description,_start,_end,_default_user):
        self.projectId = self.nextProjectId
        Project.nextProjectId += 1
        self.title = _title
        self.description = _description
        self.start = _start
        self.end = _end
        self.sprints = {}
        self.releases = {}
        self.defaultUser = _default_user
        self.team = []
        self.tasks = Task('node', 'top level node', _start, _end,_default_user)
        self.tasks.type = 'node'

    def addToTeam(self,_person: Person):
        self.team.append(_person)


