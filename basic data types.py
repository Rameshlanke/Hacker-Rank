if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    values=student_marks[query_name]
    avg=round((sum(values)/len(values)),2)
    # if query_name==student_marks[query_name]:
    print(format(avg,".2f"))
