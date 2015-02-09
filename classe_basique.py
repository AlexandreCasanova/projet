# -*- coding: utf-8 -*-

import math
import pyglet
import soccersimulator
import numpy as np
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction
from soccersimulator import PygletObserver,ConsoleListener,LogListener, PLAYER_RADIUS, BALL_RADIUS

class AllerVersUnPoint(SoccerStrategy) :
    def __init__(self,direction):
        SoccerStrategy.__init__(self,"se_déplacer")
        self.direction = direction
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = self.direction - player.position
        tir = Vector2D(0,0)
        return SoccerAction(vitesse,tir)
    def copy(self):
        return AllerVersUnPoint(self.direction)
    def create_strategy(self):
        return AllerVersUnPoint(self.direction)



class AllerVersBallon(SoccerStrategy) :
    def __init__(self,direction):
        SoccerStrategy.__init__(self,"se_déplacer")
        self.strat = AllerVersUnPoint(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.direction = state.ball.position
        return self.strat.compute_strategy(state,player,teamid)
    def copy(self):
        return AllerVersBallon(self.direction)
    def create_strategy(self):
        return AllerVersBallon(self.direction)


class Tirer(SoccerStrategy) :
    def __init__(self):
        SoccerStrategy.__init__(self,"tirer")
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = Vector2D(0,0)
        tir = state.get_goal_center(self.team_adverse(teamid)) - player.position
        return SoccerAction(vitesse,tir)
    def copy(self):
        return Tirer()
    def create_strategy(self):
        return Tirer()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1


class Degager(SoccerStrategy) :
    def __init__(self):
        SoccerStrategy.__init__(self,"tirer")
        self.strat = Tirer(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.direction = 
        
        return self.strat.compute_strategy(state,player,teamid)
    def copy(self):
        return Tirer()
    def create_strategy(self):
        return Tirer()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1


class ComposeStrategy(SoccerStrategy):
    def __init__(self,vitesse,tir):
        self.vitesse = vitesse
        self.tir = tir
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        return SoccerAction(self.vitesse.compute_strategy(state,player,teamid).acceleration,self.tir.compute_strategy(state,player,teamid).shoot)    
    def copy(self):
        return ComposeStrategy(self.vitesse.copy(),self.tir.copy())
    def create_strategy(self):
        return ComposeStrategy()
        

