import Play
import Alpha_Beta_Agent

#####
# running a game, the first parameter is the board size.
# two add AI add
# agent1 = Agent... for an AI for player 1
# and 
# agent2 = ...
# for an AI for player 2
# you can also have an AI for both
# example:
# Play.Play(8,  agent2 = Alpha_Beta_Agent.AlphaBetaAgent(-1,2))

Play.Play(8,  agent2 = Alpha_Beta_Agent.AlphaBetaAgent(-1,2))



