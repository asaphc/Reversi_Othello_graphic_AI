import random as rand
import numpy as np
from Reversi import ReversiGame
import math
class Agent:
    def get_move_depth1(self,game):
        moves = game.get_legal_moves()
        best = (-1,-1)
        sbest = 0
        for move in moves:
            temp = ReversiGame(copy = game)
            temp.make_move(move)
            board= temp.get_board()
            w = 0
            b = 0
            for row in range(temp.boardSize()):
                for col in range(temp.boardSize()):
                    if board[row,col]==1:
                        b+=1
                    elif board[row,col]==-1:
                        w+=1
            if best[0]==-1 or w-b > sbest:
                best = move
                sbest = w-b
        return move
    
    def get_move(self,game):
        return self.alpha_beta(game, 4)



    def alpha_beta(self, game, depth):
        corner_b = 10    
        def eval (game):
            board = game.get_board()
            w=0
            b=0
            for row in range(game.boardSize()):
                for col in range(game.boardSize()):
                    if board[row,col]==1:
                        b+=1
                    elif board[row,col]==-1:
                        w+=1
            return w-b

        def max_v(alpha, beta, game, depth, max_depth):
            if depth==max_depth or game.isEnd():
                return eval(game)
            moves = game.get_legal_moves()
            v = -math.inf
            for move in moves:
                new_game = ReversiGame(copy = game)
                new_game.make_move(move)
                if new_game.get_turn()==-1:
                    v = max(max_v(alpha,beta,new_game,depth+1,max_depth),v)
                else:
                    v = max(min_v(alpha,beta,new_game,depth+1,max_depth),v)
                alpha = max(alpha,v)
                if v > beta:
                    return v
            return v
        def min_v(alpha, beta, game, depth, max_depth):
            if depth==max_depth or game.isEnd():
                return eval(game)
            
            corners = [(0,0),(0,game.boardSize()-1),(game.boardSize()-1,0),(game.boardSize()-1,game.boardSize()-1)]
            moves = game.get_legal_moves()
            v = math.inf
            for move in moves:
                new_game = ReversiGame(copy = game)
                new_game.make_move(move)
                if new_game.get_turn==1:
                    v = min(min_v(alpha,beta,new_game,depth+1,max_depth),v)
                    beta = min(v,beta)
                else:
                    v = min(max_v(alpha,beta,new_game,depth+1,max_depth),v)
                    beta = min(v,beta)
                if v < alpha:
                    return v
            return v
        best = math.inf
        best_move = (-1,-1)
        moves = game.get_legal_moves()
        for move in moves:
            new_game = ReversiGame(copy = game)
            new_game.make_move(move)
            if new_game.turn==1:
                val = min_v(-math.inf,math.inf,new_game,0,depth)
            else:
                val = max_v(-math.inf,math.inf,new_game,0,depth)
            if val < best:
                best = val
                best_move = move
        return best_move

        