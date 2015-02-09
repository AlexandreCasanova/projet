
 #-*- coding: utf-8 -*-
import pyglet
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction, GAME_WIDTH, GAME_HEIGHT
from soccersimulator import PygletObserver,ConsoleListener,LogListener

from classe_basique import *
from joueur_alea import *

teama=SoccerTeam("teama")
teamb=SoccerTeam("teamb")
teama.add_player(SoccerPlayer("t1j1",AllerVersUnPoint(Vector2D(90,56))))
teamb.add_player(SoccerPlayer("t2j1",Tirer()))
teama.add_player(SoccerPlayer("t1j2",ComposeStrategy(AllerVersUnPoint(Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)),Tirer())))
teamb.add_player(SoccerPlayer("t2j2",GoalStrategy()))
print teama
print teamb
battle=SoccerBattle(teama,teamb)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()
from monequipe import teams

