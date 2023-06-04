class DPDA:
    """
    A class to represent a deterministic pushdown automaton (DPDA).

    This DPDA is defined by a set of states, an input alphabet, a stack
    alphabet, a transition function, an initial state, and a set of final
    (accepting) states; it also comes with a possibly nonempty stack.

    The transition function should be represented as a dictionary mapping
    tuples of the form (state, input symbol, stack symbol) to tuples of the
    form (next state, symbol to be pushed).  The symbol to be pushed may be
    None, indicating that nothing should be pushed to the stack.

    The DPDA starts in the initial state and processes a list of input symbols.
    The computation proceeds according to the transition function, with the
    DPDA pushing and popping symbols from the stack as specified by the
    transition function. The input is accepted if the DPDA ends in an accepting
    state after processing all input symbols. If at some point the stack
    becomes empty while the input string has not yet been fully consumed, then
    the DPDA rejects.

    Remarks: A state need not be represented by a string, e.g., it may be an
    int. The same goes for the input symbols and the elements of the stack.
    The stack is represented as a list.

    """
    def __init__(self,
                 states: set,
                 input_alphabet: set,
                 stack_alphabet: set,
                 delta: dict,
                 initial_state,
                 final_states: set,
                 stack: list):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.delta = delta
        self.initial_state = initial_state
        self.final_states = final_states
        self.stack = stack

    def run(self, input_list: list) -> bool:
        """ Runs the deterministic PDA on a given list of input symbols
        to determine whether the given word is accepted. """
        current_state = self.initial_state
        for input_symbol in input_list:
            if self.stack:
                top_symbol = self.stack.pop()
                new_state, new_top_symbol = self.delta[(current_state,
                                                        input_symbol,
                                                        top_symbol)]
                current_state = new_state
                if new_top_symbol:
                    self.stack.append(new_top_symbol)
            else:
                return False
        if current_state in self.final_states:
            return True
        else:
            return False

    def decide(self, input_list: list) -> None:
        """ Prints a message stating whether a given input is accepted or
        rejected by the DPDA. """
        input_str = [str(symbol) for symbol in input_list]
        if self.run(input_list):
            print(f"Input \"{''.join(input_str)}\" is recognized by this PDA.")
        else:
            print(f"Input \"{''.join(input_str)}\" is rejected by this PDA.")
