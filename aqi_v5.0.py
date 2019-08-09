"""
    author:zqc
    date:20190808
    1.0 feature:AQI计算
    2.0 feature:JSON
    3.0 feature:csv
    4.0 feature:根据csv或者json后缀判断，并进行相应操作
    5.0 feature:新增网络爬虫
    version:5.0
"""

##导包
import requests

def get_html_text(url):
    """
        获取返回url的文本
    """
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_name = input('输入诚实名称(拼音):')
    url = 'http://pm25.in/' + city_name
    url_text = get_html_text(url)

    ##解析文本
    aqi_div = '''    <div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div) ##获取文本开始的index值
    begin_index = index + len(aqi_div)
    end_index = index + 2
    aqi_val = url_text[begin_index: end_index]
    print(aqi_val)

if __name__ == '__main__':
    main()
