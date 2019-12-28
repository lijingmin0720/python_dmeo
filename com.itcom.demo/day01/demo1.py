import math


# 练习1：华氏温度转换为摄氏温度。
# 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

def transferFC():
    f = float(input('请输入华氏温度：'))
    c = (f - 32) / 1.8
    print('%.1f华氏度 = %.1f摄氏度' % (f, c))


# 练习2：输入圆的半径计算计算周长和面积。
def cultPerimeter():
    radius = float(input('请输入圆半径：'))
    perimeter = 2 + math.pi * radius
    area = math.pi * radius * radius
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)


# 练习3：百分制成绩转换为等级制成绩。
# 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。

def cultScore():
    score = float(input('请输入分数：'))
    if score >= 90:
        print('A')
    elif 80 <= score < 90:
        print('B')
    elif 70 <= score < 80:
        print('C')
    elif 60 <= score < 70:
        print('D')
    elif score < 60:
        print('E')


if __name__ == '__main__':
    # transferFC()
    # cultPerimeter()
    cultScore()