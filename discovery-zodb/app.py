import ZODB
from ZODB.FileStorage import FileStorage
import persistent
import transaction
from datetime import datetime
import names


storage = FileStorage("database-employees.fs")
db = ZODB.DB(storage)
connection = db.open()
root = connection.root()


class Employee(persistent.Persistent):
    def __init__(
        self, 
        name: str, 
        date_contract: datetime,
        manager = None
    ):
        self.name = name
        self.manager = manager
        self.date_contract = date_contract

    def __str__(self):
        if self.manager:
            message = f'{self.name} contracted by {self.manager.name} at {self.date_contract}'
        else: 
            message = f'{self.name} contracted at {self.date_contract}'
        return message


if "employees" not in root.keys():
    root["employees"] = {}


employees = root["employees"]


def list_employers():
    for employee in employees.values():
        print(f'{employee}')


def add_employee(employeer: Employee) -> None:
    employees[employee.name] = employeer
    root['employees'] = employees
    transaction.commit()


if __name__ == "__main__":
    linus = Employee(
        name='Linus Torvalds',
        date_contract=datetime.now()
    )
    carlos = Employee(
        name='Carlos Neto',
        manager=linus,
        date_contract=datetime.now()
    )
    employee = Employee(
        name=names.get_full_name(gender="female"),
        manager=carlos,
        date_contract=datetime.now()
    )
    add_employee(employee)
    list_employers()
    connection.close()
