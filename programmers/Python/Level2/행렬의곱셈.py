"""
문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""

def solution(arr1, arr2):
    
    arr2 = [[arr2[row][col] for row in range(len(arr2))]for col in range(len(arr2[0]))]
    
    answer = [[
        sum(map(lambda x,y : x*y,arr1[row1],arr2[row2]))
    for row2 in range(len(arr2))] for row1 in range(len(arr1))]
    
    return answer

def check(truth, result) :
    state = True
    for trow, rrow in zip(truth, result) :
        if not state :
            break
        if len(trow) != len(rrow) :
            state = False
            break
        for t, r in zip(trow, rrow) :
            if t != r :
                state =False
                break   
    return state

if __name__ == "__main__" :
    arr1 = [[1, 4], [3, 2], [4, 1]]
    arr2 = [[3, 3], [3, 3]]
    truth = [[15, 15], [15, 15], [15, 15]]
    result = solution(arr1, arr2)
    print(f"1번 : {check(truth, result)}")

    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
    truth = [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
    result = solution(arr1, arr2)
    print(f"2번 : {check(truth, result)}")