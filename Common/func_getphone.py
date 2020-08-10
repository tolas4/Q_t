import random
from Common.func_db import ConnDB
from Common.func_option import conf
from Common.func_requests import send_request


prefix = [133, 149, 153, 173, 177, 180, 181, 189, 199,
          130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 166,
          134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198
          ]


def get_newphone():
    global new_phone
    db = ConnDB()
    count = 1
    while count != 0:
        new_phone = __generator_phone()
        count = db.get_acount("SELECT * FROM member WHERE mobile_phone={}".format(new_phone))
    db.close_db()
    return new_phone


def __generator_phone():
    index = random.randint(0, len(prefix)-1)
    phone = str(prefix[index])
    for i in range(8):
        phone += str(random.randint(0,9))
    return phone


def get_old_phone():
    user = conf.get("generator", "base_phone")
    pwd =  conf.get("generator", "passwrd")
    send_request("post", "/member/register", {"mobile_phone":user,"pwd":pwd})
    return user, pwd

for i in range(4):
    a = get_newphone()
    print(a)