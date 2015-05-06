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
            self.strat = self.adversaire.position
            return self.strat.compute_strategy(state,player,teamid)        
        else:
            return self.defensif.compute_strategy(state, player, teamid)
    def create_strategy(self):
        return Defensif()
        

        