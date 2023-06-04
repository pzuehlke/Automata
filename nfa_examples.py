from nfa import NFA


# Example 1: An NFA that recognizes strings that start with 'a', end with 'b'.
states = {0, 1, 2}
alphabet = {'a', 'b'}
delta = {
    (0, 'a'): {1},     # Transition from q0 to q1 on input 'a'
    (1, 'b'): {2},     # Transition from q1 to q2 on input 'b'
    (2, 'b'): {2}      # Transition from q2 to q2 on input 'b'
}
initial_state = 0
final_states = {2}
nfa = NFA(states, alphabet, delta, initial_state, final_states)
# Testing:
inputs = ['a', 'b', 'b']   # Input string 'abb'
nfa.run(inputs)
inputs = ['a', 'b', 'a']   # Input string 'aba'
nfa.run(inputs)
