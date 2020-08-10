from openpyxl import load_workbook
import os
# import json

class Get_excel(object):
    def __init__(self, file_name, sheetname):
        self.wb = load_workbook(file_name)
        self.sh = self.wb[sheetname]

    def read_titles(self):
        titles = []
        # print(type(self.sh.rows))
        for item in list(self.sh.rows)[0]:
            titles.append(item.value)
        return titles

    def read_all_datas(self):
        titles = self.read_titles()
        all_datas = []
        for item in list(self.sh.rows)[1:]:
            datas = []
            for val in item:
                datas.append(val.value)
            case_dic = dict(zip(titles, datas))
            # case_dic["request_data"] = json.loads(case_dic["request_data"])
            all_datas.append(case_dic)
        return all_datas


if __name__ == '__main__':
    import os
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir,"Data/ats_cases.xlsx")
    sh = Get_excel(file_path, "sheet1")
    titles = sh.read_titles()
    datas = sh.read_all_datas()
    print(datas)
    pass