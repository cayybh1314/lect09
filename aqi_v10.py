"""
    author:zqc
    date:201908012
    version:10.0 数据清洗
"""

##导入包
import pandas as pd
import matplotlib.pyplot as plt

##处理字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('China_city_aqi.csv')
    # print(aqi_data.head(5)) ##前五行
    # print(aqi_data[['City','AQI']])##数据显示两列
    # sort_value = aqi_data.sort_values(by = 'AQI')##数据根据AQI排序
    print('基本信息:')
    print(aqi_data.info())
    print('数据预览:')
    print(aqi_data.head(5))

    ##数据清洗
    #只保留AQI大于0的数据
    # filter_condition  = aqi_data['AQI'] > 0  #过滤策略
    # clean_aqi_data = aqi_data[filter_condition] ##清洗过后的数据
    ##改写后的数据清洗
    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    ###基本统计
    # print('AQI最大值', clean_aqi_data['AQI'].max())
    # print('AQI最小值：', clean_aqi_data['AQI'].min())
    # print('AQI均值：', clean_aqi_data['AQI'].mean())

    # top10
    top50_cities = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI', title='空气质量最好的的50个城市', figsize=(20,10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()

    # bottom10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    # bottom10_cities = clean_aqi_data.sort_values(by=['AQI'], ascending=False).head(50)
    # print('空气质量最差的10个城市：')
    # print(bottom10_cities)

    # 保存csv文件
    # top10_cities.to_csv('top10_aqi.csv', index=False)
    # bottom10_cities.to_csv('bottom10_aqi.csv', index=False)



if __name__ == '__main__':
    main()
