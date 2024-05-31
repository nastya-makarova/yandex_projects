def get_instructions(s):
    number_of_command = 0
    for i in range(len(s)):
        if '[' not in s:
            return s
        if s[i].isdigit():
            number_of_command = number_of_command * 10 + int(s[i])
            len_num = len(str(number_of_command))
        if s[i] == '[':
            if not s[i - 1].isdigit():
                number_of_command = 1
                len_num = 0
            j = i + 1
            while j in range(i + 1, len(s)):

                if s[j] == ']':
                    result = ''
                    result += number_of_command * s[i + 1:j]
                    s = str.replace(
                        s, s[i - len_num:j + 1], result)
                    number_of_command = 0
                    j += 1
                    break
                elif s[j] == '[':
                    s = s[:j - 1] + get_instructions(s[j - 1:])
                    j = i + 1
                else:
                    j += 1

    return s


if __name__ == '__main__':
    s = input()
    print(get_instructions(s))
