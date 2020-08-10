import unittest
from ddt import ddt,data
from Common.func_excel import Get_excel
from Common.func_address import excel_dir
from Common.func_requests import send_request

# from Common.func_logger import logger
# import requests
# import os
# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, "Data/ats_cases.xlsx")
# titles = sh.read_titles()
# headers = {
#     "Cookie": "atst=BUjVSQ1FkUWtVZVQyCj9cNgEyAjU.",
#     "Content-Type": "application/x-www-form-urlencoded"
#     }

sh = Get_excel(excel_dir, "sheet1")
cases = sh.read_all_datas()


@ddt
class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def setUp(cls) -> None:
        pass

    @data(*cases)
    def test_write_user(self, case):
        response = send_request(case["method"], case["url"], data=case["request_data"])
        print(response.json())
        self.assertEqual(1, 1)