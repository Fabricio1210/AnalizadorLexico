def main():
    delimiter = "();"
    numbers = "0123456789"
    hexadecimal = "0123456789abcdf"
    s = input("Ingresa tu cadena: ")
    result = []
    term = ''
    token = ''
    i = 0
    s = s.lower()
    while(1):
        result.append('q0')
        if s[i] in delimiter:
            token = "Delimitador"
            term += s[i]
            result.append('q27')
            i+=1
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
                    break;
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
                    break;
            else:
                result.append('q2')
                token = "Entero"
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
                    break;
            else:
                result.append('q10')
                token = "Entero"
        print("<" + token + " , " + term + " ,", ','.join(result) + ">")
        token = ""
        term = ""
        result = []
        if i >= len(s):
            break; 

if __name__ == "__main__":
    main()