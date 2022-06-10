from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches    # 사각형 그리기 위해.

plt.style.use('default')
plt.rcParams['figure.figsize'] = (10, 20)

fig,ax=plt.subplots()

# plt.hlines(500,0,500,color='blue')

# redLine= plt.vlines(0,0,500)
# plt.setp(redLine, color='r', linewidth=5.0)

ax.add_patch(
    patches.Rectangle(
        (100,100),
        300,300,
        edgecolor='deeppink',
        # facecolor='lightgray',
        fill=False,
    )
)

# plt.axis('off')
plt.show()