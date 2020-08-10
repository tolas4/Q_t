import unittest
from BeautifulReport import BeautifulReport
from Common.func_address import cases_dir, reports_dir


cases = unittest.TestLoader().discover(cases_dir)
br = BeautifulReport(cases)
br.report("py30-注册用例自动化", "report_.html",reports_dir)