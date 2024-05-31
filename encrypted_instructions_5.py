#  114769659
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


def decode(encoded_string: str) -> str:
    """
    Функкция расшифровывает сжатые сообщения и
    возвращает расшифрованную строку.
    """
    num_stack = Stack()
    char_stack = Stack()

    cmd_count = ''
    decoded_string = ''

    for char in encoded_string:

        if char >= '0' and char <= '9':
            cmd_count += char
        elif char == '[':
            num_stack.push(cmd_count)
            char_stack.push(decoded_string)
            cmd_count = ''
            decoded_string = ''
        elif char == ']':
            cmd_count = int(num_stack.pop())
            command_buffer = char_stack.pop()
            decoded_string = command_buffer + decoded_string * cmd_count
            cmd_count = ''
        else:
            decoded_string += char

    return decoded_string


if __name__ == '__main__':
    encoded_string = input()
    print(decode(encoded_string))
