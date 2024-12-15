
def is_input_blank(inp: str):
    return  inp.strip() != ''

def is_array_length_valid(arr: list):
    return len(arr) > 1


def array_diff_calc(inp: str):
    if is_input_blank(inp):
        arr = [int(i) for i in inp.split(',')]
    else:
        print('error')
        return False
    
    if is_array_length_valid(arr):
        diff = max(arr) - min(arr)
        print(f'最大の差：{diff}')
        return True
    else:
        print('error')
        return False

if __name__ == "__main__":
    inp = input("配列を入力してください：")
    array_diff_calc(inp)