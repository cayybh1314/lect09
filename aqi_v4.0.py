"""
    author:zqc
    date:20190808
    1.0 feature:AQI计算
    2.0 feature:JSON
    3.0 feature:csv
    4.0 feature:根据csv或者json后缀判断，并进行相应操作
    version:4.0
"""

##导包
import json
import csv
import os


##csv文件处理函数
def csv_process_file(filepath):
    """

    :param filepath: filepath
    :return: csv file process result
    """
    with open(filepath, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print('+'.join(row))

##json文件处理函数
def json_process_file(filepath):
    """
        process json files;
    """
    # f = open(filepath, mode='r', encoding='utf-8')
    # city_list = json.load(f)
    # f.close()
    # return city_list

    with open(filepath, mode='r', encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)


def main():
    """
        主函数
    """
    ##输入
    filepath = input('请输入文件名称:')
    filename, file_ext = os.path.splitext(filepath)

    ##判断文件类型
    if file_ext == '.json':
        ##处理json文件
        json_process_file(filepath)
    elif file_ext == '.csv':
        ##处理csv文件
        csv_process_file(filepath)
    else:
        print('不支持的文件类型:{}'.format(file_ext))


if __name__ == '__main__':
    main()
