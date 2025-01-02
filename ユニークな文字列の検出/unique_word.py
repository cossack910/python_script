word_list = input("文字列を入力してください（例: abc,hello,world,noon）：").strip().lower().split(",")

unique_words = []
for word in word_list:
    if len(set(word)) == len(word):
        unique_words.append(word)
print(f'ユニーク文字列: {sorted(unique_words)}')