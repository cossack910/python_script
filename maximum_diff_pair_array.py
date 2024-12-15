
def input_blank_check(inp: str):
    return  inp.strip() == ''

def array_length_check_one_uquare_or_not(arr: list):
    return len(arr) > 1


def array_diff_calc(inp: str):
    if input_blank_check(inp):
        arr = [int(i) for i in inp.split(',')]
    else:
        print('error')
        return False
    
    if array_length_check_one_uquare_or_not(arr):
        diff = max(arr) - min(arr)
        print(f'最大の差：{diff}')
        return True
    else:
        print('error')
        return False

if __name__ == "__main__":
    inp = input("配列を入力してください：")
    array_diff_calc(inp)