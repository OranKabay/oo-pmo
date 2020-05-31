class Task:
    nextTaskId = 1
    def __init__(self,_title,_description,_start,_end):
        self.taskId = self.nextTaskId
        Task.nextTaskId += 1
        self.type = 'Task'
        self.title = _title
        self.description = _description
        self.start = _start
        self.end = _end
        self.comments = []

    def addComment(self,_comment):
        self.comments.append(_comment)

    def updateTitle(self, _newTitle):
        self.title = _newTitle

    def updateDescription(self, _newDescr):
        self.description = _newDescr

    def updateStart(self,_newStart):
        self.start = _newStart

    def updateEnd(self,_newEnd):
        self.end = _newEnd

    def raiseDependency(self):
        pass

    def reportStatus(self):
        pass