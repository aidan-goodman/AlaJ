import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 创建折线图
plt.plot(x, y, marker="o", linestyle="-", color="b", label="示例数据")

# 添加标题和标签
plt.xlabel("time")
plt.ylabel("value")

# 显示图表
plt.show()
