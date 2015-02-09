from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from joueur_alea import RandomStrategy, GoalStrategy, FonceurStrategy

from classe_basique import *
from joueur_alea import *


team1=SoccerTeam("Cherry")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))

team2=SoccerTeam("Cramberrie")
team2.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t1j2",ComposeStrategy(GoalStrategy(),Degager())))

team3=SoccerTeam("Lemon")
team3.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team3.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
team3.add_player(SoccerPlayer("t1j3",GoalStrategy()))
team3.add_player(SoccerPlayer("t1j4",Defenseur()))

teams =[team1,team2,team3]
