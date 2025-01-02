print('数字を入力してくさい：')

input_str = input()
if not input_str.isdigit():
    print('正の整数を入力してください！')
else: 
    numers =  [int(i) for i in input_str]
    print(f'各行の和は {sum(numers)} です')