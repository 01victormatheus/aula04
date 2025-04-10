fora=0
interv=0
for x in range(10):
    num=int(input("digite um numero"))
    if num>10 and num<20:
        interv=interv+1
    else:
     fora=fora+1

print(f"tem {interv} dentro do intervalo e ,{fora} que não estão")
