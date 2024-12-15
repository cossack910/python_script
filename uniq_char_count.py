from collections import Counter

words = input("文字列を入力してください：").lower()

char_count = Counter(words)

uniq_char = [char for char, count in char_count.items() if count == 1]

print(uniq_char)
print(f'ユニークな文字の数: {len(uniq_char)}')
