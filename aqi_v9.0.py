"""
    author:zqc
    date:20190809
    1.0 feature:AQI计算
    2.0 feature:JSON
    3.0 feature:csv
    4.0 feature:根据csv或者json后缀判断，并进行相应操作
    5.0 feature:新增网络爬虫
    6.0 feature: 使用beautifulsoup处理获取的文件。
    7.0 feature: 新增获取所有城市列表
    8.0 feature: 将获取到的数据存储到csv文件
    8.0 feature: 导入pandas
    version:9.0
"""

##导包
import requests
from bs4 import BeautifulSoup
import json
import csv
import os
import pandas as pd

def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('China_city_aqi.csv')
    # print(aqi_data.head(5)) ##前五行
    # print(aqi_data[['City','AQI']])##数据显示两列
    # sort_value = aqi_data.sort_values(by = 'AQI')##数据根据AQI排序
    # print('基本信息:')
    # print(aqi_data.info())
    # print('数据预览:')
    # print(aqi_data.head(5))

    ###基本统计
    print('AQI最大值', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI均值：', aqi_data['AQI'].mean())

    # top10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的10个城市：')
    print(top10_cities)

    # bottom10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的10个城市：')
    print(bottom10_cities)

    # 保存csv文件
    top10_cities.to_csv('top10_aqi.csv', index=False)
    bottom10_cities.to_csv('bottom10_aqi.csv', index=False)

if __name__ == '__main__':
    main()
