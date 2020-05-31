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
        self.tasks = {}

    def addTask(self,_person,_task):
        _L = []
        if len(self.tasks) > 0:
            _L = self.tasks[_person.name]
        _L.append(_task)
        self.tasks[_person.name] = _L

    def addToTeam(self,_person):
        self.team[_person.name] = _person

    def updateTitle(self, _title):
        self.title = _title

    def updateDescription(self, _description):
        self.description = _description

    def updateStart(self,_start):
        self.start = _start

    def updateEnd(self,_end):
        self.end = _end

    def raiseDependency(self):
        pass

    def reportStatus(self):
        pass