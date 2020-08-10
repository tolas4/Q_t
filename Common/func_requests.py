from Common.func_logger import logger
from Common.func_option import conf
import requests
import json


def __set_headers_ats():
    headers = {
        "Cookie": "atst=BUjVSQ1FkUWtVZVQyCj9cNgEyAjU.",
        "Content-Type": "application/x-www-form-urlencoded"
        }
    return headers


def __set_headers_nmb(token=None):
    headers = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "Content-Type": "application/json"
        }
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def send_request(method, url, data=None, token=None):
    # global resp
    headers = __set_headers_nmb(token)
    logger.info("**********发送一次http请求**********")
    logger.info("请求头是：{}".format(headers))
    logger.info("请求方法：{}".format(method))
    logger.info("请求地址：{}".format(url))
    logger.info("请求数据：{}".format(data))

    url = __request_url(url)
    data = __request_data(data)
    method = method.upper()
    if method == "GET":
        resp = requests.get(url, data, headers=headers)
    elif method == "POST":
        resp = requests.post(url, json=data, headers=headers)

    logger.info("响应状态码为：{}".format(resp.status_code))
    logger.info("响应数据为：{}".format(resp.json()))

    return resp


def __request_data(data):
    if data is not None and isinstance(data, str):
        return json.loads(data)
    else:
        return data

def __request_url(url):
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url


if __name__ == '__main__':
    login_url = "/member/register"
    login_datas = {"mobile_phone": "13845467785", "pwd": "1234567890"}
    resp = send_request("POST",login_url,data=login_datas)
    # token = resp.json()["data"]["token_info"]["token"]

    # recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    # recharge_data = {"member_id": 200119, "amount": 2000}
    # resp = send_request("POST",recharge_url,recharge_data,token)
    print(resp.json())