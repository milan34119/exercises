import pytest
from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList

def test_creation():
    #arrange
    fixed_date = date(2005, 8, 18)
    calendar = CalendarStub(fixed_date)
    
    #act
    sut = TaskList(calendar)
    
    #assert
    assert len(sut.task_list) == 0
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks
    
def test_adding_task_with_due_date_in_future():
    #arrange
    fixed_date = date(2005, 8, 18)
    calendar = CalendarStub(fixed_date)
    date_in_future = date(2024, 8, 18)
    task_with_due_date_in_future = Task('Boefje aaien', date_in_future)
    sut = TaskList(calendar)
    
    #act
    sut.add_task(task_with_due_date_in_future)
    
    #assert
    assert 1 == len(sut.task_list)
    assert [task_with_due_date_in_future] == sut.due_tasks

def test_adding_task_with_due_date_in_the_past():
    #Arrange
    past_date = date(2016, 8, 18)
    fixed_date = date(2005, 8, 18)
    calendar = CalendarStub(fixed_date)
    task_with_past_date = Task('Boefje Aaien', past_date)
    sut = TaskList(calendar)
    
    #assert and act
    with pytest.raises(RuntimeError):
        sut.add_task(task_with_past_date)
    assert 0 == len(sut.task_list)
    
def test_task_becomes_finished():
    future_date = date(2024, 8, 18)
    fixed_date = date(2005, 8, 18)
    calendar = CalendarStub(fixed_date)
    task_with_future_date = Task('Boefje Aaien', future_date)
    sut = TaskList(calendar)
    
    #act
    sut.add_task(task_with_future_date)
    
    #assert
    assert len(sut.due_tasks) == 1
    assert len(sut.finished_tasks) == 0
    task_with_future_date.finished = True
    assert len(sut.due_tasks) == 0
    assert len(sut.finished_tasks) == 1
    
