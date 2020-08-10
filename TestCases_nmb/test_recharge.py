import unittest
from Common.func_requests import send_request
from Common.func_getphone import get_old_phone
from jsonpath import jsonpath
from Common.func_logger import logger
from ddt import ddt, data
from Common.func_excel import Get_excel
from Common.func_address import nmb_dir
from Common.func_db import ConnDB
from Common.func_rep_data import rep_data, req_data_by_re
from Common.func_rep_data import EnvData
import json

sh_recharge = Get_excel(nmb_dir, "充值")
cases = sh_recharge.read_all_datas()
db = ConnDB()


@ddt
class TestRecharge(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        user, pwd = get_old_phone()
        response = send_request("post", "/member/login", {"mobile_phone":user, "pwd":pwd})
        setattr(EnvData, "member_id", jsonpath(response.json(), "$..id")[0])
        setattr(EnvData, "token", jsonpath(response.json(), "$..token")[0])
        # cls.member_id = jsonpath(response.json(), "$..id")[0]
        # cls.token = jsonpath(response.json(), "$..token")[0]
        pass

    @classmethod
    def tearDown(cls) -> None:
        pass

    def tearDownClass(self) -> None:
        pass

    @data(*cases)
    def test_recharge(self, case):
        if case["request_data"].find("member_id") != 1 and isinstance(case["request_data"], str):
            # case = rep_data(case, "#member_id#", str(EnvData.member_id))
            req_data_by_re(case["request_data"])

        if case["check_sql"]:
            old_money = float(db.select_one(case["check_sql"])["leave_amount"])
            recharge_money = json.loads(case["request_data"])["amount"]
            case = rep_data(case, "#money#", str(old_money+recharge_money))
        response1 = send_request(case["method"], case["url"], case["request_data"], token=EnvData.token)
        resp = response1.json()

        expect = eval(case["expected"])

        try:
            self.assertEqual(resp["code"], expect["code"])
            self.assertEqual(resp["msg"], expect["msg"])
            if case["check_sql"] is True:
                self.assertEqual(resp["data"]["leave_amount"], expect["data"]["leave_amount"])
        except AssertionError:
            raise

