class PersonList(list):
    def search(self, name):
        matching_persons = []
        for person in self:
            if name in person.name:
                matching_persons.append(person)
                return matching_persons

    def find(self,target_person):
        for person in self:
            if target_person.personId == person.personId:
                return person

    def updateTitle(self,person,title):
        _person = self.find(person)
        _person.title = title
        pass

class Person:
    nextPersonId = 1
    _all = PersonList()
    def __init__(self,_name,_title,_joinDate):
        self.personId = self.nextPersonId
        Person.nextPersonId += 1
        self.name = _name
        self.title = _title
        self.joined = _joinDate
        self.dependencies = []
        self.statuses = []
        self.comments = []
        Person._all.append(self)
