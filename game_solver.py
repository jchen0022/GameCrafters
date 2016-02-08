"""
initial_position = inital state
primitive(pos) = The base win-losses of a game. Should return a boolean
gen_moves(pos) = Generate the possible moves of a game. Should return a list of moves
do_moves(pos) = Run all the moves. Should return a list of next set of states

Fill in functions and initial_position to use
"""

initial_position = 0

def primitive(pos):
    return

def gen_moves(pos):
    return

def do_moves(pos, move):
    return

class Game_State:
    """Each state has its current state and list of next possible states
    Also keeps track of current player
    """
    def __init__(self, state): 
        self.state = state
        self.next_states = []
        self.curr_turn = "P1"
    
    def genMoves(self):
        return gen_moves(self.state)
    
    def doMoves(self):
        pos_moves = genMoves()
        states = do_moves(pos_moves)
        self.next_states = [Game_State(state) for state in states]
        if self.curr_turn == "P1":
            self.currturn = "P2"
        else:
            self.curr_turn = "P1"

def generate_game_tree(game_pos):
    """Creates a tree from a game state"""
    if primitive(game_pos):
        return
    else:
        game_pos.doMoves()
        for states in game_pos.next_states:
            generate_tree(states)



def solve():
    game_tree = generate_game_tree(initial_position)
