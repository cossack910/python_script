def calc_factorias(n: int, factorias = 1):
    if n == 0:
        print(factorias)
        return True
    factorias *= n
    calc_factorias(n - 1, factorias)

num = int(input("整数を入力してください："))
if num < 0:
    print('負の数には階乗は定義されていません')
else:
    calc_factorias(num)