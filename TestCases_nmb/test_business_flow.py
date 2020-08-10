import unittest
from Common.func_excel import Get_excel
from Common.func_requests import send_request
from Common.func_address import nmb_dir
from Common.func_option import conf
from Common.func_getphone import get_newphone
from Common.func_rep_data import EnvData, req_data_by_re
from ddt import ddt, data


sh = Get_excel(nmb_dir, "业务流")
cases = sh.read_all_datas()


@ddt
class TestBusiness(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        pwd = conf.get("generator", "passwrd")
        phone = get_newphone()
        setattr(EnvData, "mobile_phone", phone)
        setattr(EnvData, "pwd", pwd)


    data(*cases)
    def test_bus(self, case):
        if
        response = send_request(case["method"], case["url"], case["request_data"])
        resp = response.json()
        if