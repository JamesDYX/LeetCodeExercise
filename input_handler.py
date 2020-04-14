def getnumArray():
    nums = list(map(int, input().split(' ')))
    return nums


def getnumMatrix():
    matrix = []
    row = int(input())
    for r in range(row):
        matrix.append(list(map(int, input().split(' '))))
    return matrix


def getstringArray():
    chars = input().split(' ')
    return chars


if __name__ == '__main__':
    print(getstringArray())