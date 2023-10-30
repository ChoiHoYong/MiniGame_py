import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1000
screen_height = 560
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("가위바위보 게임")

# 이미지 로드
background_image = pygame.image.load("TitleScene.png")
button_image = pygame.image.load("back_button.png")
game_images = {
    "가위": pygame.image.load("2.png"),
    "바위": pygame.image.load("0.png"),
    "보": pygame.image.load("5.png")
}

# 게임 변수
user_choice = None
computer_choice = None
result = None
font = pygame.font.Font(None, 36)

def show_title_screen():
    screen.blit(background_image, (0, 0))
    button_rect = screen.blit(button_image, (250, 400))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

def play_game():
    global user_choice, computer_choice, result

    choices = ["가위", "바위", "보"]
    computer_choice = random.choice(choices)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    user_choice = "가위"
                elif event.key == pygame.K_2:
                    user_choice = "바위"
                elif event.key == pygame.K_3:
                    user_choice = "보"
                else:
                    continue

                result = determine_winner(user_choice, computer_choice)

        if user_choice is not None:
            break

        screen.fill((255, 255, 255))
        user_text = font.render("가위(1), 바위(2), 보(3)를 선택하세요.", True, (0, 0, 0))
        screen.blit(user_text, (200, 250))
        pygame.display.update()

    show_result()

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

def show_result():
    result_text = font.render(f"컴퓨터: {computer_choice}   유저: {user_choice}", True, (0, 0, 0))
    result_label = font.render(result, True, (0, 0, 0))

    screen.fill((255, 255, 255))
    screen.blit(result_text, (200, 200))
    screen.blit(result_label, (350, 300))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

show_title_screen()
play_game()

pygame.quit()
