from random import choice
import matplotlib.pyplot as plt

#设定一个随机漫步类，拥有散点数，起始位置属性
class RandomWalk():
    def __init__(self, num_points=5000):
         self.num_points = num_points
         self.x_value = [0]
         self.y_value = [0]

    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            #步数等于方向乘以步长
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance
            #放置原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #下一步等于现在位置，加下一步
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            #附加到列表中
            self.x_value.append(next_x)
            self.y_value.append(next_y)


while True:
    rw = RandomWalk()
    rw.fill_walk()
    #调整图像尺寸
    plt.figure(figsize=(10,6),dpi=100)
    #开始漫步
    plt.scatter(rw.x_value, rw.y_value, s=1,c=list(range(rw.num_points)),cmap=plt.cm.Blues)
    #设置起点
    plt.scatter(0,0,c="green",edgecolors="none",s=10)
    #设置终点
    plt.scatter(rw.x_value[-1],rw.y_value[-1],c="red",edgecolors="none",s=10)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #开始展示
    plt.show()
    #判断是否再次随机漫步
    keep_running = input("play again?(Y/N)")
    if keep_running == "n"or"N":
        break