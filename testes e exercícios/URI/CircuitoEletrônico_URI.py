x = int(input())
BinX = []
newX = []
aux = 0

while x != 0:
    x = x / 2
    if x % 2 == 0:
        BinX.append(0)
    if x % 2 == 1:
        BinX.append(1)

# for i in range(0, 4):
#     if newX[i] % 2 == 0:
#         BinX.append(0)
#     if newX[i] % 1 == 0:
#         BinX.append(1)

# print(newX)
print(BinX)
