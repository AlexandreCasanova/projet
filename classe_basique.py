# -*- coding: utf-8 -*-

import random
import math
from math import cos, sin
import pyglet
import soccersimulator
import numpy as np
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction
from soccersimulator import PygletObserver,ConsoleListener,LogListener, PLAYER_RADIUS, BALL_RADIUS, GAME_WIDTH, GAME_HEIGHT




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
    def __init__(self):
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
        return AllerVersBallon()
    def create_strategy(self):
        return AllerVersBallon()


class Tirer(SoccerStrategy) :
    def __init__(self):
        SoccerStrategy.__init__(self,"tirer")
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = Vector2D(0,0)
        tir = Vector2D(0,0)
        if player.position.distance(state.ball.position)<(PLAYER_RADIUS+BALL_RADIUS):
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
        SoccerStrategy.__init__(self,"dégager")  
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    
    def joueurprocheballon (self, state, player, teamid):        
        if (teamid == 1):
            res = [state.ball.position.distance(p.position) for p in state.team1.players if p!= player]
            m=min(res)
            return state.team1.players[res.index(m)]        
        else:
            res = [state.ball.position.distance(p.position) for p in state.team2.players if p!= player]
            m=min(res)
            return state.team2.players[res.index(m)]    
    def compute_strategy(self,state,player,teamid):
        vitesse = Vector2D(0,0)
        tir = Vector2D(0,0)
        joueur_proche = self.joueurprocheballon(state,player,teamid)
        if player.position.distance(state.ball.position)<=(PLAYER_RADIUS+BALL_RADIUS):
            
            tir = joueur_proche.position - player.position
        return SoccerAction(vitesse,tir)
    def copy(self):
        return Degager()
    def create_strategy(self):
        return Degager()
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


class Defenseur (SoccerStrategy):
    def __init__(self):
        SoccerStrategy.__init__(self,"Defenseur")
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy (self, state, player, teamid):
        diff = state.ball.position - state.get_goal_center(teamid)
        if diff.norm > 60 :
            vitesse = state.ball.position + state.get_goal_center(teamid) - player.position - player.position
            tir = Vector2D(0,0)
        else :
            vitesse = state.ball.position - player.position
            tir = Vector2D(0,0)
        
        return SoccerAction(vitesse,tir)
    def copy(self):
        return Defenseur()
    def create_strategy(self):
        return Defenseur()


class Dribble(SoccerStrategy):
    def __init__(self):
        SoccerStrategy.__init__(self,"dribbler")
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        tir = state.get_goal_center(self.team_adverse(teamid)) - player.position
        dri = Vector2D.create_polar(tir.angle + random.random(),1)
        return SoccerAction(Vector2D(0,0), dri)
    def copy(self):
        return Dribble()
    def create_strategy(self):
        return Dribble()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1


def aleballon(self,state,player,teamid):
   return player.position.distance(self.ball.position)<(PLAYER_RADIUS+BALL_RADIUS)
    
    

class Tudors(SoccerStrategy):
    def __init__(self):
        self.name="tudors"
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        diff = state.ball.position - player.position
        tir = Vector2D(0,0)
        vitesse = Vector2D(0,0)
        if diff.norm > 100 :
            vitesse = state.ball.position - player.position
        if player.position.distance(state.ball.position)<(PLAYER_RADIUS+BALL_RADIUS) :    
            tir = state.get_goal_center(self.team_adverse(teamid)) - player.position
        return SoccerAction(vitesse,tir)
    def copy(self):
        return Tudors()
    def create_strategy(self):
        return Tudors()
    def team_adverse(self,teamid):
        if (teamid==1):
            return 2
        else :
            return 1

class SimpleSelector(SoccerStrategy):
    def __init__(self):
        self.name="Selecteur simple"
        self.list_strat=[ComposeStrategy(GoalStrategy(),Degager()),FonceurStrategy,GoalStrategy()]
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def selector(self,state,player,teamid):
        diff = state.ball.position - player.position
        if (diff.norm < 10):
            return 0
        if (aleballon):
            return 1
        return -1
    def compute_strategy(self,state,player,teamid):
        return self.list_strat[self.selector(state,player,teamid)].compute_strategy(state,player,teamid)
    


class PremSelector(SimpleSelector):
    def __init__(self):
       self.list_strat=[ComposeStrategy(GoalStrategy(),Degager()),FonceurStrategy,GoalStrategy()]
    def selector(self,state,player,teamid):
        diff = state.ball.position - player.position
        if (diff.norm < 10):
            return 0
        if (aleballon):
            return 1
        return -1
        

