"""
    author:zqc
    date:20190809
    1.0 feature:AQI计算
    2.0 feature:JSON
    3.0 feature:csv
    4.0 feature:根据csv或者json后缀判断，并进行相应操作
    5.0 feature:新增网络爬虫
    6.0 feature: 使用beautifulsoup处理获取的文件。
    version:6.0
"""

##导包
import requests
from bs4 import BeautifulSoup

def get_city_aqi(city_name):
    """
        获取诚实的AQI
    """
    url = 'http://pm25.in/' + city_name
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
        主函数
    """
    city_name = input('输入诚实名称(拼音):')
    city_aqi = get_city_aqi(city_name)
    print(city_aqi)

if __name__ == '__main__':
    main()
