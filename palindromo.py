def palindromo(string):
    palavra = string.lower().replace(" ", "")
    
    stack = []
    
    for letra in palavra:
        stack.append(letra)
    
    palavra_invertida = ""
    
    while stack:
        palavra_invertida += stack.pop()
    
    return palavra == palavra_invertida

print(palindromo("augusto"))
print(palindromo("ana"))