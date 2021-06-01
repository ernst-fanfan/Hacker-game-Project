# Ernst Fanfan
# Data structures to hold data in the game
# 5/27/2021

from dataclasses import dataclass, field
from datetime import datetime

from typing import List

from Testing.Testing import ob


#######################################################
# Logs player's progress through the story
# @ob
@dataclass()
class Log:
    date: datetime
    entree: str


#######################################################
# Stores player level and logs
# @ob
@dataclass()
class Player:
    level: int = 1
    logs: list[Log] = field(default_factory=list)


######################################################
# Files
@dataclass()
class File:
    name: str
    content: str


############################################
# Character classes
# @ob
@dataclass(frozen=True, order=True)
class Person:
    first: str
    last: str
    dob: str


######################################################
# emails
@dataclass()
class Email:
    sender: Person
    content: str


######################################################
# Systems
# @ob
@dataclass()
class UserAccount:
    user_id: str
    password: str
    emails: dict[Email] = field(default_factory=dict)
    files: dict[File] = field(default_factory=dict)


############################################
# Character extensions
# @ob
@dataclass(frozen=True, order=True)
class Employee(Person):
    title: str
    department: str
    account: UserAccount


######################################################
# Programs
@dataclass()
class Program:
    name: str
    func: str
    arg: int = 0


######################################################
# Systems
# @ob
@dataclass()
class System:
    users: list[Employee] = field(default_factory=list)
    programs: dict[Program] = field(default_factory=dict)


######################################################
# Organizations
@dataclass()
class Organizations:
    name: str
    employees: list[Employee] = field(default_factory=list)
    systems: list[System] = field(default_factory=list)
