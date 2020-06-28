import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing

# 数据加载
data = pd.read_csv('D:\Data Analysis SVW L3\L3\car_data.csv',encoding="gbk")
train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数", "百户拥有汽车量"]]
# print( train_x)

#数据规范化:最小最大值标准化
min_max_scaler=preprocessing.MinMaxScaler()
train_x_processed=min_max_scaler.fit_transform(train_x)
# print(train_x_processed)

# K-Means 手肘法：统计不同K取值的误差平方和
import matplotlib.pyplot as plt
sse = []
for k in range(1, 11):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x_processed)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()
#根据曲线，选定分组数为5


# 使用KMeans聚类
kmeans = KMeans(n_clusters=5,max_iter=300)
kmeans.fit(train_x_processed)
predict_y = kmeans.predict(train_x_processed)

# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
print(result)

# 将结果导出到CSV文件中
result.rename({0: u"聚类结果"}, axis=1, inplace=True)
result.to_csv("D:\Data Analysis SVW L3\L3\City_classification_result.csv", index=False)