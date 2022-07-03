import agent
import math
from Reversi import ReversiGame


class AlphaBetaAgent(agent.Agent):
    def __init__(self, player,depth=5):
        self.player = player
        self.depth = depth

    def get_move(self,game):
                return self.alpha_beta(game,self.depth)

    def alpha_beta(self, game, depth):
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

        if self.player==-1:
            best = -math.inf
            best_move = (-1,-1)
            moves = game.get_legal_moves()
            for move in moves:
                new_game = ReversiGame(copy = game)
                new_game.make_move(move)
                if new_game.turn==1:
                    val = min_v(-math.inf,math.inf,new_game,0,depth)
                else:
                    val = max_v(-math.inf,math.inf,new_game,0,depth)
                if val > best:
                    best = val
                    best_move = move
        else:
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

    
