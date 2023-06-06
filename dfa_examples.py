from dfa import DFA


# Example 1: A DFA that emulates an automatic door controller.
name = "Automatic Door"
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


# Example 2: A DFA over the alphabet containing the single symbol '0' that
# accepts those words consisting of an even number of zeros.
name = "Even Number of Zeros"
states = {"even", "odd"}
alphabet = {'0'}
initial_state = "even"
final_states = {"even"}
delta = {("even", '0'): "odd",
         ("odd", '0'): "even"}
even_zeros = DFA(name, states, alphabet, delta, initial_state, final_states)
even_zeros.decide("00")
even_zeros.decide("000")
even_zeros.decide("")
print()


# Example 3: A DFA that recognizes the language over the alphabet {0, 1}
# consisting of all words that either:
#   * End with '1'; or
#   * Contain at least one '1' and consist of an even quantity of '0' after the
#     last '1'.
name = "M1"
states = {'1', '2', '3'}
alphabet = {'0', '1'}
initial_state = '1'
final_states = {'2'}
delta = {('1', '0'): '1',
         ('1', '1'): '2',
         ('2', '0'): '3',
         ('2', '1'): '2',
         ('3', '0'): '2',
         ('3', '1'): '2'}
M1 = DFA(name, states, alphabet, delta, initial_state, final_states)
M1.decide("01010001")
M1.decide("1")
M1.decide("101000100")
M1.decide("1010001000")
print()


# Example 4: A DFA that recognizes the language over the alphabet {0, 1}
# consisting of all words that end with "01".
name = "Ends with 01"
states = {'ε', '0', "01"}
alphabet = {'0', '1'}
initial_state = 'ε'
final_states = {"01"}
delta = {('ε', '0'): '0',
         ('ε', '1'): 'ε',
         ('0', '0'): '0',
         ('0', '1'): "01",
         ("01", '0'): "0",
         ("01", '1'): 'ε'}

ends_with_01 = DFA(name, states, alphabet, delta, initial_state, final_states)
ends_with_01.decide("01")
ends_with_01.decide("10100101")
ends_with_01.decide("1000011")
print()

# Example 5: A DFA that recognizes no words at all and which emulates a
# controller for a six-floor eleverator.
name = "Six-Floor Elevator"
states = {'0', '1', '2', '3', '4', '5'}
alphabet = {'0', '1', '2', '3', '4', '5'}
initial_state = '0'
final_states = {}
delta = dict()
for i in range(6):
    for j in range(6):
        delta[f'{i}', f'{j}'] = f'{j}'


# Example 6: A DFA that recognizes the language over the alphabet {0, 1}
# consisting of all words that end with "001".
name = "Ends with 001"
states = {'ε', '0', "00", "001"}
alphabet = {'0', '1'}
initial_state = 'ε'
final_states = {"001"}
delta = {('ε', '0'): '0',
         ('ε', '1'): 'ε',
         ('0', '0'): '00',
         ('0', '1'): 'ε',
         ("00", '0'): "00",
         ("00", '1'): "001",
         ("001", '0'): 'ε',
         ("001", '1'): 'ε'}
ends_with_001 = DFA(name, states, alphabet, delta, initial_state, final_states)
ends_with_001.decide("1001")
ends_with_001.decide("0011")
ends_with_001.decide("")
ends_with_001.decide("01")
print()


# Example 7: A DFA over the alphabet {a, b} that recognizes strings which start
# and end with the same letter.
name = "First = Last"
states = {'s', 'a', "not a", 'b', "not b"}
alphabet = {'a', 'b'}
initial_state = 's'
final_states = {'a', 'b'}
delta = {('s', 'a'): 'a',
         ('s', 'b'): 'b',
         ('a', 'a'): 'a',
         ('a', 'b'): "not a",
         ('b', 'a'): "not b",
         ('b', 'b'): 'b',
         ("not a", 'a'): 'a',
         ("not a", 'b'): "not a",
         ("not b", 'a'): "not b",
         ("not b", 'b'): 'b'}

first_eq_last = DFA(name, states, alphabet, delta, initial_state, final_states)
first_eq_last.decide("bbaa")
first_eq_last.decide("abababa")
first_eq_last.decide("baba")
first_eq_last.decide("a")
first_eq_last.decide("")
print()


# Example 8: A DFA that does arithmetic modulo n, including a reset button 'r'.
def DFA_modulo(n: int) -> DFA:
    name = f"Arithmetic Modulo {n}"
    states = set(str(k) for k in range(n))
    alphabet = set(range(n)).add('r')
    initial_state = '0'
    final_states = {'0'}
    delta = dict()
    for i in range(n):
        delta[(f'{i}', 'r')] = '0'
        for j in range(n):
            delta[(f'{i}', f'{j}')] = f"{(i + j) % n}"
    return DFA(name, states, alphabet, delta, initial_state, final_states)


DFA_modulo_3 = DFA_modulo(3)
DFA_modulo_3.decide("01r2")
DFA_modulo_3.decide("0111")
DFA_modulo_3.decide("012")
print()


# Example 9: A DFA over the alphabet {0, 1} that recognizes any string that
# contains "001" as a substring.
name = "Contains 001"
states = {'ε', "0", "00", "001"}
alphabet = {'0', '1'}
initial_state = 'ε'
final_states = {"001"}
delta = {('ε', '0'): "0",
         ('ε', '1'): 'ε',
         ("0", '0'): "00",
         ("0", '1'): 'ε',
         ("00", '0'): "00",
         ("00", '1'): "001",
         ("001", '0'): "001",
         ("001", '1'): "001"}
contains_001 = DFA(name, states, alphabet, delta, initial_state, final_states)
contains_001.decide("001")
contains_001.decide("10011")
contains_001.decide("01")
contains_001.decide("1010100")
print()
