import getpass
import hashlib

#出入隐藏
pwd = getpass.getpass()


# #hash对象
# hash = hashlib.md5()

#算法加盐
hash = hashlib.md5("**6*#".encode())
hash.updata(pwd.encode())
pwd = hash.hexdigest()
