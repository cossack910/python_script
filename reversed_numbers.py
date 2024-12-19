def is_negative(str_number: str) -> bool:
    """前方一致で整数かどうか判定"""
    return str_number.startswith("-")

def reverse_number(str_number: str) -> str:
    negative_flag = is_negative(str_number)
    
    if negative_flag:
        str_number =  str(str_number)[1:]

    if not str_number.isdigit():
        raise ValueError("整数を入力")
    
    reversed_number =  int(str_number[::-1])
    return -reversed_number if negative_flag else reversed_number

if __name__ == "__main__":
    try:
        result = reverse_number(str_number=input("整数を入力してください: ").strip())
        print(result)
    except ValueError as e:
        print(e)