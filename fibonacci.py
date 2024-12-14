print('整数を入力してください')
n = int(input())

if n == 0:
    print('出力結果: 0')
elif n == 1:
    print('出力結果: 1')
else:
    fibonacci_numbers = [0, 1]
    for i in range(1, n):
        fibonacci_numbers.append(fibonacci_numbers[i]+fibonacci_numbers[i-1])
    print(f'出力結果: {fibonacci_numbers[n]}')
