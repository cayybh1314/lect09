"""
    测试
"""
import requests

def main():
    """
        主函数
    """
    url = 'http://pm25.in/'
    r = requests.get(url, timeout=30)
    print(r.text)



if __name__ == '__main__':
    main()
