class Task:
    nextTaskId = 1
    tasks = []
    def __init__(self,_title,_description,_start,_end):
        self.taskId = self.nextTaskId
        Task.nextTaskId += 1
        self.type = 'Task'
        self.title = _title
        self.owner = ''
        self.description = _description
        self.start = _start
        self.end = _end
        self.comments = []

    def updateTitle(self, _title):
        for x in Task.tasks:
            if x.taskId == self.taskId:
                x.title = _title
                break
        pass

    def updateOwner(self,_owner):
        for x in Task.tasks:
            if x.taskId == self.taskId:
                x.owner = _owner
                break
        pass
