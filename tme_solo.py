# -*- coding: utf-8 -*-

from ToolBox import *
from classe_basique import *
import random
import math
from math import cos, sin
import pyglet
import soccersimulator
import numpy as np
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction, SoccerState
from soccersimulator import PygletObserver,ConsoleListener,LogListener, PLAYER_RADIUS, BALL_RADIUS, GAME_WIDTH, GAME_HEIGHT


#Question 1
class Defensif(SoccerStrategy):
    def __init__(self,player):
        SoccerStrategy.__init__(self,"Défensif")
        self.adversaire = player
        self.strat = AllerVersUnPoint(Vector2D())
        self.defensif = AllerVersBallon()
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Utilitaire(state, teamid, player)
        d = self.adversaire.position - state.ball.position
        if(d <(PLAYER_RADIUS+BALL_RADIUS)):
            self.strat.direction = self.adversaire.position
            return self.strat.compute_strategy(state,player,teamid)        
        else:
            return self.defensif.compute_strategy(state, player, teamid)
    def create_strategy(self):
        return Defensif()

class AllerLentementVersUnPoint(SoccerStrategy):
    def __init__(self, direction):
        self.direction = direction      
        pass
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        vitesse = self.distance - player.position
        vitesse.product(0.1)
        return SoccerAction(vitesse, Vector2D(0,0))
    def create_strategy(self):
        return AllerLentementVersUnPoint()
        

class AllerLentementVersBallon(SoccerStrategy):
    def __init__(self):
        self.strat= AllerLentementVersUnPoint(Vector2D())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        self.strat.direction= state.ball.position + state.ball.speed
        return self.strat.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return AllerLentementVersBallon()

class Leggo(SoccerStrategy):
    def __init__(self):
        self.fonceur = CompoStrat(AllerVersBallon(), Tirer())
        self.fonceurlent = CompoStrat(AllerLentementVersBallon(), Tirer())
    def start_battle(self,state):
        pass
    def finish_battle(self,won):
        pass
    def compute_strategy(self,state,player,teamid):
        test = Utilitaire(state, teamid, player)
        if(test.ballmud()):
            return self.fonceur.compute_strategy(state,player,teamid)
        if(test.ballice()):
            return self.fonceurlent.compute_strategy(state,player,teamid)
        return self.fonceur.compute_strategy(state,player,teamid)
    def create_strategy(self):
        return Leggo()
        

        