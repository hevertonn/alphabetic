import sys

def scan_automaton():
    print('Digite os estados do autômato separados por vírgula:')

    states_str = sys.stdin.readline()
    states = []
    token = ''

    for i in states_str:
        if i != ',' and i != '\n':
            token += i
        else:
            states.append(token) 
            token = ''

    print('Digite os caracteres do alfabeto separados por vírgula:')

    characteres_str = sys.stdin.readline()
    characteres = []

    for i in characteres_str:
        if i != ',' and i != '\n':
            token += i
        else:
            characteres.append(token) 
            token = ''

    print('Informe as transições correspondentes:')

    automaton = {}

    for i in states:
        automaton[i] = []
        for j in characteres:
            state = input(f"δ({i}, {j}) = ")
            automaton[i].append((j, state))

    print(automaton)
    
scan_automaton()
