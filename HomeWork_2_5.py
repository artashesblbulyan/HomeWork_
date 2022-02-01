import os

cwd = os.getcwd()
phil_pat = os.path.join(cwd, 'test.txt')


def count_digits():
    """
    count the amount of digits in every line
    """
    with open(phil_pat, "r") as file:
        row = 0
        for j in range(4):
            row += 1
            num = 0
            file_line_2 = file.readline()
            for i in file_line_2:
                if i.isdigit():
                    num += 1
                else:
                    continue
            print(f"row {row}:amount of digits {num}")


count_digits()


def amount_sum_digit():

    with open(phil_pat, "r") as file_2:
        sum = 0
        file_content = file_2.read()
        for i in file_content:
            if i.isdigit():
                sum += int(i)
            else:
                continue
        return sum


print(amount_sum_digit())


def amount_specific_digit(num):
    """
    count the amount of the specific digit in all file
    """
    with open(phil_pat, "r") as file_2:
        k = 0
        file_content = file_2.read()
        for i in file_content:
            if i == num:
                k += 1
            else:
                continue
        return k


print(amount_specific_digit("1"))


def special_words():
    """
    create a list of special words
    (<<word>> is special as it starts with << and ends with >>)
    """
    with open(phil_pat, 'r') as file_3:
        s = []
        for file_line in range(4):
            file_content_3 = file_3.readline()
            if "<" in file_content_3:
                for i in file_content_3:
                    if i == "<":
                        aa = file_content_3.index(i)
                    elif i == ">":
                        bb = file_content_3.index(i)
                s.append(file_content_3[aa:bb + 2])
                # print(file_content_3[aa:bb + 2])
            else:
                continue
        return s


print(special_words())


def file_without_digits(new_file_name):
    """
    create another file which will be the given file only without digits
    """
    with open(new_file_name, 'a') as file_4:
        for i in open(phil_pat, 'r'):
            for j in i:
                if j.isdigit():
                    continue
                else:
                    file_4.write(j)


file_without_digits("test_3")
