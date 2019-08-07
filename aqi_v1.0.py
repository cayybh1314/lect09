"""
    author:zqc
    date:20190807
    feature:AQI计算
    version:1.0
"""

def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
      缩放范围,现行转化
    :return:
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi

def cal_pm_iaqi(pm_val):
    """

    :param pm_val: pm2.5 value
    :return: pm2.5 IAQI
    """
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    else:
        print('PM2.5浓度值为:{},浓度值过高,药丸!!!!'.format(pm_val))


def cal_co_iaqi(co_val):
    """

    :param co_val: co value
    :return: co IAQI
    """
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    else:
        print('二氧化碳浓度值为:{},浓度值过高，药丸!!!!'.format(co_val))


def cal_aqi(param_list):
    """
        AQI计算
    :param param_list: 传入的参数
    :return: 返回值
    """
    ##传入pm和co的值
    pm_val = param_list[0]
    co_val = param_list[1]

    ##计算pm和co的空气质量分指数
    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    ##构造iaqi列表，临时存储co和pm的空气质量分指数
    iqai_list = []
    iqai_list.append(pm_iaqi)
    iqai_list.append(co_iaqi)

    ##计算空气质量指数
    aqi = max(iqai_list)
    return aqi


def main():
    """
        主函数
    """
    print('请输入以下信息，用空格分割')
    input_str = input('(1)PM2,5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    ##构造列表，放入值
    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    ##调用AQI计算函数
    aqi_val = cal_aqi(param_list)

    ##输出aqi计算值
    print('空气质量直属为:{}'.format(aqi_val))


if __name__ == '__main__':
    main()
