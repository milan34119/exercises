from datetime import date

class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.__finished = False
        
    @property
    def description(self):
        return self.__description
    
    @property
    def due_date(self):
        return self.__due_date
    
    @property
    def finished(self):
        return self.__finished
    
    @finished.setter
    def finished(self, value):
        if value is None:
            raise ValueError('cant be null')
        else:
            self.__finished = value
            
class TaskList:
    def __init__(self):
        self.__task_list = []
            
    @property
    def task_list(self):
        return self.__task_list

    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError('Must be of type task')
        elif task.due_date <= date.today():
            raise RuntimeError('Due date must be in the future')
        else:
            self.__task_list.append(task)
            
    def finished_tasks(self):
        finished = []
        for task in self.__task_list:
            if task.finished == True:
                finished.append(task)
        return finished
    
    def due_tasks(self):
        unfinished = []
        for task in self.__task_list:
            if task.finished == False:
                unfinished.append(task)
        return unfinished
    
    def overdue_tasks(self):
        overdue = []
        for task in self.__task_list:
            if task.due_date < date.today():
                overdue.append(task)
        return overdue
    
    
task = Task('Boefje aaien', '2024-01-01')
tasklist = TaskList()
tasklist.add_task(task)
        
            
            
    
            