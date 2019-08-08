"""
    author:zqc
    date:20190808
    feature:AQI计算
    feature:JSON
    version:2.0
"""

##导包
import json

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
    top5_list = city_list[:5]

    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()

if __name__ == '__main__':
    main()
