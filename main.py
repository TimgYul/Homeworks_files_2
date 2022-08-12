# with open('1.txt' , 'r', encoding='utf-8' ) as f1:

def write_file(a,b,c,d):
    with open(a, 'r', encoding='utf-8' ) as f1:
        content1 = f1.read() + '\n'
    with open(b, 'r', encoding='utf-8') as f2:
        content2 = f2.read() + '\n'
    with open(c, 'r', encoding='utf-8') as f3:
        content3 = f3.read() + '\n'

    with open(d, 'w', encoding='utf-8' ) as f4:
        f4.write(content1)
        f4.write(content2)
        f4.write(content3)


line_count_1 = sum (1 for line1 in open('1.txt' , 'r', encoding='utf-8' ) if line1.rstrip('\n'))
line_count_2 = sum (1 for line2 in open('2.txt' , 'r', encoding='utf-8' ) if line2.rstrip('\n'))
line_count_3 = sum (1 for line3 in open('3.txt' , 'r', encoding='utf-8' ) if line3.rstrip('\n'))
# print(line_count_1)
# print(line_count_2)
# print(line_count_3)
dict_count = {}
dict_count[ line_count_1] = '1.txt'
dict_count[ line_count_2] = '2.txt'
dict_count[ line_count_3] = '3.txt'
sort_dict_count = dict(sorted(dict_count.items()))
print(sort_dict_count)

min_f = list(sort_dict_count.values())[0]
aver_f = list(sort_dict_count.values())[1]
max_f = list(sort_dict_count.values())[2]
write_file(min_f,aver_f,max_f,'res.txt')

with open('res.txt', 'r', encoding='utf-8') as result:
    result_content = result.read()
    print(result_content)
