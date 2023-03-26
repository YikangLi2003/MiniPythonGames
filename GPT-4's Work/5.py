import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制哥斯拉
godzilla_body = Ellipse((0.3, 0.5), 0.2, 0.5, angle=-10, linewidth=2, fill=True, color='darkgreen')
godzilla_head = Polygon([[0.25, 0.7], [0.35, 0.8], [0.45, 0.7]], closed=True, linewidth=2, fill=True, color='darkgreen')
godzilla_leg1 = Polygon([[0.2, 0.4], [0.25, 0.15], [0.3, 0.4]], closed=True, linewidth=2, fill=True, color='darkgreen')
godzilla_leg2 = Polygon([[0.4, 0.4], [0.45, 0.15], [0.5, 0.4]], closed=True, linewidth=2, fill=True, color='darkgreen')
godzilla_arm1 = Polygon([[0.15, 0.6], [0.2, 0.4], [0.3, 0.55]], closed=True, linewidth=2, fill=True, color='darkgreen')
godzilla_arm2 = Polygon([[0.45, 0.55], [0.55, 0.4], [0.6, 0.6]], closed=True, linewidth=2, fill=True, color='darkgreen')

ax.add_patch(godzilla_body)
ax.add_patch(godzilla_head)
ax.add_patch(godzilla_leg1)
ax.add_patch(godzilla_leg2)
ax.add_patch(godzilla_arm1)
ax.add_patch(godzilla_arm2)

# 绘制猫咪
cat_body = Ellipse((0.7, 0.5), 0.25, 0.5, angle=10, linewidth=2, fill=True, color='gray')
cat_head = Ellipse((0.85, 0.8), 0.15, 0.15, angle=0, linewidth=2, fill=True, color='gray')
cat_leg1 = Polygon([[0.65, 0.4], [0.7, 0.15], [0.75, 0.4]], closed=True, linewidth=2, fill=True, color='gray')
cat_leg2 = Polygon([[0.85, 0.4], [0.9, 0.15], [0.95, 0.4]], closed=True, linewidth=2, fill=True, color='gray')
cat_arm = Polygon([[0.95, 0.7], [0.9, 0.85], [0.85, 0.7]], closed=True, linewidth=2, fill=True, color='gray')

ax.add_patch(cat_body)
ax.add_patch(cat_head)
ax.add_patch(cat_leg1)
ax.add_patch(cat_leg2)
ax.add_patch(cat_arm)

# 绘制哥斯拉吐出的蓝色光柱
ax.plot([0.35, 0.9], [0.75, 0.7], linewidth=5, color='blue')

# 配置轴
ax.axis('equal')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# 保存和显示图像
plt.savefig('godzilla_vs_cat_detailed.png')
plt.show()