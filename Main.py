from Project import Project
from Person import Person
from Action import *

def main():
    print("Welcome to OO-PMO App")
    defaultUser = Person('Default', 'Backlog', '30 May 2020')
    newProj = Project('OO training','Initial OO project in python','30 May 2020','30 June 2020',defaultUser)
    teamPM = Person('Sal Kabay', 'Project Manager', '30 May 2020')
    teamArchitect = Person('Oran Kabay', 'System Architect', '30 May 2020')
    newProj.addToTeam(teamArchitect)
    newProj.addToTeam(teamPM)
    t1 = Task('task-1', 'an initial TASK to test the class', '30 May 2020', '06 June 2020',teamPM)
    a1 = Action('action-1', 'an initial ACTION to test the class', '30 May 2020', '06 June 2020',teamPM)
    newProj.tasks._all.updateTitle(a1,'ACTION-1')
    newProj.tasks._all.updateOwner(a1,newProj.defaultUser._all.find(teamArchitect))
    pass

if __name__ == "__main__":
    main()