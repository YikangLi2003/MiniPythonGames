from PIL import Image, ImageDraw

# 创建一个空白图像
image = Image.new('RGB', (300, 500), 'white')
draw = ImageDraw.Draw(image)

# 绘制头部
draw.ellipse((100, 50, 200, 150), fill='orange', outline='black', width=3)

# 绘制身体
draw.rectangle((135, 150, 165, 350), fill='blue', outline='black', width=3)

# 绘制腿
draw.line((135, 350, 120, 450), fill='black', width=3)
draw.line((165, 350, 180, 450), fill='black', width=3)

# 绘制手臂
draw.line((135, 180, 100, 280), fill='black', width=3)
draw.line((165, 180, 200, 280), fill='black', width=3)

# 绘制眼睛
draw.ellipse((120, 80, 130, 90), fill='white', outline='black', width=2)
draw.ellipse((170, 80, 180, 90), fill='white', outline='black', width=2)

# 绘制嘴巴
draw.arc((130, 100, 170, 130), 0, 180, fill='black', width=2)

# 保存图像
image.save('human_image.png')
