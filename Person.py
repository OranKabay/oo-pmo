class Person:
    nextPersonId = 1
    def __init__(self,_name,_title,_joinDate):
        self.personId = self.nextPersonId
        Person.nextPersonId += 1
        self.name = _name
        self.title = _title
        self.joined = _joinDate
        self.tasks = []
        self.issues = []
        self.dependencies = []
        self.statuses = []
        self.comments = []

    def addTask(self,_task):
        self.tasks.append(_task)

    def addComment(self,_comment):
        self.comments.append(_comment)

    def reassignTask(self,_task,_person):
        pass

    def updateName(self,_name):
        self.name = _name

    def updateTitle(self,_title):
        self.title = _title

    def updateJoinedDate(self,_joinDate):
        self.joined = _joinDate

    def raiseIssue(self):
        pass

    def raiseDependency(self):
        pass

    def reportStatus(self):
        pass