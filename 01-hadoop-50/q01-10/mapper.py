import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    
    for line in sys.stdin:
        
        credit_history = line.split(',')[2]
    
        print(credit_history + '\t' + '1')