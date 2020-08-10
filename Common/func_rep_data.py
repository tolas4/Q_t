import re
from Common.func_option import conf


class EnvData:
    pass


def rep_data(case_data, mark, real_data):
    for key, value in case_data.items():
        if value is not None and isinstance(value, str):
            if value.find(mark) != -1:
                case_data[key] = value.replace(mark, real_data)
    return case_data


def req_data_by_re(data):
    res = re.findall("#(.*?)#", data)
    if res:
        for item in res:
            try:
                value = conf.get("re_data", item)
            except:
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    continue
            data = data.replace("#{}#".format(item), value)
    return data


if __name__ == '__main__':
    case = {
        "method": "POST",
        "url": "http://api.lemonban.com/futureloan/#phone#/member/register",
        "request_data": '{"mobile_phone": "#phone#", "pwd": "123456789", "type": 1, "reg_name": "美丽可爱的小简"}'
    }

    rep_data(case, "#phone#", "1234")
    print(case)