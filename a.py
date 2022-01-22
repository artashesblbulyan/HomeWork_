# # a = "artash"
# # b = dict()
# # print(b)
import random

k = random.randrange(1023, 9999)
# print(k)
# c = 0

k = set(str(k))
print(len(k))
while len(k) < 4:
    k = random.randrange(1023, 9999)
    k = set(str(k))
else:
    k = "".join(k)
    print(k)


# for i in range(1000, 9999):
#     # list_1.append(i)
#     k = 0

#     for j in str(i):
#         if str(i).count(j) > 1:
#             i += 1
#         else:
#             print(i)
