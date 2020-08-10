import unittest
from Common.func_excel import Get_excel
from Common.func_address import nmb_dir
from Common.func_logger import logger
from ddt import ddt, data
from Common.func_requests import send_request
from Common.func_rep_data import rep_data
from Common.func_getphone import get_newphone
import json
from Common.func_db import ConnDB


sh = Get_excel(nmb_dir, "注册")
cases = sh.read_all_datas()
db = ConnDB()

@ddt
class TestNmbRegister(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        logger.info("*******柠檬班注册用例开始执行*******")

    @classmethod
    def tearDown(self) -> None:
        logger.info("*******柠檬班注册用例执行结束*******")

    @data(*cases)
    def test_register(self, case):
        logger.info("*********执行用例 {}:{} **************".format(case["id"], case["title"]))
        if case["request_data"].find("#phone#") != -1:
            phone = get_newphone()
            case= rep_data(case, "#phone#", phone)
        resp = send_request(case["method"], case["url"], case["request_data"])
        expected = eval(case["expected"])
        resp = resp.json()

        try:
            self.assertEqual(resp["code"], expected["code"])
            self.assertEqual(resp["msg"], expected["msg"])
            if case["check_sql"]:
                result = db.select_one(case["check_sql"])
                self.assertIsNotNone(result)
        except AssertionError:
            raise