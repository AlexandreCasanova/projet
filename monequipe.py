from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from joueur_alea import RandomStrategy, GoalStrategy, FonceurStrategy

from classe_basique import *
from joueur_alea import *


team1=SoccerTeam("Forever_alone")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team4=SoccerTeam("Mais_Fonce")
team4.add_player(SoccerPlayer("t1j1",FonceurStrategy()))

team2=SoccerTeam("Messi_dribble_ta_team")
team2.add_player(SoccerPlayer("t1j1",ComposeStrategy(GoalStrategy(),Degager())))
team2.add_player(SoccerPlayer("t1j2",PremSelector()))


team3=SoccerTeam("One_job:Marquer")
team3.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team3.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
team3.add_player(SoccerPlayer("t1j3",GoalStrategy()))
team3.add_player(SoccerPlayer("t1j4",Defenseur()))

teams =[team1,team2,team3,team4]


