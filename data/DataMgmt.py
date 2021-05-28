# Ernst Fanfan
# Data structure to hold data in the game
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


@ob
@dataclass(frozen=True, order=True)
class CompanyPeople(Person):
    title: str
    company: str


@ob
@dataclass(frozen=True, order=True)
class GovernmentPeople(Person):
    title: str
    department: str


#######################################################
# Player level and logs
@ob
@dataclass()
class Player:
    level: int = 1
    log: list = field(default_factory=list)


######################################################
# Systems
@ob
@dataclass()
class Systems:
    localhost: int = 0
    vote: int = 0
    state: int = 0
    mail: int = 0
    files: list = field(default_factory=list)
