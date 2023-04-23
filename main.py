a = 'aaaabbcaa'
count_1 = 1
result = ''
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count_1 += 1
    else:
        result += a[i] + str(count_1)
        count_1 = 1
result += a[-1] + str(count_1)
print(result)


# while i < (len(a) - 1):
#     if a[i] == a[i+1]:
#         k = k + 1
#     else:
#         res = res + a[i] + str(k)
#         k = 1
#     i = i + 1
# print(res + a[i] + str(k))








