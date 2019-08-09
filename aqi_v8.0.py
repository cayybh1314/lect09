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
    version:8.0
"""

##导包
import requests
from bs4 import BeautifulSoup
import json
import csv
import os

def get_city_aqi(city_pinyin):
    """
        获取诚实的AQI
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append(value)  ##只获取value
    return city_aqi

def get_all_cities():
    """
        获取所有城市
    """
    url = 'http://pm25.in/'
    city_list = []
    r = requests.get(url, timeout = 30)##使用get方法打开URL，超时时间30

    ##创建beautifulsoup对象
    soup = BeautifulSoup(r.text, 'lxml')##r.text爬虫获取的文本，lxml是解析器

    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')

    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    """
        主函数
    """
    ##获取城市列表
    city_list = get_all_cities()
    # for city in city_list:
    #     city_name = city[0]
    #     city_pinyin = city[1]
    #     city_aqi = get_city_aqi(city_pinyin)
    #     print(city_name, city_aqi)
    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']

    with open('China_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)##先写入第一行，标题
        for i, city in enumerate(city_list):
            if (i + 1) %10 ==0:
                print('已处理{}条记录。(共{}条记录)'.format(i + 1, len(city_list)))
            city_name = city[0]
            city_pinyin = city[1]
            city_aqi = get_city_aqi(city_pinyin)
            row = [city_name] + city_aqi
            writer.writerow(row)


if __name__ == '__main__':
    main()
