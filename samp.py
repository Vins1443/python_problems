lis=['apple 25','mango 35','grape 20']
list_2 =['apple 2','mango 3', 'grape 6']

lis_dic = {item.split()[0]: int(item.split()[1]) for item in lis}
print(lis_dic)

lis_dic_price = {item.split()[0]: int(item.split()[1]) for item in list_2}
print(lis_dic_price)

final_price = {}
for key in lis_dic:
    if key in lis_dic_price:
        final_price[key] = lis_dic[key] * lis_dic_price[key]
        
print(final_price)
        
file_path = 'C:/Users/vsj14/Desktop/sample.txt'

with open(file_path, 'r') as file:
    contents = file.read()
    print(contents)


with open('C:/Users/vsj14/Desktop/newfile.txt', 'w') as file:
    file.write("Hello, world!")    


class Cat:
    pass
cat = Cat()
print(cat)  


my_dict = {"apple": 25, "mango": 35, "grape": 20}

keys_list = list(my_dict.keys())

print(keys_list)




