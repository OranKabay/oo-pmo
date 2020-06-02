from Task import Task

class Action(Task):
    def __init__(self,_title,_description,_start,_end,_owner):
        super().__init__(_title,_description,_start,_end,_owner)
        self.type = 'Action'
