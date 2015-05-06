# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 18:27:33 2015

@author: 3200982
"""

#encoding=utf8

from soccersimulator import pyglet
from soccersimulator import Vector2D, SoccerBattle, SoccerPlayer, SoccerTeam, SoccerStrategy, SoccerAction, GAME_WIDTH, GAME_HEIGHT, BALL_RADIUS, PLAYER_RADIUS
from soccersimulator import PygletObserver,ConsoleListener,LogListener
import math

class Utilitaire :
        def __init__ (self, state, player, teamid) :
            self.state = state
            self.player = player
            self.teamid = teamid
        def adversaire(self) :
            if(self.teamid == 1) :
                return 2
            else : 
                return 1
        def posBalle(self) :
            return self.state.ball.position
        def vectBalle(self) :
            return self.state.ball.speed
        def posJoueur(self) :
            return self.player.position
        def milieuTH(self) :
            return GAME_HEIGHT/2
        def milieuTV(self) :
             return GAME_WIDTH/2
        def aLaBalle(self) :
            return self.player.position.distance(self.state.ball.position)<=(PLAYER_RADIUS+BALL_RADIUS)
        def versUnPoint(self, direction) :
            return direction - self.player.position
        def versLaBalle(self) :
           return self.state.ball.position-self.player.position
        def distanceBallon(self):
            return (self.player.position-self.state.ball.position).norm
        def distanceMonBut(self):
            return (self.state.get_goal_center(self.teamid)-self.player.position).norm
        def distanceButAdverse(self):
            return (self.state.get_goal_center(3-self.teamid)-self.player.position).norm
        def versLesButsAdverses(self) :
            return self.state.get_goal_center(self.adversaire()) - self.player.position
        def versButsAdversesBallon(self) :
            return self.state.get_goal_center(self.adversaire()) - self.state.ball.position+self.state.ball.speed    
        def distanceBallonMesButs(self) :
             return (self.state.get_goal_center(self.teamid)-self.state.ball.position).norm
        def distanceBallonAdversaire(self) :
            return self.state.ball.position - self.adversaire().position
        def distanceJoueurButAdverse(self) :
            return self.state.get_goal_center(self.adversaire()) - self.player.position
        def distanceBallonButAdverse(self) :
            return (self.state.get_goal_center(3-self.teamid)-self.state.ball.position).norm
        def rienDuTout(self) :
            return SoccerAction(Vector2D(0,0), Vector2D(0,0))
        def bouger(self, acceleration) : 
            return SoccerAction(acceleration, Vector2D(0,0))
        def tirer(self, shoot) :
            return SoccerAction(Vector2D(0,0), shoot)
        def bougertirer(self, acceleration, shoot) :
            return SoccerAction(acceleration, shoot)
        def entreBalleEtBut(self) :
            return self.state.ball.position + self.state.get_goal_center(self.teamid) - self.player.position - self.player.position
        def joueurLePlusProche(self) :
            if (self.teamid == 1) :
                res = [self.state.ball.position.distance(p.position) for p in self.state.team1.players if p!= self.player]
                m = min(res)
                return self.state.team1.players[res.index(m)]
            else :
                res = [self.state.ball.position.distance(p.position) for p in self.state.team2.players if p!= self.player]
                m=min(res)
                return self. state.team2.players[res.index(m)]
        def versJoueurLePlusProche(self) :
            return self.joueurLePlusProche().position - self.player.position
