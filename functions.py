def format_name(string1, string2):
    x = string1.strip() + " " + string2.strip()
    return x.title()


def doubler(parameter):
    return str(parameter) * 2


def base_conversion():
    b = int(input(" Insert Base from 2-9 to convert: "))
    x = (b ** 4) - 1
    c = int(input(" Input number = or < " + str(x) + ": "))
    r = c % b
    q = c // b
    r2 = q % b
    q2 = q // b
    r3 = q2 % b
    q3 = q2 // b
    r4 = q3 % b
    string = str(r4) + str(r3) + str(r2) + str(r)
    return print(int(string))


base_conversion()
