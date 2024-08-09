def solution(id_pw, db):
    user_id, user_pw = id_pw  # 입력된 아이디와 비밀번호
    
    for entry in db:
        db_id, db_pw = entry  # 데이터베이스의 각 회원 정보
        if db_id == user_id:
            if db_pw == user_pw:
                return "login"  # 아이디와 비밀번호가 모두 일치하는 경우
            else:
                return "wrong pw"  # 아이디는 일치하지만 비밀번호가 일치하지 않는 경우

    return "fail"  # 일치하는 아이디가 없는 경우
