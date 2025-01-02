import itertools

try:
    word = input("文字列を入力してください: ").strip()
    div = int(input("組み合わせの長さを入力してください: ").strip())

    if div <= 0:
        print("エラー: 組み合わせの長さは1以上である必要があります。")
    elif len(word) < div:
        print("エラー: 組み合わせの長さが文字列の長さを超えています。")
    else:
        combinations = [''.join(comb) for comb in itertools.combinations(word, div)]
        print(f"組み合わせ: {combinations}")

except ValueError:
    print("エラー: 有効な文字列と整数を入力してください。")
