import random
import string
import decimal
import sys


def random_word(length):
    return ''.join(random.sample(string.ascii_lowercase, length))


def random_decimal(i, d):
    return decimal.Decimal('%d.%d' % (random.randint(0, i), random.randint(0, d)))


def random_csv(n=5, m=5, headers=False, file=None):
    if file is not None:
        f = open(file, "w+")
    else:
        f = open("random.csv", "w+")

    if headers:
        for j in range(m):
            f.write(random_word(5) + ",")
        f.write("\n")

    for i in range(headers, n):
        for j in range(m):
            f.write(str(random_decimal(0, 99999)) + ",")
        f.write("\n")

    f.close()


if __name__ == "__main__":
    random_csv(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
