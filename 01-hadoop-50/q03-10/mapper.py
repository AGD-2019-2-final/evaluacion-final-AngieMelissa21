import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    
    for line in sys.stdin:
        line = line.strip()
        letra, numero = line.split(',')
        sys.stdout.write("{}\t{}\n".format(numero, letra))