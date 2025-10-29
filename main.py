def main():
    delimiter = "();"
    numbers = "0123456789"
    hexadecimal = "0123456789ABCDEF"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = input("Ingresa tu cadena: ")
    result = []
    term = ''
    token = ''
    i = 0
    
    while (1):
        
        result.append('q0')
        
        # Espacio(s)
        if s[i].isspace():
            term += s[i]
            result.append("q19")
            result.append("q16")
            token = "Espacio"
            i += 1
        
        # Delimitador
        elif s[i] in delimiter:
            token = "Delimitador"
            term += s[i]
            result.append('q27')
            i+=1
        
        # Hexadecimal/Flotante/Entero
        elif s[i] == '0':
            term += s[i]
            result.append('q1')
            i+=1
            if i < len(s) and s[i] == "x":
                term += s[i]
                result.append('q3')
                i+=1
                if i < len(s) and s[i] in hexadecimal:
                    while i < len(s) and s[i] in hexadecimal:
                        result.append('q4')
                        term += s[i]
                        i += 1
                    result.append('q5')
                    token = "Hexadecimal"
                else:
                    print("Error numero hexadecimal incompleto, formato no valido")
                    break
            
            elif i < len(s) and s[i] == ".":
                term += s[i]
                result.append('q7')
                i+=1
                if i < len(s) and s[i] in numbers:
                    while i < len(s) and s[i] in numbers:
                        result.append('q8')
                        term += s[i]
                        i += 1
                    result.append('q9')
                    token = "Flotante"
                else:
                    print("Error numero flotante incompleto, formato no valido")
                    break
            else:
                result.append('q2')
                token = "Entero"
        
        # Entero/Flotante
        elif s[i] in numbers:
            while i < len(s) and s[i] in numbers:
                result.append('q6')
                term += s[i]
                i += 1
            if i < len(s) and s[i] == ".":
                term += s[i]
                result.append('q7')
                i+=1
                if i < len(s) and s[i] in numbers:
                    while i < len(s) and s[i] in numbers:
                        result.append('q8')
                        term += s[i]
                        i += 1
                    result.append('q9')
                    token = "Flotante"
                else:
                    print("Error numero flotante incompleto, formato no valido")
                    break
            else:
                result.append('q10')
                token = "Entero"        

        # Identificadores / Palabras reservadas
        elif s[i] in letters or s[i] in "$_":
            # "if"
            if s[i:i+2] == "if":
                term += "if"
                result.extend(["q11", "q12", "q13"])
                i += 2
                token = "Palabra_reservada"
            else:
                # Identificadores
                while i < len(s) and (s[i] in letters or s[i] in numbers or s[i] in "$_"):
                    term += s[i]
                    result.append("q14")
                    i += 1
                result.append("q15")
                token = "Identificador"
        

        # Operadores(+, ++)
        elif s[i] == "+":
            term += s[i]
            result.append("q17")
            i += 1
            if i < len(s) and s[i] == "+":
                term += s[i]
                result.append("q18")
                token = "incremento"
                i += 1
            else:
                result.append("q20")
                token = "suma"


        # Operadores (=, ==)
        elif s[i] == "=":
            term += s[i]
            result.append("q22")
            i += 1
            if i < len(s) and s[i] == "=":
                term += s[i]
                result.append("q26")
                token = "Igual"
                i += 1
                if s[i] == "=":
                    print("Error [===] no valido")
                    break
            else:
                result.append("q25")
                token = "Asignación"
        else:
            print(f"Error: símbolo no reconocido '{s[i]}' en q0")
            break        

        # Impresion final            
        print("<" + token + ", " + term + ", " + ','.join(result) + ">")
        token = ""
        term = ""
        result = []
        if i >= len(s):
            break


if __name__ == "__main__":
    main()