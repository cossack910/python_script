import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

cnt = 0
while True:
    word = ''.join([alphabet[random.randint(0, 25)] for n in range(random.randint(5, 20))])
    print(word)
    input_word = input()
    if word == input_word:
        cnt += 1
    if cnt >= 30:
        print("clear!!!")
        break