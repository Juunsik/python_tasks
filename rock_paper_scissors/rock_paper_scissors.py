import random

RPS = ("가위", "바위", "보")
computer_win = 0
player_win = 0
draw = 0

while 1:
    # 컴퓨터에 무작위로 하나를 선택
    computer = random.choice(RPS)

    player = input("가위, 바위, 보 중 하나를 선택하세요: ").strip()

    # 유효한 입력인지 판별
    # 플레이어와 컴퓨터 승패 판정, 통계 계산
    if player in RPS:
        if computer == player:
            print("무승부!")
            draw += 1
        elif computer == "가위":
            if player == "바위":
                print(f"사용자: {player}, 컴퓨터: {computer}")
                print("사용자 승리!")
                player_win += 1
            else:
                print(f"사용자: {player}, 컴퓨터: {computer}")
                print("컴퓨터 승리!")
                computer_win += 1
        elif computer == "바위":
            if player == "보":
                print(f"사용자: {player}, 컴퓨터: {computer}")
                print("사용자 승리!")
                player_win += 1
            else:
                print(f"사용자: {player}, 컴퓨터: {computer}")
                print("컴퓨터 승리!")
                computer_win += 1
        else:
            if player == "가위":
                print(f"사용자: {player}, 컴퓨터: {computer}")
                print("사용자 승리!")
                player_win += 1
            else:
                print(f"사용자: {player}, 컴퓨터: {computer}")
                print("컴퓨터 승리!")
                computer_win += 1

        # 게임 재시작 여부
        # 대소문자 구분하지 않게 lower로 통일
        if input("다시 하시겠습니까? (y/n): ").lower() == "y":
            continue
        else:
            print("게임을 종료합니다.")
            print(f"승: {player_win} 패: {computer_win} 무승부: {draw}")
            break
    else:
        print("유효한 입력이 아닙니다.")
