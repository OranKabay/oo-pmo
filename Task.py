class TaskList(list):
    def search(self, name):
        matching_tasks = []
        for task in self:
            if name in task.name:
                matching_tasks.append(task)
                return matching_tasks

    def find(self,target_task):
        for task in self:
            if target_task.taskId == task.taskId:
                return task

    def updateTitle(self,task,title):
        _task = self.find(task)
        _task.title = title
        pass

    def updateOwner(self,task,owner):
        _task = self.find(task)
        _task.owner = owner
        pass

class Task:
    next_task_id = 0
    _all = TaskList()
    def __init__(self,_title,_description,_start,_end,_owner):
        self.taskId = self.next_task_id
        Task.next_task_id += 1
        self.type = 'Task'
        self.title = _title
        self.owner = _owner
        self.description = _description
        self.start = _start
        self.end = _end
        self.comments = []
        Task._all.append(self)
