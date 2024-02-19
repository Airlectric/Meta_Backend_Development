num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for id, num in enumerate(num_list):
    count+=1
    if num == 36:
        print("Number found at position",id)
        break
    else:
        print(id,'Under 45')

print(count)
