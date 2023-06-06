class NFA:
    """
    A class to represent a non-deterministic finite automaton (NFA).
    Attributes:
        * name: A string providing a name for the DFA.
        * states: A set of all states in the NFA. These states must be strings.
        * alphabet: A set of all input symbols in the NFA. These symbols also
          need to be of type str.
        * delta : A dictionary representing the transition function of the NFA.
        * initial_state: The initial state of the NFA.
        * final_states: A set of all final (accepting) states in the NFA.
    Remarks:
        * The transition function associates a (possibly empty) set to pairs
          of the form (state, symbol). If a pair of this form does not appear
          as a key in the dictionary, this is interpreted to mean that there is
          no arrow labeled with this symbol leaving this state.  Equivalently,
          one can assign the empty set to such a pair for the same effect.
        * The empty symbol ε should be represented by the string 'ε'.

    """
    def __init__(self,
                 name: str,
                 states: set[str],
                 alphabet: set[str],
                 delta: dict[tuple[str, str], str],
                 initial_state: str,
                 final_states: set[str]):
        self.name = name  # A name by which the NFA is referred to.
        self.states = states
        self.alphabet = alphabet
        self.alphabet.add('ε')  # Add the empty symbol to the alphabet.
        self.delta = delta  # The transition function, represented as a dict.
        self.initial_state = initial_state
        self.final_states = final_states  # The set of accepting states.

    def epsilon_flow(self, states: set[str]) -> set[str]:
        """ Returns the set of all possible states obtained by following a
        single epsilon arrow, starting from a given set of states. """
        return set([self.delta[state, 'ε'] for state in states
                    if self.delta.get((state, 'ε'))])

    def epsilon_closure(self, states: set[str]) -> set[str]:
        """ Given a set 'states', returns its epsilon closure, i.e, the set of
        all states which can be reached from some state in 'states' by
        following zero or more consecutive epsilon arrows. """
        new_states = self.epsilon_flow(states)
        while new_states:
            states.update(new_states)
            new_states = self.epsilon_flow(new_states)
        return states

    def run(self, input_string: str) -> set[str]:
        """
        Determines if the NFA accepts a given input. Returns the intersection
        of the set of accepting states with the end states in the computation
        tree. Thus the NFA accepts if and only if this set is nonempty.
        """
        current_states = {self.initial_state}
        for symbol in input_string:
            new_states = set()
            for current_state in current_states:
                new_states.update(self.delta.get((current_state, symbol),
                                                 set()))
            current_states = self.epsilon_closure(new_states)
        return current_states.intersection(self.final_states)

    def decide(self, input_string: str) -> None:
        """
        Prints a message stating whether a given input (in the form of a string
        of symbols) is accepted or rejected by the NFA.
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
            print(f"The empty string ε is recognized by NFA {self.name}.")
        else:
            print(f"The empty string ε is rejected by NFA {self.name}.")
