S02 = set()
S02 = input("Nhâp họ: ")

print(S02, 'co do dai la', len(S02))
S02 = set()
S02 = input("Nhâp tên đệm: ")

print(S02, 'co do dai la', len(S02))
S02 = set()
S02 = input("Nhâp tên: ")

print(S02, 'co do dai la', len(S02))
def isThuanNghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;


n = int(input("Nhập số nguyên dương n = "));
m = int(input("Nhập số nguyên dương m = "));
print("Tổng các chữ số của", m, "là", isThuanNghich(m));
print("Tổng các chữ số của", n, "là", isThuanNghich(n));
