import random
import time

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
TARGET_CHAR_COUNT = 500
MIN_WORD_LENGTH = 5
MAX_WORD_LENGTH = 20

def generate_random_word():
    """ランダムな単語を生成する"""
    word_length = random.randint(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
    return ''.join(random.choice(ALPHABET) for _ in range(word_length))

def typing_game():
    word_cnt = 0
    start_time = time.time()
    
    while word_cnt < TARGET_CHAR_COUNT:
        word = generate_random_word()
        print(word)
        if word == input():
            word_cnt += len(word)
        elapsed_time = time.time() - start_time
        print("clear!!!")
        print(f"クリア時間: {elapsed_time:.2f} 秒")
        print(f"クリア文字数: {word_cnt}")

if __name__ == "__main__":
    typing_game()