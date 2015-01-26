# -*- coding: utf-8 -*-

import pyglet
import soccersimulator
import numpy as np
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction
from soccersimulator import PygletObserver,ConsoleListener,LogListener


	
	

u = Vector2D(3,4)
v = Vector2D(1,2)
w = Vector2D.create_random()

u+v
u-v
u.norm


acc = Vector2D(1,2)
tir = Vector2D(5,5)

action2 = SoccerAction(acc,tir)

pos = Vector2D.create_random()
shoot = Vector2D.create_random()
action = SoccerAction(pos,shoot)

class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        pos = Vector2D.create_random(-1,1)
        shoot = Vector2D.create_random(-1,1)
        return SoccerAction(pos,shoot)
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()
        

class FonceurStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        pos = state.ball.position - player.position
        shoot = state.get_goal_center(self.team_adverse(teamid)) - player.position
        return SoccerAction(pos,shoot)
    def copy(self):
        return FonceurStrategy()
    def create_strategy(self):
        return FonceurStrategy()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1
            

class GoalStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Goal"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        dif = state.ball.position - player.position
        if dif.norm > 15:
            pos = state.ball.position + state.get_goal_center(teamid) - player.position - player position
        else:
            pos = state.ball.position - player.position
        shoot = state.get_goal_center(self.get_op(teamid)) - player.position
        return SoccerAction(pos,shoot)
    def copy(self):
        return GoalStrategy()
    def create_strategy(self):
        return GoalStrategy()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1
            

teama=SoccerTeam("teama")
teamb=SoccerTeam("teamb")
teama.add_player(SoccerPlayer("t1j1",GoalStrategy()))
teamb.add_player(SoccerPlayer("t2j1",GoalStrategy()))
teama.add_player(SoccerPlayer("t1j2",FonceurStrategy()))
teamb.add_player(SoccerPlayer("t2j2",FonceurStrategy()))
battle=SoccerBattle(teama,teamb)
obs=PygletObserver()
obs.set_soccer_battle(battle)
pyglet.app.run()


