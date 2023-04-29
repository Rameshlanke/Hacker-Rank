if __name__ == '__main__': 
    records = []
    scores = []
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)

    # print(records,"\n", scores,"\n", student)

    scores.sort()
    records.sort()
    second_lowest = scores[0]
    # print(records,"\n", scores,"\n", student)

    for i in scores :
        if(second_lowest < i):
            second_lowest = i
            break


    for record in records:
        if(record[1] == second_lowest):
            print(record[0])