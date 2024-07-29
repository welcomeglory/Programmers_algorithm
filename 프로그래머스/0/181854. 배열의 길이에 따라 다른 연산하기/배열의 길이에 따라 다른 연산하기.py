def solution(arr, n):
    # 배열의 길이가 홀수인지 짝수인지 확인
    if len(arr) % 2 == 1:
        # 길이가 홀수일 때: 짝수 인덱스에 n을 더하기
        return [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))]
    else:
        # 길이가 짝수일 때: 홀수 인덱스에 n을 더하기
        return [arr[i] + n if i % 2 == 1 else arr[i] for i in range(len(arr))]
