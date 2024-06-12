import pytest
from datetime import date, timedelta
from calendars import CalendarStub
from tasks import Task, TaskList

def get_today():
    return date.today()

def get_tomorrow(today):
    return today + timedelta(days=1)

def get_yesterday(today):
    return today - timedelta(days=1)

def get_calendar(today):
    return CalendarStub(today)

def get_sut(calendar):
    return TaskList(calendar)

def create_task(task):
    return Task('Boefje aaien', 'Lalala')

def test_creation(sut):
    # Assert
    assert 0 == len(sut)
    assert [] == sut.due_tasks
    assert [] == sut.overdue_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future(sut, tomorrow):
    # Arrange
    task = Task('description', tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert 1 == len(sut)
    assert [task] == sut.due_tasks


def test_adding_task_with_due_day_in_past(sut, yesterday):
    # Arrange
    task = Task('description', yesterday)

    # Act/Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)
    assert 0 == len(sut)


def test_task_becomes_overdue(sut, calendar, today, tomorrow):
    # Arrange
    next_week = today + timedelta(weeks=1)
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks


def test_task_becomes_finished(sut, tomorrow):
    # Arrange
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
