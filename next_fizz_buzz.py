try:
    num = int(input("正の整数を入力してください："))
    div1 = int(input("倍数1を入力してください"))
    div2 = int(input("倍数2を入力してください"))

    if num <= 0 or div1 <= 0 or div2 <= 0:
        raise ValueError("整数を入力")
    
    print_arr = []
    for i in range(1, num + 1):
        if i % div1 == 0 and i % div2 == 0:
            print_arr.append("FizzBuzz")
        elif i % div1 == 0:
            print_arr.append("Fizz")
        elif i % div2 == 0:
            print_arr.append("Buzz")
        else:
            print_arr.append(str(i))
    print(f'リスト形式で出力します.{print_arr}')
except ValueError as e:
    print(e)