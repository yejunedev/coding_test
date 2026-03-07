def solution(todo_list, finished):
    answer = []
    n=len(todo_list)
    for i in range(n):
        if finished[i]==False:
            answer.append(todo_list[i])
    return answer