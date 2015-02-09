from soccersimulator import SoccerBattle, SoccerPlayer, SoccerTeam
from soccersimulator import PygletObserver,ConsoleListener,LogListener
from soccersimulator import pyglet
from joueur_alea import RandomStrategy, GoalStrategy, FonceurStrategy

team1=SoccerTeam("team1")
team1.add_player(SoccerPlayer("t1j1",FonceurStrategy()))

team2=SoccerTeam("team2")
team2.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team2.add_player(SoccerPlayer("t1j2",GoalStrategy()))

team3=SoccerTeam("team3")
team3.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
team3.add_player(SoccerPlayer("t1j2",GoalStrategy()))
team3.add_player(SoccerPlayer("t1j3",GoalStrategy()))
team3.add_player(SoccerPlayer("t1j4",RandomStrategy()))

teams =[team1,team2,team3]
