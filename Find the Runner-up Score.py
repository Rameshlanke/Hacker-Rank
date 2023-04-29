if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sortedarr = sorted(arr)
    new_list = set(sortedarr)
    new_list.remove(max(new_list))
    print(max(new_list))

    