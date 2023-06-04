# INCOMPLETE/INCORRECT
class PDA:
    def __init__(self,
                 states: set,
                 stack: list,
                 input_alphabet: set,
                 stack_alphabet: set,
                 delta: dict,
                 initial_state,
                 final_states: set):
        self.states = states
        self.input_alphabet = input_alphabet
        self.input_alphabet.add('ε')
        self.stack_alphabet = stack_alphabet
        self.stack_alphabet.add('ε')
        self.delta = delta
        self.initial_state = initial_state
        self.final_states = final_states

    def epsilon_flow(self, states: set) -> set:
        """ Returns the set of all possible states obtained by following a
        single epsilon arrow, starting from a given set of states. """
        return set([self.delta[state, "eps"] for state in states
                    if self.delta.get((state, "eps"))])

    def epsilon_closure(self, states: set) -> set:
        """ Given a set 'states', returns its epsilon closure, i.e, the set of
        all states which can be reached from some state in 'states' by
        following zero or more consecutive epsilon arrows. """
        new_states = self.epsilon_flow(states)
        while new_states:
            states.update(new_states)
            new_states = self.epsilon_flow(new_states)
        return states

    def run(self, input_list: list) -> set:
        """ Determines if the PDA accepts a given input list of symbols. """
        current_configurations = {(self.initial_state, self.stack)}
        for input_symbol in input_list:
            new_configurations = set()
            for current_state, current_stack in current_configurations:
                top_symbol = current_stack[-1] if current_stack else 'ε'
                new_pairs = (self.delta.get((current_state, input_symbol,
                             top_symbol), set()))
                for new_state, new_top_symbol in new_pairs:
                    new_stack = current_stack[:] + [new_top_symbol]
                    new_configurations.update({(new_state, new_stack)})
            current_configurations = self.epsilon_closure(new_configurations)
        current_states = set(config[0] for config in current_configurations)
        return current_states.intersection(self.final_states)

    def decide(self, input_list: list) -> None:
        """
        Prints a message stating whether a given input (in the form of a list
        of symbols) is accepted or rejected by the PDA.
        """
        input_str = [str(symbol) for symbol in input_list]
        if self.run(input_list):
            print(f"Input \"{''.join(input_str)}\" is recognized by this PDA.")
        else:
            print(f"Input \"{''.join(input_str)}\" is rejected by this PDA.")
