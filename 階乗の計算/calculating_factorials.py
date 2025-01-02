print('整数を入力してください：')
num = int(input())

if num < 0:
    print('負の数には階乗は定義されていません')
elif num == 0:
    print('0! = 1')
else:
    factorias = 1
    for i in range(1, num+1):
        factorias *= i
    print(factorias)