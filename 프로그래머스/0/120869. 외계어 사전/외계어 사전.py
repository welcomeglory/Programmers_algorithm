def solution(spell, dic):
    # spell을 사전순으로 정렬하여 문자열로 변환
    spell_sorted = ''.join(sorted(spell))
    
    for word in dic:
        # dic의 각 단어를 정렬하여 비교
        if ''.join(sorted(word)) == spell_sorted:
            return 1
    
    return 2