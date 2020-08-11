# 해시
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    b = min(phone_book, key=len)
    cnt = 0
    for i in phone_book:
        if b == i[:len(b)]:
            cnt += 1
    if cnt > 1:
        answer = False
    return answer