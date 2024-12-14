import random
import time

alphabet = "abcdefghijklmnopqrstuvwxyz"

word_cnt = 0
start_time = time.time()

while True:
    word = ''.join([alphabet[random.randint(0, 25)] for n in range(random.randint(5, 20))])
    print(word)
    if word == input():
        word_cnt += len(word)
    if word_cnt >= 400:
        elapsed_time = time.time() - start_time
        print("clear!!!")
        print(f"クリア時間: {elapsed_time:.2f} 秒")
        print(f"クリア文字数: {word_cnt}")
        break