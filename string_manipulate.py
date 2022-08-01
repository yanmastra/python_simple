import re


def main():
    var = str(input("Input word or sentence: "))
    res = parse_to_camel_case(var)
    print(res)


def parse_to_camel_case(var):
    var = var.replace('-', ' ')
    var = var.replace('_', ' ')
    vars = re.split(' ', var)
    i = 0
    res = ''
    for s in vars:
        s = s.lower()
        if i > 0:
            s = s.title()
        i += 1
        res = res + s
    return res


if __name__ == '__main__':
    continue_ = 1
    while continue_ == 1:
        main()
        continue_ = int(input("Repeat ? 1/0:"))
