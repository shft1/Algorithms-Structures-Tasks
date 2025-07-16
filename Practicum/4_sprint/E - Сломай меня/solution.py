import random
import sys
from string import ascii_lowercase

# Ответ: lyrfod -> tsajigeaz


def generate_random_string():
    n = random.randint(1, 10)
    return "".join([random.choice(ascii_lowercase) for _ in range(n)])


def gorner_polinom_hash(s, a=1000, m=123987123):
    hush = 0
    for si in s:
        hush = (hush * a + ord(si)) % m
    return hush


def main():
    hash_str = {}
    while True:
        s = generate_random_string()
        hash_s = gorner_polinom_hash(s)
        candidate = hash_str.setdefault(hash_s, s)
        if candidate != s:
            output = f"{s}\n{candidate}\n"
            sys.stdout.write(output)
            break


if __name__ == "__main__":
    main()
