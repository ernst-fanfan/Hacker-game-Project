# Ernst Fanfan
# Data structure to hold data for all people in the game
# 5/27/2021
from dataclasses import dataclass, asdict


@dataclass(frozen=True, order=True)
class Person:
    first: str
    last: str
    dob: str


@dataclass(frozen=True, order=True)
class CompanyPeople(Person):
    title: str
    company: str


@dataclass(frozen=True, order=True)
class GovernmentPeople(Person):
    title: str
    department: str
