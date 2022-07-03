import numpy as np

class ReversiGame:
    def __init__(self, board_size:int = 8, copy = None, state = None):
        
        self.end = False

        if copy == None and state==None:
            if board_size % 2 != 0 or board_size <=2:
                raise ValueError('board size must be even and greater then 2')

            
            self.board_size = board_size
            self.board = np.zeros((board_size,board_size))
            self.board[int(self.board_size/2)-1][int(self.board_size/2)-1] = 1
            self.board[int(self.board_size/2)+1-1][int(self.board_size/2)+1-1] = 1
            self.board[int(self.board_size/2)+1-1][int(self.board_size/2)-1] = -1
            self.board[int(self.board_size/2)-1][int(self.board_size/2)+1-1] = -1

            self.turn = 1
        elif state!=None:
            board, turn  = state
            self.board_size = len(board)
            self.turn = turn
            self.board = np.copy(board)

        else:
            self.board_size = copy.board_size
            self.board = np.copy(copy.board)
            self. turn = copy.turn

    def inBoard(self,pos):
        x,y = pos
        if (x>=0 and x<self.board_size) and (y>=0 and y<self.board_size):
            return True
        return False
            
    def is_legal_move(self,move):
        x,y = move
        if not self.inBoard(move):
            raise ValueError('move out of board limits')
        if self.board[move]!=0:
            return False
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        for direc in directions:
            near = (move[0] + direc[0],move[1] + direc[1])
            if self.inBoard(near) and self.board[near]==self.turn*-1:
                near = (near[0]+direc[0],near[1]+direc[1])
                while self.inBoard(near) and self.board[near]==self.turn*-1:
                    near = (near[0]+direc[0],near[1]+direc[1])
                if self.inBoard(near) and self.board[near]==self.turn:
                    return True
        return False
    
    def make_move(self,move):
        if not self.is_legal_move(move):
            return False
        self.board[move] = self.turn
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
        for direc in directions:
            near = (move[0] + direc[0],move[1] + direc[1])
            if self.inBoard(near) and self.board[near]==self.turn*-1:
                near = (near[0]+direc[0],near[1]+direc[1])
                while self.inBoard(near) and self.board[near]==self.turn*-1:
                    near = (near[0]+direc[0],near[1]+direc[1])
                if self.inBoard(near) and self.board[near]==self.turn:
                    near = (near[0]-direc[0],near[1]-direc[1])
                    while near != move:
                        self.board[near] = self.turn
                        near = (near[0]-direc[0],near[1]-direc[1])
        self.turn*=-1
        if len(self.get_legal_moves())==0:
            self.turn*=-1
        return True
    
    def get_legal_moves(self):
        moves = []
        if not self.end:
            for row in range(self.board_size):
                for col in range(self.board_size):
                    if self.is_legal_move((row,col)):
                        moves.append((row,col))
        return moves
    
    def isEnd(self):
        if not self.end:
            if len(self.get_legal_moves())==0:
                self.end = True
                return True
            return False
        return True
    
    def get_board(self):
        return np.copy(self.board)
    
    def boardSize(self):
        return self.board_size

    def get_turn(self):
        return self.turn



        
    
