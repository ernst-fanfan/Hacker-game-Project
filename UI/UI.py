# Ernst Fanfan
# User Interfaces to navigate game
# 5/29/2021
from Testing.Testing import func_tester
from dataclasses import asdict


######################################################
# @func_tester
# keyword argument
def cmd_parser(input_str):
    try:
        cmd, arg = input_str.split()
        return cmd, arg
    except ValueError:
        cmd = input_str
        arg = ""
        return cmd, arg


# cmd checker
def is_program_in_system(cmd, programs={}):
    return programs.get(cmd, "error")


# arg checker
def is_arg_in_system(arg, dct):
    return dct.get(arg, "Error")


# cmd handler
def cmd_handler(input_str, system, user_account=None):
    cmd, arg = cmd_parser(input_str)
    program = is_program_in_system(cmd, system.programs)
    if program.arg == 0:
        return program.func
    if program.name == "mail":
        emails = user_account.emails
        arg = is_arg_in_system(arg, emails)
        return program.func(arg)
    if program.name == "ls":
        files = user_account.files
        arg = is_arg_in_system(arg, files)
        return program.func(arg)
