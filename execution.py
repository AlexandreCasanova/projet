
 #-*- coding: utf-8 -*-
import pyglet
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction, GAME_WIDTH, GAME_HEIGHT
from soccersimulator import PygletObserver,ConsoleListener,LogListener, PLAYER_RADIUS, BALL_RADIUS, mdpsoccer

from classe_basique import *
from joueur_alea import *


teama=SoccerTeam("teama")
teamb=SoccerTeam("teamb")
teama.add_player(SoccerPlayer("t1j1",GoalStrategy()))
teama.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
teamb.add_player(SoccerPlayer("t2j1",ComposeStrategy(GoalStrategy(),Degager())))
teamb.add_player(SoccerPlayer("t2j2",PremSelector()))

print teama
print teamb
battle=SoccerBattle(teama,teamb)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
from monequipe import teams
 
