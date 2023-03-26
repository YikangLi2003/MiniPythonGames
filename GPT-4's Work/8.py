from PIL import Image, ImageDraw

def create_godzilla_image(image_name):
    # 创建一个空白图像
    image = Image.new('RGBA', (80, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # 绘制哥斯拉身体
    draw.rectangle([20, 50, 60, 110], fill=(100, 200, 100, 255))

    # 绘制哥斯拉头部
    draw.ellipse([30, 10, 50, 40], fill=(100, 200, 100, 255))

    # 绘制哥斯拉腿部
    draw.rectangle([30, 110, 35, 120], fill=(100, 200, 100, 255))
    draw.rectangle([45, 110, 50, 120], fill=(100, 200, 100, 255))

    # 绘制哥斯拉尾巴
    if image_name == "godzilla1.png":
        draw.polygon([60, 80, 90, 70, 60, 70], fill=(100, 200, 100, 255))
    elif image_name == "godzilla2.png":
        draw.polygon([60, 80, 90, 90, 60, 90], fill=(100, 200, 100, 255))

    # 保存图像
    image.save(image_name)

# 生成两个哥斯拉贴图
create_godzilla_image("godzilla1.png")
create_godzilla_image("godzilla2.png")
