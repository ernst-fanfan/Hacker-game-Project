from data.DataMgmt import CompanyPeople, GovernmentPeople, Player, Systems
from dataclasses import asdict
import UI
import time

john = CompanyPeople("John", "Helix", "11101970", "CEO", "Voters R Us")
jay = GovernmentPeople("Jay", "Dump", "06071950", "Governor", "State")
player1 = Player()
player_pc = Systems(user_id="admin", password="Password", programs=["mail"], files=["one"])
p = asdict(player_pc)
print(p)

player_pc.vote = 1
p = asdict(player_pc)
cmd = ""
current_ui = "localhost"
cmd = UI.cmd_parser(input(f"{current_ui}>>"))
UI.ui_manager(p, cmd)


