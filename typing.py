import random
import time

alphabet = "abcdefghijklmnopqrstuvwxyz"

start = time.time()
cnt = 0
while True:
    word = ''.join([alphabet[random.randint(0, 25)] for n in range(random.randint(5, 20))])
    print(word)
    input_word = input()
    if word == input_word:
        cnt += 1
    if cnt >= 30:
        elapsed_time = time.time() - start
        print("clear!!!")
        print(f"クリア時間: {elapsed_time:.2f} 秒")
        break