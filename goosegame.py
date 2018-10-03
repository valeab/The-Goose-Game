# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:04:34 2018

@author: user
"""

import numpy as np
import random

print ('The Goose Game')

t=63 #number of states
tab = np.array(range(t+1))[1:]
print (tab)

def roll (): #this function simulates the throwing of the dice
       r=random.randint(1,6)
       return r

n = 2 #number of players
players=[]
for i in range(n):
    print ('Add player')
    new_player=input ('Player:')
    while new_player in players:
        print ('Already existing player')
        new_player=input ('Player:')
        
    players.append(new_player)
print ('Players: %s'%players)
    
g=np.ones(2) #initial position
while g[0]!=tab[t-1] and g[1]!=tab[t-1]: #the game goes on until one of the two player wins
    for i in range (n):
        print('%s rolls dice' %players[i])
        #use the "roll" function
        d1=roll()
        d2=roll()
        print (d1)
        print (d2)
   
        g[i]=g[i]+(d1+d2) #new position
        print ('%s moves from %i to %i' %(players[i], (g[i]-(d1+d2)), g[i]))
     
        #the Bridge: the player jumps to the space "12"
        if g[i]==6:
            print ('The Bridge: %s jumps to 12' %players[i])
            g[i]=tab[11]
       
        #the Goose: the player moves again by the sum of the two dice rolled before
        while g[i]==5 or g[i]==9 or g[i]==14 or g[i]==18 or g[i]==23 or g[i]==27:
            print ('The Goose: %s moves again!' %players[i])
            g[i]=g[i]+(d1+d2)
            print ('%s moves from %i to %i' %(players[i], (g[i]-(d1+d2)), g[i]))
        
        #winning with the exact dice shooting
        if g[i]>tab[t-1]:
            print ('Out of the range! %s bounces!' %players[i])
            g[i]=g[i]-2*(g[i]-t)
            print ('%s returns to %i' %(players[i],g[i]))
           
        #victory    
        if g[i] == tab[t-1]:
            print ('%s wins!!!' %players[i])
            break
        