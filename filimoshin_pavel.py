n= int(input())
if n <= 1000000 or n >= 10000000 :
    print('WRONG')
elif n >= 1000000 and n <= 100000000:
    n= str(n)
    n= n + n[0]
    n= n[:: -1]
    n = n.replace('0','O').replace('1','I').replace('2','Z').replace('3','E').replace('4','!').replace('5','S').replace('6','b').replace('7','J').replace('8','#').replace('9','P')
    print(n)
