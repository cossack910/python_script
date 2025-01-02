def fibonacci_recursive(end_num: int, numbers: list = [0, 1], current_num: int = 0):
    if current_num == end_num:
        print(numbers[end_num])
        return False
    numbers.append(numbers[current_num]+numbers[current_num + 1])
    fibonacci_recursive(end_num, numbers, current_num + 1)

end_num = int(input("整数を入力してください :"))
fibonacci_recursive(end_num)