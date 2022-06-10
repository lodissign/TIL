from turtle import color
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches    # 사각형 그리기 위해.

fig,ax=plt.subplots()   # 선 그리기 명령들 위에 있어야 함.

plt.hlines(500,0,500,color='blue')

redLine= plt.vlines(0,0,500)
plt.setp(redLine, color='r', linewidth=5.0)

ax.add_patch(
    patches.Rectangle(
        (100,100),
        300,300,
        edgecolor='deeppink',
        facecolor='lightgray',
        fill=True,
    )
)

# ax.add_patch(
#      patches.Polygon(
#         ((1.9, 4.0), (2.0, 2.5), (2.1, 4.0)),
#         closed=True,
#         edgecolor = 'deeppink',
#         facecolor = 'lightgray'
#      ))

plt.axis('off')
plt.show()