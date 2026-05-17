def solution(cards1, cards2, goal):
    # 각 카드 뭉치 현재 단어 가리킬 인덱스 변수
    idx1 = 0
    idx2 = 0
    
    # goal의 단어들을 순서대로 확인
    for word in goal:
        # 1. cards1에 아직 사용할 카드가 남아있고, 현재 단어가 cards1의 맨 앞 단어와 일치할 때
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1 # 다음 카드로 이동
        # 2. cards2에 아직 사용할 카드가 남아있고, 현재 단어가 cards2의 맨 앞 단어와 일치할 때
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1 # 다음 카드로 이동
        # 3. 두 카드 뭉치의 맨 앞 단어 모두와 일치하지 않는 경우 (규칙 위반)
        else:
            return "No"
            
    # goal의 모든 단어를 규칙에 맞게 처리했다면 Yes 반환
    return "Yes"