import Reversi
import matplotlib.pyplot as plt
import Graphics


class Play:
    def __init__(self, board_size: int, agent1=None, agent2 = None):
        
        self.board_size = board_size
        self.agent1 = agent1
        self.agent2 = agent2

        if agent1==None or agent2==None:

            fig = plt.figure(figsize = (7.2,7.2))
            ax = fig.add_subplot(111)
            self.game = Reversi.ReversiGame(board_size)

            self.graphics = Graphics.Graphics(self,ax, self.game)

            plt.show()
        
    def update(self, pos):
        if not self.game.isEnd():
            self.game.make_move(pos)
            self.graphics.update_board(self.game)
            turn = self.game.get_turn()
            if not self.game.isEnd() and turn == 1 and self.agent1!=None:
                move = self.agent1.get_move(Reversi.ReversiGame(copy = self.game))
                self.game.make_move(move)
                self.graphics.update_board(self.game)
            if not self.game.isEnd() and turn == -1 and self.agent2!=None:
                move = self.agent2.get_move(Reversi.ReversiGame(copy = self.game))
                self.game.make_move(move)
                self.graphics.update_board(self.game)

          
        
