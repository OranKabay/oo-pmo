from Project import Project
from Person import Person
from Action import *

def main():
    print("Welcome to OO-PMO App")
    newProj = Project('OO training','Initial OO project in python','30 May 2020','30 June 2020')
    defaultUser = Person('Default', 'Backlog', '30 May 2020')
    teamPM = Person('Sal Kabay', 'Project Manager', '30 May 2020')
    teamArchitect = Person('Oran Kabay', 'System Architect', '30 May 2020')
    newProj.addToTeam(teamArchitect)
    newProj.addToTeam(teamPM)
    t1 = Task('task-1', 'an initial TASK to test the class', '30 May 2020', '06 June 2020')
    a1 = Action('action-1', 'an initial ACTION to test the class', '30 May 2020', '06 June 2020')
    teamPM.createTask(t1)
    teamPM.createTask(a1)
    a1.updateTitle('ACTION-1')
    a1.updateOwner(teamArchitect)
    pass

if __name__ == "__main__":
    main()