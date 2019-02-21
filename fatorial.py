def main():

        num = int(input("diga um numero inteiro: "))
        if num >= 0:
                f = fatorial(num)
                print("O fatorial de (%d) = %d\n"%(num, f))
        else:
             print("invalida")
#-----------------------------------------------------------------------------------------------------------
def fatorial(num):
        fa = 1
        while num > 0:
            fa = fa * num
            n = n - 1
        return fa

main()
