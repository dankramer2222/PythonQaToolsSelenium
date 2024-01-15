from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    email: str = None
    age: int = None
    salary: int = None
    department: str = None
    current_address: str = None
    permanent_address: str = None
