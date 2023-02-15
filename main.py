#В данном файле описывается основная работа алгоритма
#Необходимо вызвать все файлы
#
import sys

if(len(sys.argv) == 1):
    print("Введите аргументы")

if(len(sys.argv) == 4):
    arv1 = float(sys.argv[1])
    arv2 = float(sys.argv[3])

    if(sys.argv[2] == "+"):
        print(arv1 + arv2)
    if(sys.argv[2] == "-"):
        print(arv1 - arv2)
    if(sys.argv[2] == "^"):
        print(arv1 * arv2)
    if(sys.argv[2] == "/"):
        print(arv1 / arv2)        