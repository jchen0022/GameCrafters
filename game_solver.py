"""
initial_position = inital state
primitive(pos) = The base win-losses of a game. Should return a boolean
gen_moves(pos) = Generate the possible moves of a game. Should return a list of moves
do_moves(pos) = Run all the moves. Should return a list of next set of states

Fill in functions and initial_position to use
"""

initial_position = 4

def primitive(pos):
    return pos == 0

def gen_moves(pos):
    def sub1(x):
        return x-1
    def sub2(x):
        return x-2
    if pos >= 2:
        return [sub1, sub2]
    else:
        return [sub1];

def do_moves(pos, moves):
    return [move(pos) for move in moves]
                

class Game_State:
    """Each state has its current state and list of next possible states
    Also keeps track of current player
    """
    def __init__(self, state): 
        self.state = state
        self.next_states = []
        self.curr_turn = 1
    
    def genMoves(self):
        return gen_moves(self.state)
    
    def doMoves(self):
        pos_moves = self.genMoves()
        states = do_moves(self.state, pos_moves)
        self.next_states = [Game_State(state) for state in states]
        if self.curr_turn == 1:
            self.curr_turn = 2
        else:
            self.curr_turn = 1

def generate_game_tree(game_pos):
    """Creates a tree from a game state"""
    if primitive(game_pos.state):
        return
    else:
        game_pos.doMoves()
        for states in game_pos.next_states:
            generate_game_tree(states)



def solve(game_state):
    if primitive(game_state.state):
        return game_state.curr_turn
    possibilites = [solve(next_turn) for next_turn in game_state.next_states]
    if game_state.curr_turn in possibilites:
        return game_state.curr_turn
    if game_state.curr_turn == 1:
        return 2
    else:
        return 1

def main():
    game_tree = Game_State(initial_position)
    generate_game_tree(game_tree)
    return solve(game_tree)

print(main())


