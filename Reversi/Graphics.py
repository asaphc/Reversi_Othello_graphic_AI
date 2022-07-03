import Reversi
import random as rand
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import agent

class Graphics:
    def __init__(self, play, ax, game: Reversi.ReversiGame):
        self.game: Reversi.ReversiGame = game
        self.ax = ax
        self.ax.figure.canvas.mpl_connect('button_press_event', self)
        self.draw_board(self.ax, self.game.get_board())
        self.play = play


    def get_cell(self, x , y):
        try:
            col = int(x * self.game.boardSize()) % self.game.boardSize()
            row = self.game.boardSize() - int(y * self.game.boardSize()) % self.game.boardSize() - 1
            return row,col
        except:
            return -1,-1
    def __call__(self,event):
        row, col = self.get_cell(event.xdata,event.ydata)
        if row != -1:
            self.play.update((row,col))

    def update_board(self,game):
        self.game = game
        self.draw_board(self.ax, self.game.get_board())

    def draw_board(self,ax, board):
        ax.clear()
        w = 0 
        b = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i,j]==1:
                    b+=1
                elif board[i,j]==-1:
                    w+=1
        ax.text(0.5/len(board), 1 + 0.5/len(board), 'black: {}'.format(b),horizontalalignment='center',verticalalignment='center', fontsize = 14)
        ax.text(1-0.5/len(board), 1 + 0.5/len(board), 'white: {}'.format(w),horizontalalignment='center',verticalalignment='center', fontsize = 14)
        if self.game.isEnd():
            if w > b:
                ax.text(0.5, 1 + 0.5/len(board), 'white wins!',horizontalalignment='center',verticalalignment='center', fontsize = 14)
            elif w < b:
                ax.text(0.5, 1 + 0.5/len(board), 'black wins!',horizontalalignment='center',verticalalignment='center', fontsize = 14)
            else:
                ax.text(0.5, 1 + 0.5/len(board), 'draw!',horizontalalignment='center',verticalalignment='center', fontsize = 14)

        for i in range(len(board)+1):
            ax.plot([i/len(board),i/len(board)], [0,1], color='black')
            ax.plot([0,1], [i/len(board),i/len(board)], color='black')
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row,col]==1:
                    ax.add_patch(Circle(((col+0.5)/len(board),1-(row+0.5)/len(board)) , 0.2/len(board), color= 'black'))
                if board[row,col]==-1:
                    ax.add_patch(Circle(((col+0.5)/len(board),1-(row+0.5)/len(board)) , 0.2/len(board), facecolor= 'w', edgecolor = 'black'))
        self.ax.figure.canvas.draw()
        self.ax.figure.canvas.flush_events()


