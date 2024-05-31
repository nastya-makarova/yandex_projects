#  114121124
def min_carrying_count(weights: list[int], limit: int) -> int:
    """
    Определяет минимальное количество транспортных платформ,
    необходимое для перевозки роботов.

    """

    weights.sort()

    min_carrying_count = 0

    left_pointer = 0
    right_pointer = len(weights) - 1

    while left_pointer <= right_pointer:

        if weights[left_pointer] + weights[right_pointer] <= limit:
            left_pointer += 1

        min_carrying_count += 1
        right_pointer -= 1

    return min_carrying_count


if __name__ == '__main__':
    print(
        min_carrying_count([int(num) for num in input().split()], int(input()))
        )
