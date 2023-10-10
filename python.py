import tkinter as tk
import random
import time

app = tk.Tk()
app.title("나때는말이야")

# 윈도우 크기 설정
app.geometry("400x300")  # 너비 x 높이

# 게임 화면으로 이동하는 함수들
def game1():
    # 게임 1로 이동
    game_window = tk.Toplevel(app)
    game_window.title("가위바위보 게임")

    # 윈도우 크기 설정
    game_window.geometry("400x300")  # 너비 x 높이

    # 가위바위보 게임 함수
    def play_game(user_choice):
        choices = ["가위", "바위", "보"]
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)
        result_label.config(text=f"컴퓨터 선택: {computer_choice}\n결과: {result}")

    def determine_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "무승부"
        elif (
            (user_choice == "가위" and computer_choice == "보")
            or (user_choice == "바위" and computer_choice == "가위")
            or (user_choice == "보" and computer_choice == "바위")
        ):
            return "사용자 승리"
        else:
            return "컴퓨터 승리"

    # 가위바위보 게임 화면 생성
    game_label = tk.Label(game_window, text="가위바위보 게임을 시작하세요:")
    game_label.pack()

    user_choice_entry = tk.Entry(game_window)
    user_choice_entry.pack()

    play_button = tk.Button(game_window, text="가위바위보!", command=lambda: play_game(user_choice_entry.get()))
    play_button.pack()

    result_label = tk.Label(game_window, text="")
    result_label.pack()

def game2():
    # 게임 2로 이동하는 코드를 여기에 추가하세요.
    game_label.config(text="게임 2 화면으로 이동")

    game_window = tk.Toplevel(app)
    game_window.title("주사위 굴리기 게임")

    # 윈도우 크기 설정
    game_window.geometry("400x300")  # 너비 x 높이

    def roll_dice():
        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        
        user_result_label.config(text=f"당신의 주사위 숫자: {user_roll}")
        computer_result_label.config(text=f"컴퓨터의 주사위 숫자: {computer_roll}")
        
        time.sleep(1)  # 1초 딜레이
        
        if user_roll > computer_roll:
            result_label.config(text="당신이 이겼습니다!")
        elif user_roll < computer_roll:
            result_label.config(text="컴퓨터가 이겼습니다!")
        else:
            result_label.config(text="무승부!")

    # 주사위 굴리기 게임 화면 생성
    roll_button = tk.Button(game_window, text="주사위 굴리기", command=roll_dice)
    roll_button.pack()

    user_result_label = tk.Label(game_window, text="")
    user_result_label.pack()

    computer_result_label = tk.Label(game_window, text="")
    computer_result_label.pack()

    result_label = tk.Label(game_window, text="")
    result_label.pack()


def game3():
    # 게임 3로 이동하는 코드를 여기에 추가하세요.
    # 게임 3로 이동
    game_window = tk.Toplevel(app)
    game_window.title("UPDOWN 게임")

    # 윈도우 크기 설정
    game_window.geometry("400x300")  # 너비 x 높이

    def play_updown_game():
        # UPDOWN 게임 함수
        target_number = random.randint(0, 50)
        attempts = 0

        message_label = tk.Label(game_window, text="UPDOWN 게임을 시작합니다. 0 ~ 50 사이의 숫자를 고르세요.")
        message_label.pack()
        #message_label.config(text="UPDOWN 게임을 시작합니다. 0 ~ 50 사이의 숫자를 고르세요.")
        
        def check_guess():
            nonlocal attempts
            user_guess = user_input.get()
            user_input.delete(0, "end")
            
            try:
                user_guess = int(user_guess)
            except ValueError:
                message_label.config(text="올바른 숫자를 입력하세요.")
                return

            attempts += 1

            if user_guess < target_number:
                message_label.config(text="UP! 더 큰 숫자를 선택하세요.")
            elif user_guess > target_number:
                message_label.config(text="DOWN! 더 작은 숫자를 선택하세요.")
            else:
                message_label.config(text=f"정답! {attempts}번만에 맞췄습니다.")
                user_input.config(state="disabled")
                check_button.config(state="disabled")

        user_input = tk.Entry(game_window)
        user_input.pack()
        
        check_button = tk.Button(game_window, text="확인", command=check_guess)
        check_button.pack()
        
        message_label = tk.Label(game_window, text="")
        message_label.pack()

    play_updown_game()


def game4():
    # 게임 4로 이동하는 코드를 여기에 추가하세요.
    game_label.config(text="게임 4 화면으로 이동")

    game_window = tk.Toplevel(app)
    game_window.title("과일 스무고개 게임")

    # 윈도우 크기 설정
    game_window.geometry("400x300")  # 너비 x 높이

    def play_fruit_game():
        # 과일 스무고개 게임 함수
        fruits = {
            "사과": ["빨간색이며 원형입니다.", "맛있는 과일 중 하나입니다.", "고요한 계절에 자라는 과일입니다."],
            "딸기": ["작고 빨간색이며 씨가 밖으로 돌출돼 있습니다.", "아이스크림에 자주 올려먹는 과일입니다.", "딸기잼으로도 많이 쓰입니다."],
            "포도": ["작고 둥글며 보라색 또는 초록색입니다.", "포도주로 만들어지는 과일입니다.", "큰 손에 들어가는 것이 어려운 크기입니다."],
            "귤": ["오렌지색이며 작고 동그란 모양입니다.", "겉 껍질을 까야 속을 먹을 수 있습니다.", "겉 껍질이 두껍게 나 있습니다."],
            "배": ["노란색 또는 녹색이며 오각형입니다.", "부드럽고 달콤한 맛을 가진 과일입니다.", "아침식사에 자주 먹는 과일 중 하나입니다."]
        }
        target_fruit = random.choice(list(fruits.keys()))
        target_feature = random.choice(fruits[target_fruit])

        message_label = tk.Label(game_window, text=f"특징을 알려드립니다:\n{target_feature}")
        message_label.pack()

        def check_guess():
            user_guess = user_input.get().strip().lower()
            user_input.delete(0, "end")
            
            if user_guess == target_fruit:
                message_label.config(text=f"정답! {target_fruit}입니다.")
                user_input.config(state="disabled")
                check_button.config(state="disabled")
            else:
                new_feature = random.choice([f for f in fruits[target_fruit] if f != target_feature])
                message_label.config(text=f"틀렸습니다. 다른 특징을 알려드립니다:\n{new_feature}")

        user_input = tk.Entry(game_window)
        user_input.pack()
        
        check_button = tk.Button(game_window, text="확인", command=check_guess)
        check_button.pack()

    play_fruit_game()


# 레이블 생성
game_label = tk.Label(app, text="나때는 말이야!!")
game_label.grid(row=0, column=0, columnspan=4)  # 레이블을 4열로 확장

# 버튼 생성
button1 = tk.Button(app, text="가위바위보", command=game1)
button2 = tk.Button(app, text="주사위", command=game2)
button3 = tk.Button(app, text="UPDOWN", command=game3)
button4 = tk.Button(app, text="과일 스무고개", command=game4)

# 버튼을 가로로 배치하기 위해 grid 사용
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=1, column=3)

# 애플리케이션 실행
app.mainloop()
