class NFA:
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
        self.alphabet.add("eps")
        self.delta = delta
        self.initial_state = initial_state
        self.final_states = final_states

    def epsilon_flow(self, states):
        """ Returns the set of all possible states obtained by following a
        single epsilon arrow, starting from a given set of states. """
        return set([self.delta[state, "eps"] for state in states
                    if self.delta.get((state, "eps"))])

    def epsilon_closure(self, states):
        """ Given a set 'states', returns its epsilon closure, i.e, the set of
        all states which can be reached from some state in 'states' by
        following zero or more consecutive epsilon arrows. """
        new_states = self.epsilon_flow(states)
        while new_states:
            states.update(new_states)
            new_states = self.epsilon_flow(new_states)
        return states

    def run(self, input_list: list):
        """ Determines if the NFA accepts a given input list of symbols. """
        current_states = {self.initial_state}
        for symbol in input_list:
            new_states = set()
            for current_state in current_states:
                new_states.update(self.delta.get((current_state, symbol),
                                                 set()))
            current_states = self.epsilon_closure(new_states)
        return current_states.intersection(self.final_states)

    def decide(self, input_list: list):
        """
        Prints a message stating whether a given input (in the form of a list
        of symbols) is accepted or rejected by the NFA.
        """
        input_str = [str(symbol) for symbol in input_list]
        if self.run(input_list):
            print(f"Input \"{''.join(input_str)}\" is recognized by this NFA.")
        else:
            print(f"Input \"{''.join(input_str)}\" is rejected by this NFA.")

        return None
