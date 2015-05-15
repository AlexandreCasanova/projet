
 #-*- coding: utf-8 -*-
import pyglet
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction, GAME_WIDTH, GAME_HEIGHT
from soccersimulator import PygletObserver,ConsoleListener,LogListener, PLAYER_RADIUS, BALL_RADIUS, mdpsoccer
import classe_basique

teama=SoccerTeam("teama")
teamb=SoccerTeam("teamb")
teama.add_player(SoccerPlayer("t1j1",ComposeStrategy(GoalStrategy(),Degager())))
teama.add_player(SoccerPlayer("t1j2",PremSelector()))
teamb.add_player(SoccerPlayer("t2j1",FonceurStrategy())
teamb.add_player(SoccerPlayer("t2j2",RandomStrategy()))
print teama
print teamb
battle=SoccerBattle(teama,teamb)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()

 
