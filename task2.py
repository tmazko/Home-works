class Project():
    def __init__(self, name:str, description:str, tasks:list):
        self.name=name
        self.description=description
        self.tasks=tasks
    def add_task(self,title, description, status):
        self.tasks.append(Task(title,description,status))
    def remove_task(self, title):
        for task in self.tasks:
            if task.name==title:
                self.tasks.remove(self.tasks.index(task))

    def get_task_status(self,title):
        for task in self.tasks:
            if task.name==title:
                print(f"Status: {task.status}")
    def update_task_status(self,title, new_status):
        for task in self.tasks:
            if task.name==title:
                task.status=new_status
    def get_tasks_by_status(self, status):
        for task in self.tasks:
            if task.status==status:
                print(f"T{task}")
    def print_tasks(self):
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i]}")

class Task():
    def __init__(self,name:str,description:str,status:str):
        self.name = name
        self.description = description
        self.status=status

    def __str__(self) -> str:
        print(f"Task {self.name}: {self.description}")

t1=Task("Cleaning","Do cleaning","P")
t2=Task("Washing","Wash the dishes","N")
t3=Task("Bed sheets", "Change bed sheets","F")
p1=Project("Happy house","Create a happy house",[t1,t2,t3])

def is_continue():
    answ = ""
    print("Do you want to continue(enter y or n)?")
    while answ.lower() != "y" and answ.lower() != "n":
        answ = input(">> ")
    if answ == "y":
        return True
    else:
        return False
def choose_mode():
    print("Your commands(enter only number): ")
    print("1. add_task")
    print("2. remove_task")
    print("3. get_task_status")
    print("4. update_task_status")
    print("5. get_tasks_by_status")
    print("6. print_tasks")
    answ=""
    while answ!="1" and answ!="2" and answ!="3" and answ!="4" and answ!="5" and answ!="6":
        answ=input(">> ")
        answ=answ.replace(" ", "")
        answ=answ.replace(".","")
    return int(answ)
cars=[]

while(True):
    mode=choose_mode()
    if mode== 1:
        title=input("Enter title: ")
        description=input("Enter description: ")
        status=input("Enter status(only a letter: N-not started, P-in progress, F-finished): ")
        p1.tasks.append(Task(title,description,status.upper()))
    elif mode== 2:
        task_title=input("Enter task title to remove it: ")
        p1.remove_task(task_title)
    elif mode==3:
        task_title = input("Enter task title to remove it: ")
        p1.get_task_status(task_title)
    elif mode==4:
        task_title = input("Enter task title to remove it: ")
        task_status=input("Enter new status(only a letter: N-not started, P-in progress, F-finished): ")
        p1.update_task_status(task_title,task_status)
    elif mode==5:
        task_status=input("Enter status to get your tasks: ")
        p1.get_tasks_by_status(task_status)
    elif mode==6:
        p1.print_tasks()
    if not is_continue():
        break
