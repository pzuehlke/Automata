from dfa import DFA


# Example 1: A DFA that emulates an automatic door controller.
states = {"closed", "open"}
alphabet = {"front", "rear", "both", "neither"}
initial_state = "closed"
final_states = {}
delta = {("open", "front"): "open",
         ("open", "rear"): "open",
         ("open", "both"): "open",
         ("open", "neither"): "closed",
         ("closed", "front"): "open",
         ("closed", "rear"): "closed",
         ("closed", "both"): "closed",
         ("closed", "neither"): "closed"}


# Example 2: A DFA that recognizes the language over the alphabet {0, 1}
# consisting of all words that end with '1' or which contain at least one '1'
# and which consist of an even number of zeros after the last '1'.
states = {1, 2, 3}
alphabet = {0, 1}
initial_state = 1
final_states = {2}
delta = {(1, 0): 1,
         (1, 1): 2,
         (2, 0): 3,
         (2, 1): 2,
         (3, 0): 2,
         (3, 1): 2}


# Example 3: A DFA that recognizes no words at all and which emulates a
# controller for a six-floor eleverator.
states = {0, 1, 2, 3, 4, 5}
alphabet = {0, 1, 2, 3, 4, 5}
initial_state = 0
final_states = {}
delta = dict()
for i in range(6):
    for j in range(6):
        delta[i, j] = j


# Example 3: A DFA that recognizes the language consisting of an even number of
# zeros (defined over the alphabet which contains the single symbol '0'.
states = {"even", "odd"}
alphabet = {0}
initial_state = "even"
final_states = {"even"}
delta = {("even", 0): "odd",
         ("odd", 0): "even"}

even_zeros = DFA(states, alphabet, delta, initial_state, final_states)


# Example 4: A DFA that recognizes the language over the alphabet {0, 1}
# consisting of all words that end with "01".
states = {"eps", "0", "01"}
alphabet = {0, 1}
initial_state = "eps"
final_states = {"01"}
delta = {("eps", 0): "0",
         ("eps", 1): "eps",
         ("0", 0): "0",
         ("0", 1): "01",
         ("01", 0): "0",
         ("01", 1): "eps"}

ends_with_01 = DFA(states, alphabet, delta, initial_state, final_states)
ends_with_01.run([0, 1])


# Example 5: A DFA that recognizes the language over the alphabet {0, 1}
# consisting of all words that end with "001".
states = {"eps", "0", "00", "001"}
alphabet = {0, 1}
initial_state = "eps"
final_states = {"001"}
delta = {("eps", 0): "0",
         ("eps", 1): "eps",
         ("0", 0): "00",
         ("0", 1): "eps",
         ("00", 0): "00",
         ("00", 1): "001",
         ("001", 0): "eps",
         ("001", 1): "eps"}
ends_with_001 = DFA(states, alphabet, delta, initial_state, final_states)
ends_with_001.run([0, 0, 1])
ends_with_001.run([0, 0, 1, 1])


# Example 6: A DFA over the alphabet {a, b} that recognizes strings which start
# and end with the same letter.
states = {'s', 'a', "nota", 'b', "notb"}
alphabet = {'a', 'b'}
initial_state = 's'
final_states = {'a', 'b'}
delta = {('s', 'a'): 'a',
         ('s', 'b'): 'b',
         ('a', 'a'): 'a',
         ('a', 'b'): "nota",
         ('b', 'a'): 'notb',
         ('b', 'b'): 'b',
         ("nota", 'a'): 'a',
         ("nota", 'b'): "nota",
         ("notb", 'a'): "notb",
         ("notb", 'b'): 'b'}

first_equals_last = DFA(states, alphabet, delta, initial_state, final_states)
first_equals_last.run("bbaa")


# Example 7: A DFA that does arithmetic modulo n, including a reset button.
def DFA_modulo(n: int) -> DFA:
    states = set(range(n))
    alphabet = set(range(n)).add("<reset>")
    initial_state = 0
    final_states = {0}
    delta = dict()
    for i in range(n):
        delta[(i, "<reset>")] = 0
        for j in range(n):
            delta[(i, j)] = (i + j) % n
    return DFA(states, alphabet, delta, initial_state, final_states)


DFA_modulo_3 = DFA_modulo(3)
DFA_modulo_3.run([0, 1, "<reset>", 2])


# Example 8: A DFA over the alphabet {0, 1} that recognizes any string that
# contains "001" as a substring.
states = {"eps", "0", "00", "001"}
alphabet = {0, 1}
initial_state = "eps"
final_states = {"001"}
delta = {("eps", 0): "0",
         ("eps", 1): "eps",
         ("0", 0): "00",
         ("0", 1): "eps",
         ("00", 0): "00",
         ("00", 1): "001",
         ("001", 0): "001",
         ("001", 1): "001"}
contains_001 = DFA(states, alphabet, delta, initial_state, final_states)
contains_001.run([0, 0, 1])
contains_001.run([1, 0, 0, 1, 1])
