from PIL import Image, ImageDraw

# 创建一个空白图像
image = Image.new('RGB', (800, 600), 'skyblue')
draw = ImageDraw.Draw(image)

# 绘制哥斯拉
draw.rectangle((100, 300, 200, 550), fill='darkgreen', outline='black', width=3)  # 身体
draw.line((200, 350, 280, 320), fill='darkgreen', width=3)  # 右手臂
draw.line((100, 350, 20, 320), fill='darkgreen', width=3)  # 左手臂
draw.polygon([(150, 200), (100, 300), (200, 300)], fill='darkgreen', outline='black', width=3)  # 头部

# 绘制巨型猫咪
draw.ellipse((500, 400, 700, 550), fill='gray', outline='black', width=3)  # 身体
draw.ellipse((550, 250, 650, 400), fill='gray', outline='black', width=3)  # 头部
draw.arc((575, 325, 625, 375), 0, 180, fill='black', width=2)  # 嘴巴
draw.polygon([(600, 275), (610, 300), (620, 275)], fill='gray', outline='black', width=3)  # 爪子

# 绘制哥斯拉吐出的蓝色光柱
draw.line((150, 250, 650, 250), fill='blue', width=10)

# 保存图像
image.save('godzilla_vs_cat.png')
