#======================================================
# n진수 -> 10진수
# int() 함수 이용 -> int(string, base)
# print(int('111', 2))
# print(int('222', 3))
# print(int('FFF', 16))


#========================================================
# 10진수 -> n진수
import string
tmp = string.digits + string.ascii_lowercase
# 16진수 까지일경우는
# tmp = "0123456789ABCDEF" 로 써도 된다.
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]
