p = input("整数を入力してください: ").strip()

def display_normal_pyramid(n: int):
    for i in range(1, n + 1):        
        print(' '.join(str(j) for j in range(1, i + 1)))


def display_reverse_pyramid(n: int):
    for i in range(n, 0, -1):
        print(' '.join(str(j) for j in range(i, 0, -1)))


def display_equal_interval_pyramid(n: int):
    max_width = len(' '.join(str(i) for i in range(1, n + 1)))
    
    for i in range(1, n +1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line.center(max_width))


if p.isdigit():
    n = int(p)
    display_normal_pyramid(n)
    display_reverse_pyramid(n)
    display_equal_interval_pyramid(n)
else:
    print("整数じゃないです")