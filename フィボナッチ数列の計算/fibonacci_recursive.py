def fibonacci_recursive(end_num: int, a = 0, b = 1, current_num = 0):
    if current_num == end_num:
        print(a)
        return True
    fibonacci_recursive(end_num, b, a + b, current_num + 1)

end_num = int(input("整数を入力してください :"))
fibonacci_recursive(end_num)