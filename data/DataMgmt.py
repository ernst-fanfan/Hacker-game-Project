# Ernst Fanfan
# Data structures to hold data in the game
# 5/27/2021

from dataclasses import dataclass, field
from Testing.Testing import ob


############################################
# Character classes
# @ob
@dataclass(frozen=True, order=True)
class Person:
    first: str
    last: str
    dob: str


# @ob
@dataclass(frozen=True, order=True)
class CompanyPeople(Person):
    title: str
    company: str


# @ob
@dataclass(frozen=True, order=True)
class GovernmentPeople(Person):
    title: str
    department: str


#######################################################
# Player level and logs
# @ob
@dataclass()
class Player:
    level: int = 1
    log: list = field(default_factory=list)


######################################################
# Systems
# @ob
@dataclass()
class Systems:
    user_id: str
    password: str
    programs: list = field(default_factory=list)
    files: list = field(default_factory=list)


######################################################
# Programs
@dataclass()
class Programs:
    name: str
    files: list = field(default_factory=list)
