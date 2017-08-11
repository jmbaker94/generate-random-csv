import random
import string
import decimal
import sys
import getopt


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


def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'n:m:h:o', ["nrows=", "ncols=", "headers=", "outputfile="])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    nrows = 5
    ncols = 5
    headers = False
    outputfile = None

    for o, a in optlist:
        if o in ["-n", "--nrows"]:
            nrows = int(a)
        elif o in ["-m", "--ncols"]:
            ncols = int(a)
        elif o in ["-h", "--headers"]:
            headers = int(a)
            if headers == 0:
                headers = False
            else:
                headers = True
        elif o in ["-o", "--outputfile"]:
            outputfile = a

    random_csv(nrows, ncols, headers, outputfile)


if __name__ == "__main__":
    main()
