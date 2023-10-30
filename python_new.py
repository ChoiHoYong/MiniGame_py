import tkinter as tk
from tkinter import PhotoImage
import random
import time

def game1():
    game_window = create_game_window("가위바위보 게임")

    user_choice = tk.StringVar()
    computer_choice = tk.StringVar()
    result = tk.StringVar()

    # 가위바위보 게임 함수
    def play_game():
        choices = ["가위", "바위", "보"]
        computer_choice_str = random.choice(choices)
        user_choice_str = user_choice.get()
        computer_choice.set(computer_choice_str)
        
        game_label = tk.Label(game_frame, text="컴퓨터: " + computer_choice_str + " 유저: " + user_choice_str, font=font_style)
        game_label.pack()

        result_str = determine_winner(user_choice_str, computer_choice_str)
        result.set(result_str)

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

    # 이미지 미리 로드
    image0 = PhotoImage(file="0.png")
    image2 = PhotoImage(file="2.png")
    image5 = PhotoImage(file="5.png")

    # 게임 프레임 생성
    game_frame = tk.Frame(game_window)
    game_frame.pack()

    game_label = tk.Label(game_frame, text="가위바위보 게임(가위, 바위, 보)", font=font_style)
    game_label.pack()

    buttons_frame = tk.Frame(game_frame)
    buttons_frame.pack()

    scissors_button = tk.Button(buttons_frame, text="가위", image=image2, command=lambda: user_choice.set("가위"), **button_style)
    scissors_button.photo = image2
    scissors_button.pack(side="left")

    rock_button = tk.Button(buttons_frame, text="바위", image=image0, command=lambda: user_choice.set("바위"), **button_style)
    rock_button.photo = image0
    rock_button.pack(side="left")

    paper_button = tk.Button(buttons_frame, text="보", image=image5, command=lambda: user_choice.set("보"), **button_style)
    paper_button.photo = image5
    paper_button.pack(side="left")

    play_button = tk.Button(game_frame, text="가위바위보!", command=play_game, **button_style)
    play_button.pack()

    result_label = tk.Label(game_frame, textvariable=result, font=font_style)
    result_label.pack()

def game2():
    game_window = create_game_window("주사위 굴리기 게임")

    dice_images = [PhotoImage(file=f"dice_{i}.png") for i in range(1, 7)]

    # Game variables
    user_result = tk.StringVar()
    computer_result = tk.StringVar()

    def roll_dice():
        # Simulate dice rolling animation
        for _ in range(10):
            user_roll = random.randint(1, 6)
            computer_roll = random.randint(1, 6)
            user_result.set(dice_images[user_roll - 1])
            computer_result.set(dice_images[computer_roll - 1])
            app.update()
            time.sleep(0.2)

        user_roll = random.randint(1, 6)
        computer_roll = random.randint(1, 6)
        user_result.set(dice_images[user_roll - 1])
        computer_result.set(dice_images[computer_roll - 1])
    
        determine_winner(user_roll, computer_roll)

    def determine_winner(user_roll, computer_roll):
        if user_roll > computer_roll:
            result_label.config(text="당신이 이겼습니다!")
        elif user_roll < computer_roll:
            result_label.config(text="컴퓨터가 이겼습니다!")
        else:
            result_label.config(text="무승부!")

    # Game UI
    roll_button = tk.Button(app, text="주사위 굴리기", command=roll_dice, **button_style)
    roll_button.pack()

    user_dice_label = tk.Label(app, image=None, textvariable=user_result)
    user_dice_label.pack()

    computer_dice_label = tk.Label(app, image=None, textvariable=computer_result)
    computer_dice_label.pack()

    result_label = tk.Label(app, text="", font=font_style)
    result_label.pack()

