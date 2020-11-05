import ZODB
from ZODB import DB
from ZODB.FileStorage import FileStorage
from ZODB.PersistentMapping import PersistentMapping
from persistence import Persisten
import transaction
from datetime import datetime


storage = FileStorage("employees.fs")
db = DB(storage)
connection = db.open()
root = connection.root()


class Employeer(Persistent):
    def __init__(
        self, 
        name: str, 
        date_contract: datetime,
        manager: Employeer = None
    ):
        self.name = name
        self.manager = manager
        self.date_contract = date_contract

    def __str__(self):
        if self.manager:
            message = '{self.name} contracted by {self.manager} at {self.date_contract}'
        else: 
            message = '{self.name} contracted at {self.date_contract}'
        return message


if not root.has_key("employees"):
    root["employees"] = {}


employees = root["employees"]


def list_employers():
    for employee in employees.values():
        print(f'{employee}')


def add_employee(employeer: Employeer) -> None:
    root[employee.name] = employeer
    root['employees'] = employees
    transaction.commit()


if __name__=="__main__":
    list_employers()

    manager = Employeer(name='Linus Torvalds', date_contract=datetime.now())
    employee = Employeer(name='Carlos Neto', manager=manager, date_contract=datetime.now())

    connection.close()
    add_employee(employee)
    list_employers()
