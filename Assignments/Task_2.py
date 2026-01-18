list = [1,2,7,"ram","josh",2,3,"jack",4,4,"ram","smith"]
res = []

for ele in list:
    if ele not in res:
        res.append(ele)

print(res)