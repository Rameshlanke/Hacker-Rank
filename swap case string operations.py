def swap_case(s):
    word = s.swapcase()
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)