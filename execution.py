
 #-*- coding: utf-8 -*-
import pyglet
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction, GAME_WIDTH, GAME_HEIGHT
from soccersimulator import PygletObserver,ConsoleListener,LogListener

from classe_basique import *
from joueur_alea import *

teama=SoccerTeam("teama")
teamb=SoccerTeam("teamb")
teama.add_player(SoccerPlayer("t1j1",FonceurStrategy()))
teamb.add_player(SoccerPlayer("t1j2",ComposeStrategy(GoalStrategy(),Degager())))
teama.add_player(SoccerPlayer("t1j3",ComposeStrategy(Defenseur(),Degager())))
teamb.add_player(SoccerPlayer("t1j4",FonceurStrategy()))
teama.add_player(SoccerPlayer("t2j1",FonceurStrategy()))
teamb.add_player(SoccerPlayer("t2j2",FonceurStrategy()))
teama.add_player(SoccerPlayer("t2j3",ComposeStrategy(Defenseur(),Degager())))
teamb.add_player(SoccerPlayer("t2j4",ComposeStrategy(GoalStrategy(),Degager())))
print teama
print teamb
battle=SoccerBattle(teama,teamb)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
from monequipe import teams
 
