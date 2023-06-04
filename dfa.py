class DFA:
    """
    A class to represent a non-deterministic finite automaton (DFA).
    Attributes:
        * states: A set of all states in the DFA.
        * alphabet: A set of all input symbols in the DFA.
        * delta : A dictionary representing the transition function of the DFA.
        * initial_state: The initial state of the DFA.
        * final_states: A set of all final (accepting) states in the DFA.
    Remark:
        * A state need not be represented by a string, e.g., it may be an int.
          The same goes for the input symbols.
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

    def run(self, input_list: list) -> bool:
        """ Determines if the DFA accepts a given list of input symbols. """
        current_state = self.initial_state
        for symbol in input_list:
            current_state = self.delta[(current_state, symbol)]
        return current_state in self.final_states

    def decide(self, input_list: list) -> None:
        """
        Prints a message stating whether a given input (in the form of a list
        of symbols) is accepted or rejected by the DFA.
        """
        input_str = [str(symbol) for symbol in input_list]
        if self.run(input_list):
            print(f"Input \"{''.join(input_str)}\" is recognized by this DFA.")
        else:
            print(f"Input \"{''.join(input_str)}\" is rejected by this DFA.")
