# -*- coding: utf-8 -*-

import math
import pyglet
import soccersimulator
import numpy as np
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction
from soccersimulator import PygletObserver,ConsoleListener,LogListener, PLAYER_RADIUS, BALL_RADIUS


	
	

u = Vector2D(3,4)
v = Vector2D(1,2)
w = Vector2D.create_random()

u+v
u-v
u.norm


acc = Vector2D(1,2)
tir = Vector2D(5,5)

action2 = SoccerAction(acc,tir)

vitesse = Vector2D.create_random()
tir = Vector2D.create_random()
action = SoccerAction(vitesse,tir)

class RandomStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Random"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = Vector2D.create_random(-1,1)
        tir = Vector2D.create_random(-1,1)
        return SoccerAction(vitesse,tir)
    def copy(self):
        return RandomStrategy()
    def create_strategy(self):
        return RandomStrategy()
        

class FonceurStrategy(SoccerStrategy):
    def __init__(self):
        self.name="Fonceur"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = state.ball.position - player.position
        tir = state.get_goal_center(self.team_adverse(teamid)) - player.position
        return SoccerAction(vitesse,tir)
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
        diff = state.ball.position - player.position
        tir = Vector2D(0,0)
        if diff.norm > 5 :
            vitesse = state.ball.position + state.get_goal_center(teamid) - player.position - player.position
        else :
            vitesse = state.ball.position - player.position
        if player.position.distance(state.ball.position)<(PLAYER_RADIUS+BALL_RADIUS) :    
            tir = state.get_goal_center(self.team_adverse(teamid)) - player.position
        return SoccerAction(vitesse,tir)
    def copy(self):
        return GoalStrategy()
    def create_strategy(self):
        return GoalStrategy()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1





    