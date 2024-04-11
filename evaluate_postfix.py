def evaluate_postfix(expression):
    pilha = []
    contador_temp = 1

    for caractere in expression:
        if caractere.isalpha():
            pilha.append(caractere)
        else:
            operando2 = pilha.pop()
            operando1 = pilha.pop()

            print(f"LD {operando1}")

            if caractere == '+':
                print(f"AD {operando2}")
            elif caractere == '-':
                print(f"SB {operando2}")
            elif caractere == '*':
                print(f"ML {operando2}")
            elif caractere == '/':
                print(f"DV {operando2}")

            var_temporaria = f"TEMP{contador_temp}"
            print(f"ST {var_temporaria}")
            pilha.append(var_temporaria)
            contador_temp += 1

evaluate_postfix("ABC*+DE-/")