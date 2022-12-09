import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage import color


image = plt.imread("C:\\Users\\mano4ka\\Desktop\\python\\balls_and_rects.png")

hsv = color.rgb2hsv(image)
binary = hsv[:,:,0].copy()
binary[binary > 0] = 1

labeled = label(binary)
regions = regionprops(labeled)

colors = []
for reg in regions:
    cy, cx = reg.centroid
    colors.append(hsv[int(cy), int(cx), 0])
colors = sorted(colors)   

balls = []
rectan = []
for reg in regions:# круг квадрат
    if np.mean(reg.image) == 1:
        balls.append(reg)
    else:
        rectan.append(reg)

def colorss(colors):
    #пара, группы оттенков
    groups = [[colors[0]],]
    delta = np.mean(np.diff(colors))
    for i in range(1, len(colors)):
        previous = colors[i-1]
        current = colors[i]
        if current - previous > delta:
            groups.append([])
        groups[-1].append(current) 
    return groups

cballs = []
crectan = []
for reg in regions:
    cy, cx = reg.centroid
    col = hsv[int(cy), int(cx)][0]
    if reg in balls:
        cballs.append(col)
    else:
        crectan.append(col)

#resultColors = []
#resultCount = []
#for grp in groups:
#    resultCount.append(len(grp))
#    resultColors.append(np.mean(grp))

result_b = {}
result_r = {}
for grp in colorss(sorted(cballs)):
    result_b[len(grp)] = [np.mean(grp)]
for grp in colorss(sorted(crectan)):
    result_r[len(grp)] = [np.mean(grp)]

print('Всего объектов:')
print(np.max(labeled))
print('Круги:')
print(result_b)
print('Прямоугольники:')
print(*result_r)
#print('Circle:', sum(resultCount))   
#print(resultCount)

plt.imshow(labeled)
plt.show()