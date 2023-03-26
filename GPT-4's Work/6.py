import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon, Arc

fig, ax = plt.subplots(figsize=(5, 6))

# 绘制猫咪身体
cat_body = Ellipse((0.5, 0.4), 0.4, 0.5, angle=0, linewidth=2, fill=True, color='gray')
ax.add_patch(cat_body)

# 绘制猫咪头部
cat_head = Ellipse((0.5, 0.8), 0.25, 0.25, angle=0, linewidth=2, fill=True, color='gray')
ax.add_patch(cat_head)

# 绘制猫咪耳朵
cat_ear1 = Polygon([[0.4, 0.95], [0.35, 1], [0.45, 1]], closed=True, linewidth=2, fill=True, color='gray')
cat_ear2 = Polygon([[0.6, 0.95], [0.55, 1], [0.65, 1]], closed=True, linewidth=2, fill=True, color='gray')
ax.add_patch(cat_ear1)
ax.add_patch(cat_ear2)

# 绘制猫咪眼睛
cat_eye1 = Ellipse((0.43, 0.82), 0.08, 0.1, angle=0, linewidth=2, fill=True, color='white')
cat_eye2 = Ellipse((0.57, 0.82), 0.08, 0.1, angle=0, linewidth=2, fill=True, color='white')
ax.add_patch(cat_eye1)
ax.add_patch(cat_eye2)

# 绘制猫咪眼珠
cat_pupil1 = Ellipse((0.43, 0.81), 0.04, 0.05, angle=0, linewidth=2, fill=True, color='black')
cat_pupil2 = Ellipse((0.57, 0.81), 0.04, 0.05, angle=0, linewidth=2, fill=True, color='black')
ax.add_patch(cat_pupil1)
ax.add_patch(cat_pupil2)

# 绘制猫咪嘴巴
cat_mouth1 = Arc((0.48, 0.78), 0.1, 0.1, angle=0, theta1=0, theta2=180, linewidth=2, color='black')
cat_mouth2 = Arc((0.52, 0.78), 0.1, 0.1, angle=0, theta1=0, theta2=180, linewidth=2, color='black')
ax.add_patch(cat_mouth1)
ax.add_patch(cat_mouth2)

# 配置轴
ax.axis('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 保存和显示图像
plt.savefig('detailed_cat.png')
plt.show()