import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    
    count = 1
    
    for line in sys.stdin:
        line = line.strip()
        letra, fecha, num = line.split()
        sys.stdout.write("{}\t{}\n".format(letra, count))
