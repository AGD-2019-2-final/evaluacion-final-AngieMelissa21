import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
if __name__ == '__main__':

    key = None
    total = 0

    for line in sys.stdin:

        letra, num = line.split("\t")
        num = int(num)

        if letra == key:

            total += num
            
        else:

            if key is not None:
                
                sys.stdout.write("{},{}\n".format(key, total))

            key = letra
            total = num

    sys.stdout.write("{},{}\n".format(letra, total))
