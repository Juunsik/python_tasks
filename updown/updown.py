from os import path
import random


com_num = random.randint(1, 100)

count = 1
cycle = 1

while 1:
    if path.exists("updown/record.txt"):
        with open("updown/record.txt", "r", encoding="utf-8") as r:
            max_cnt = "".join(r.readlines())
            if cycle == 1:
                print("이전 게임 플레이어 최고 시도 횟수: " + max_cnt)
    else:
        max_cnt = 0

    player_num = int(input("숫자를 입력하세요: "))

    if 1 <= player_num and player_num <= 100:
        if com_num == player_num:
            print("맞았습니다!!")
            print(f"시도한 횟수: {count}")
            if input("다시 하시겠습니까? (y/n): ") == "y":
                with open("updown/record.txt", "w", encoding="utf-8") as r:
                    r.write(str(max(count, int(max_cnt))))
                com_num = random.randint(1, 100)
                count = 1
                cycle = 1
                continue
            else:
                print("게임을 종료합니다.")
                break
        elif com_num < player_num:
            print("다운")
            count += 1
        else:
            print("업")
            count += 1
    else:
        print("유효한 범위 내의 숫자를 입력하세요.")

    cycle += 1
