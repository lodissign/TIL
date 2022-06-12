from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches    # 사각형 그리기 위해.

# plt.rcParams['figure.figsize'] = (6, 6)

fig,ax=plt.subplots()

plt.plot([0,10], [5,10])

ax.add_patch(
    patches.Rectangle(
        (0,5),
        5,5,
        edgecolor='deeppink',
        # facecolor='lightgray',
        fill=False,
    )
)

# plt.axis('off')
plt.show()