# (1)회원가입 시작 화면 만들기 : 회원가입 진행 여부 확인
print("===============================")
print("회원가입")
print("===============================")

register = False
# register = False일때 동안 계속 진행(True가 되면 종료)
while not register:
        print("회원가입을 진행하시겠습니까?\ny:진행     n:취소")
        register_input = input(">> ")
        register_input = register_input.lower()

        if register_input == "y":
                register = True
                print("===============================")
                print("회원가입이 진행됩니다")
                print("===============================")
        # 입력값이 n인 경우 exit 함수로 while문 종료
        elif register_input == "n":
                print("===============================")
                print("회원가입이 취소됩니다")
                print("===============================")
                exit()
        else:
                print("입력값을 확인해주세요")  
        
# (2)회원가입 진행 : ID, PW 입력 받기
# users 리스트 선언(user들의 정보를 담음)
users = []
# user 딕셔너리 선언(새로운 user의 정보를 담음) -> ID, PW, 이름, 생년월일, 이메일 입력 
while True:
    user = {}
    username = input("ID: ")
    # 패스워드가 일치할 때까지 계속 입력 받음
    while True:
           password = input("PW: ")
           password_confirm = input("PW 확인: ")
           if password == password_confirm:
                  break
           else:
                  print("패스워드가 일치하지 않습니다")
    # 이름 입력                 
    name = input("이름: ")
    # 생년월일 입력 -> 양식에 맞을 때까지 계속 입력 받음
    while True:
           birth_date = input("생년월일(6자리): ")
           if len(birth_date) == 6:
                  break
           else:
                  print("생년월일 입력값이 올바르지 않습니다") 
    # 이메일 입력
    email = input("이메일: ")
    # user 딕셔너리 요소값 할당
    user["username"] = username
    user["password"] = password
    user["name"] = name
    user["birth_date"] = birth_date
    user["email"] = email
    # user 리스트에 새로운 user 추가 
    users.append(user)
    print(users)
    # 회원가입 완료 메시지 출력
    print("----------------------------")
    print(f"{user['name']}님 가입을 환영합니다!")
    print("----------------------------")
    # 추가 회원가입 의사 확인   
    print("회원가입을 추가로 진행하시겠습니까?")
    register_another_input = input(">> ")
    register_another_input = register_another_input.lower()
    if register_another_input == "y":
           pass
    elif register_another_input == "n":
           exit()