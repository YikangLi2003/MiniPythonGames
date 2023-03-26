import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

# 设置窗口标题
pygame.display.set_caption("Godzilla Movement")

# 加载哥斯拉图像
godzilla_images = [pygame.image.load('godzilla1.png'), pygame.image.load('godzilla2.png')]

# 设置哥斯拉的初始位置
godzilla_position = [400, 300]
godzilla_speed = 5

# 设置哥斯拉的动画帧计数器
frame_counter = 0

# 游戏主循环
while True:
    screen.fill((255, 255, 255))  # 填充背景颜色

    # 响应事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 响应键盘按键
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        godzilla_position[0] -= godzilla_speed
    if keys[pygame.K_RIGHT]:
        godzilla_position[0] += godzilla_speed
    if keys[pygame.K_UP]:
        godzilla_position[1] -= godzilla_speed
    if keys[pygame.K_DOWN]:
        godzilla_position[1] += godzilla_speed

    # 更新动画帧
    frame_counter = (frame_counter + 1) % 20
    current_frame = frame_counter // 10

    # 绘制哥斯拉
    screen.blit(godzilla_images[current_frame], godzilla_position)

    # 更新屏幕
    pygame.display.update()
    pygame.time.delay(50)
