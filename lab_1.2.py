num = [5, 4, 3, 6, 3, 5, 2, 4, 1, 7, 7, 6]

arr = [0] * 200

ans = []

for i in num:
    if arr[i] == 0:
        ans.append(i)
        arr[i] = 1

print("after remove duplicates:", ans)
