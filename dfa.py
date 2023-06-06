class DFA:
    """
    A class to represent a deterministic finite automaton (DFA).
    Attributes:
        * name: A string providing a name for the DFA.
        * states: A set of all states in the DFA. These states must be strings.
        * alphabet: A set of all input symbols in the DFA. These symbols also
          need to be of type str.
        * delta : A dictionary representing the transition function of the DFA.
        * initial_state: The initial state of the DFA.
        * final_states: A set of all final (accepting) states in the DFA.
    """
    def __init__(self,
                 name: str,
                 states: set[str],
                 alphabet: set[str],
                 delta: dict[tuple[str, str], str],
                 initial_state: str,
                 final_states: set[str]):
        self.name = name  # A name by which the DFA is referred to.
        self.states = states
        self.alphabet = alphabet
        self.delta = delta  # The transition function, represented as a dict.
        self.initial_state = initial_state
        self.final_states = final_states  # The set of accepting states.

    def run(self, input_string: str) -> bool:
        """ Determines whether the DFA accepts a given input string. """
        current_state = self.initial_state
        for symbol in input_string:
            current_state = self.delta[(current_state, symbol)]
        return current_state in self.final_states

    def decide(self, input_string: str) -> None:
        """
        Prints a message stating whether a given input (in the form of a string
        of symbols) is accepted or rejected by the DFA.
        """
        # Nonempty string:
        if input_string and self.run(input_string):
            print(f"Input \"{''.join(input_string)}\" "
                  f"is recognized by DFA {self.name}.")
        elif input_string and not self.run(input_string):
            print(f"Input \"{''.join(input_string)}\" "
                  f"is rejected by DFA {self.name}.")
        # Empty string:
        elif not input_string and self.run(input_string):
            print(f"The empty string ε is recognized by DFA {self.name}.")
        else:
            print(f"The empty string ε is rejected by DFA {self.name}.")
