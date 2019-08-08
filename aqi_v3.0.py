"""
    author:zqc
    date:20190808
    1.0 feature:AQI计算
    2.0 feature:JSON
    3.0 feature:csv
    version:3.0
"""

##导包
import json
import csv


##json文件处理函数
def json_process_file(filepath):
    """
        process json files;
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    f.close()
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称:')
    city_list = json_process_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])

    # 构造一个空列表
    lines = []

    ##处理列名
    lines.append(list(city_list[0].keys()))
    ##循环遍历values
    for city in city_list:
        lines.append(list(city.values()))
        print(lines)

    f = open('aqi.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
