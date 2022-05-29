def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dic = {id: [] for id in id_list}
    report = set(report)
    report = list(report)

    for i in report:
        i = i.split(' ')
        dic[i[1]].append(i[0])

    for key, value in dic.items():
        if len(value) >= k:
            for i in value:
                answer[id_list.index(i)] += 1

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
print(solution(id_list,report,2))