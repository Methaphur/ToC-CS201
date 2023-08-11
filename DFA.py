class State:
    def __init__(self, name, is_accepting = False):
        self.name = name
        self.is_accepting = is_accepting
        self.transitions = {}   # All function mappings from current state
    
    def add_transition(self, input_symbol, next_state):
        self.transitions[input_symbol] = next_state
    
    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol ,None)


class DFA:
    def __init__(self, states, alphabet, start_state, final_states):
        self.alphabet = alphabet
        self.states = states
        self.start_state = start_state
        self.final_states = final_states 
    
    def validate(self, input_string):
        current_state = self.states[self.start_state]

        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
        
            next_state = current_state.get_next_state(symbol)
            if next_state is None:
                return False
        
            current_state = self.states[next_state]
        return current_state.name in self.final_states
    

# A simple DFA that accepts a string with even number of 1s  

q0 = State("q0")
q1 = State("q1")

q0.add_transition('1', 'q1')
q0.add_transition('0', 'q0')
q1.add_transition('1', 'q0')
q1.add_transition('0', 'q1')

alphabet = ['0' , '1']
states = {'q0' : q0 , 'q1' : q1}
start_state = 'q0'
final_states = {'q0'}

dfa = DFA(states, alphabet, start_state, final_states)
input_string = "110010110111"
result = dfa.validate(input_string)
print(result)
