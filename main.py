#В данном файле описывается основная работа алгоритма
#Необходимо вызвать все файлы
#
import sys
import delel
import mult
import sum
import sub

if(len(sys.argv) == 1):
    print("Введите аргументы")

if(len(sys.argv) == 4):
    arv1 = float(sys.argv[1])
    arv2 = float(sys.argv[3])

    if(sys.argv[2] == "+"):
        print(sum.sum(arv1, arv2))
    if(sys.argv[2] == "-"):
        print(sub.sub(arv1, arv2))
    if(sys.argv[2] == "^"):
        print(mult.mult(arv1, arv2))
    if(sys.argv[2] == "/"):
        print(delel.delel(arv1, arv2))        