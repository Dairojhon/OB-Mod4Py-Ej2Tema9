import random
from functools import reduce
def main():

    numeros=[]
    for i in range(random.randint(0,20)):
        numeros.append(random.randint(0,20))

    def impares(a):
        if a % 2 == 1:
            return True
        return False

    def suma(a,b):
        return a+b

    def listImpares(lista):
        numImpares=list(filter(impares,numeros))
        print("Esta es la lista de numeros impares:", numImpares)
        return numImpares


    def listSumada(lista):
        numSumados=reduce(suma,lista)
        return numSumados

    print("Esta es la lista original:",numeros)
    numImpares=listImpares(numeros)
    print("Esta es la suma de los elementos de la lista original", listSumada(numeros))
    print("Esta es la suma de los elementos de la lista de numeros impares", listSumada(numImpares))
if __name__=="__main__":
    main()