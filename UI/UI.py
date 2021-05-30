# Ernst Fanfan
# User Interfaces to navigate game
# 5/29/2021
from Testing.Testing import func_tester
from dataclasses import asdict


# @func_tester
def cmd_parser(raw_cmd):
    cmd = ""
    if "open" in raw_cmd:
        try:
            cmd, file = raw_cmd.split()
        except ValueError:
            return "no filename"
        return cmd, file
    return raw_cmd


@func_tester
def system_manger(current_system):
    return asdict(current_system)


@func_tester
def show_files(files):
    return "files"


@func_tester
def mail_ui(programs):
    return "mail system"


@func_tester
def vote_ui(programs):
    return "vote system"


@func_tester
def state_ui(programs):
    return "state system"


def ex_func():
    return "exiting Program"


# @func_tester
def ui_manager(current_system, cmd):
    ui_switcher = {
        "ls": show_files,
        "mail": mail_ui,
        "vote": vote_ui,
        "state": state_ui,
        "exit": ex_func
    }
    func = ui_switcher.get(cmd)
    func(current_system)
