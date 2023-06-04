class DFA:
    """
    A class to represent a non-deterministic finite automaton (NFA).
    Attributes:
        * states: A set of all states in the NFA.
        * alphabet: A set of all input symbols in the NFA.
        * delta : A dictionary representing the transition function of the NFA.
        * initial_state: The initial state of the NFA.
        * final_states: A set of all final (accepting) states in the NFA.
    """
    def __init__(self,
                 states: set,
                 alphabet: set,
                 delta: dict,
                 initial_state,
                 final_states: set):
        self.states = states
        self.alphabet = alphabet
        self.delta = delta
        self.initial_state = initial_state
        self.final_states = final_states

    def run(self, inputs: list):
        """ Determines if the DFA accepts a given list of input symbols. """
        current_state = self.initial_state
        for symbol in inputs:
            current_state = self.delta[(current_state, symbol)]
        return current_state in self.final_states

    def decide(self, input_list: list):
        """
        Prints a message stating whether a given input (in the form of a list
        of symbols) is accepted or rejected by the DFA.
        """
        input_str = [str(symbol) for symbol in input_list]
        if self.run(input_list):
            print(f"Input \"{''.join(input_str)}\" is recognized by this NFA.")
        else:
            print(f"Input \"{''.join(input_str)}\" is rejected by this NFA.")