def game3():
    game_window = create_game_window("UPDOWN 게임")

    def play_updown_game():
        target_number = random.randint(0, 50)
        attempts = 0

        message_label = tk.Label(game_window, text="0 ~ 50 사이의 숫자를 고르세요.", font=font_style, bg="lightyellow")
        message_label.pack(pady=10)
        
        def check_guess():
            nonlocal attempts
            user_guess = user_input.get()
            user_input.delete(0, "end")
            
            try:
                user_guess = int(user_guess)
            except ValueError:
                message_label.config(text="올바른 숫자를 입력하세요.", fg="red")
                return

            attempts += 1

            if user_guess < target_number:
                message_label.config(text="UP! 더 큰 숫자를 선택하세요.", fg="blue")
            elif user_guess > target_number:
                message_label.config(text="DOWN! 더 작은 숫자를 선택하세요.", fg="blue")
            else:
                message_label.config(text=f"정답! {attempts}번만에 맞췄습니다.", fg="green")
                user_input.config(state="disabled")
                check_button.config(state="disabled")

        user_input = tk.Entry(game_window, font=font_style)
        user_input.pack(pady=10)
        
        check_button = tk.Button(game_window, text="확인", command=check_guess, **button_style)
        check_button.pack(pady=10)
        
        message_label = tk.Label(game_window, text="", font=font_style)
        message_label.pack(pady=20)

    play_updown_game()

def game4():
    game_window = create_game_window("과일 스무고개 게임")

    def play_fruit_game():
        fruits = {
            "사과": ["빨간색이며 원형입니다", "맛있는 과일 중 하나입니다", "고요한 계절에 자라는 과일입니다"],
            "딸기": ["작고 빨간색이며 씨가 밖으로 돌출돼 있습니다", "아이스크림에 자주 올려먹는 과일입니다", "딸기잼으로도 많이 쓰입니다"],
            "포도": ["작고 둥글며 보라색 또는 초록색입니다", "포도주로 만들어지는 과일입니다", "큰 손에 들어가는 것이 어려운 크기입니다"],
            "귤": ["오렌지색이며 작고 동그란 모양입니다", "겉 껍질을 까야 속을 먹을 수 있습니다", "겉 껍질이 두껍게 나 있습니다"],
            "배": ["노란색 또는 녹색이며 오각형입니다", "부드럽고 달콤한 맛을 가진 과일입니다", "아침식사에 자주 먹는 과일 중 하나입니다"]
        }
        # 과일 고르기
        target_fruit = random.choice(list(fruits.keys()))
        # 설명 고르기
        target_feature = random.choice(fruits[target_fruit])

        message_label = tk.Label(game_window, text=f"특징을 알려드립니다\n{target_feature}", font=font_style)
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

        user_input = tk.Entry(game_window, font=font_style)
        user_input.pack()
        
        check_button = tk.Button(game_window, text="확인", command=check_guess, **button_style)
        check_button.pack()

    play_fruit_game()

app = tk.Tk()
app.title("나때는말이야")

# 윈도우 크기 설정
app.geometry("1000x560")
app.resizable(False, False)

# 이미지 보여주기
background_image = tk.PhotoImage(file="TitleScene.png")
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# 스타일 정의
font_style = ("Helvetica", 22)
button_style = {
    "padx": 0,
    "pady": 0,
    "font": font_style,
}

# 게임 화면으로 이동하는 함수들
def create_game_window(title):
    game_window = tk.Toplevel(app)
    game_window.title(title)

    # 윈도우 크기 설정
    game_window.geometry("1000x560")  # 너비 x 높이
    game_window.resizable(False, False)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    return game_window


# 타이틀 생성
title_font = ("Helvetica", 50) 
game_label = tk.Label(app, text="으라차차", font=title_font)

game_label.pack(pady=90) 

button_frame = tk.Frame(app)
button_frame.pack()

# 버튼 이미지
button_image = tk.PhotoImage(file="back_button.png")

# 버튼 생성
button1 = tk.Button(button_frame, image=button_image, width=500, height=70, text="가위바위보", bd=0, highlightthickness=0, command=game1, **button_style, fg="white", compound="center")
button2 = tk.Button(button_frame, image=button_image, width=500, height=70, text="주사위", bd=0, highlightthickness=0, command=game2, **button_style, fg="white", compound="center")
button3 = tk.Button(button_frame, image=button_image, width=500, height=70, text="UPDOWN", bd=0, highlightthickness=0, command=game3, **button_style, fg="white", compound="center")
button4 = tk.Button(button_frame, image=button_image, width=500, height=70, text="과일 스무고개", bd=0, highlightthickness=0, command=game4, **button_style, fg="white", compound="center")

# 버튼을 세로로 배치하기 위해 pack 사용
button1.pack()
button2.pack()
button3.pack()
button4.pack()

# 애플리케이션 실행
app.mainloop()