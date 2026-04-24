import sys


class Automaton:
    def __init__(self, num_states, alphabet):
        self.__states = {}
        self.__alphabet = []
        self.__start = "q1"
        self.__end = []

        for i in range(num_states):
            self.__states[f"q{i + 1}"] = []

        if type(alphabet) is list:
            self.__alphabet = alphabet
        elif type(alphabet) is str:
            token = ""

            for c in alphabet:
                if c != "," and c != "\n":
                    token += c
                else:
                    self.__alphabet.append(token)
                    token = ""

    def set_transition(self, origin, target, character):
        if origin not in self.__states.keys() or target not in self.__states.keys():
            print(f"Estados {origin} e {target} não pertencem ao autômato")
            return

        if character not in self.__alphabet:
            print(f"Caractere {character} não pertence ao alfabeto do autômato")
            return

        self.__states[origin].append((character, target))

    def set_end(self, end):
        if type(end) is list:
            self.__end = end
        elif type(end) is str:
            token = ""

            for c in end:
                if c != "," and c != "\n":
                    token += c
                elif token in self.__states.keys():
                    self.__end.append(token)
                    token = ""
                else:
                    print(f"Estado {token} não pertence ao autômato")
                    token = ""

    def get_states(self):
        return self.__states.keys()

    def get_states_num(self):
        return len(self.__states.keys())

    def get_alphabet(self):
        return self.__alphabet

    def get_transitions(self, origin, target):
        if origin not in self.__states.keys() or target not in self.__states.keys():
            print(f"Estados {origin} e {target} não pertencem ao autômato")
            return

        transitions = []

        for t in self.__states[origin]:
            if t[1] == target:
                transitions.append(t[0])

        return transitions

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def string(self):
        automaton_str = "Estado inicial "

        for state, transactions in self.__states.items():
            automaton_str += state + ":\n    "

            for t in transactions:
                automaton_str += f"δ({state}, {t[0]}) = {t[1]}  "

            automaton_str += "\n"

        return automaton_str


def scan_automaton():
    num_states = int(input("Digite o número de estados do autômato: "))
    print()

    print(
        "Digite os caracteres do alfabeto separados por vírgula.\n    Caracteres: ",
        end="",
    )
    automaton = Automaton(num_states, sys.stdin.readline())
    print()

    print("Defina as transições correspondentes.")

    for state in automaton.get_states():
        for charactere in automaton.get_alphabet():
            automaton.set_transition(
                state, input(f"    δ({state}, {charactere}) = "), charactere
            )
    print()

    print("Autômato resultante:\n")
    print(automaton.string())

    print(
        f"Defina os estados finais separados por virgula entre os seguintes.\n    Estados: {', '.join(automaton.get_states())}\n    Estados finais: ",
        end="",
    )

    automaton.set_end(sys.stdin.readline())
    print()

    return automaton


def parse_automaton_to_regex(automaton: Automaton, k, i, j):
    if k == 0:
        if i == j:
            return (
                f"(λ+{'+'.join(automaton.get_transitions('q' + str(i), 'q' + str(j)))})"
            )
        else:
            return (
                f"({'+'.join(automaton.get_transitions('q' + str(i), 'q' + str(j)))})"
            )
    else:
        return f"({parse_automaton_to_regex(automaton, k - 1, i, k)}({parse_automaton_to_regex(automaton, k - 1, k, k)})*{parse_automaton_to_regex(automaton, k - 1, k, j)})+{parse_automaton_to_regex(automaton, k - 1, i, j)}"


automaton = scan_automaton()
expression = []

for e in automaton.get_end():
    expression.append(
        parse_automaton_to_regex(
            automaton,
            automaton.get_states_num(),
            int(automaton.get_start().replace("q", "")),
            int(e.replace("q", "")),
        )
    )

expression = "+".join(expression)

print(f"Expressão resultante:\n    {expression}")
