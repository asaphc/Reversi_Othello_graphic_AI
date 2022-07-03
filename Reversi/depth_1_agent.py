import agent

class Depth1Agent (Agent.Agent):

    def get_move(self,game):
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
    
        


