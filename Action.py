from Task import Task

class Action(Task):
    def __init__(self,_title,_description,_start,_end):
        super().__init__(_title,_description,_start,_end)
        self.type = 'Action'
