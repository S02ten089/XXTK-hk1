S02 = set()
S02 = set()
def totalDigitsOfNumber(n):

    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;

S02 = input("Nhập tên đệm: ")
print(S02, 'co do dai la', len(S02))
S02 = input("Nhập tên: ")
print(S02, 'co do dai la', len(S02))
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n));

