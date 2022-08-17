"""
High level description about the function and the approach you
have undertaken.
:Input:
argv1:
argv2:
:Output, return or postcondition:
:Time complexity:
:Aux space complexity:
"""
results = [['EAE', 'BCA', 85], ['EEE', 'BDB', 17], ['EAD', 'ECD', 21],
['ECA', 'CDE', 13], ['CDA', 'ABA', 76], ['BEA', 'CEC', 79],
['EAE', 'CED', 8], ['CBE', 'CEA', 68], ['CDA', 'CEA', 58],
['ACE', 'DEE', 24], ['DDC', 'DCA', 61], ['CDE', 'BDE', 67],
['DED', 'EDD', 83], ['ABC', 'CAB', 54], ['AAB', 'BDB', 15],
['BBE', 'EAD', 28], ['ACD', 'DCD', 50], ['DEB', 'CAA', 21],
['EBE', 'AAC', 24], ['EBD', 'BCD', 48]]
def counting_sort(list,place_value):
    length = len(list) 
    output = [0]*length
    count = [0]*10
    position = [0]*10

    for i in range(0,length):
        val = (list[i][2]//place_value)%10
        count[val] += 1
    for i in range(1,10):
        position[i] = position[i-1] + count[i-1]
    for i in range(length):
        val = (list[i][2]//place_value)%10
        output[position[val]] = list[i]
        position[val] += 1
    for i in range(0,length):
        list[i] = output[i]

def radix_sort(list):
    place_value = 1
    scores = []
    for i in range(len(list)):
        scores.append(list[i][2])
    max_score = max(scores)

    while max_score // place_value > 0:
        counting_sort(list,place_value)
        place_value = place_value*10

radix_sort(results)
print(results)
nums = [[3,'a'],[1,'p'],[3,'c'],[7,'f'],[5,'g'],[3,'b'],[7,'d'],[8,'w']]
#print(len(nums))
#print(nums[7])
#counting_sort(nums,1)
#print(nums)
print(3%10)
#results[0] += [results[0][1],results[0][0], 100-results[0][2]]
#print(results)
#print(100-results[0][2])
res_len = len(results)
for i in range(res_len):
    results.append(results[i])
for i in range(res_len):
    results[i] = [results[i][1],results[i][0], 100-results[i][2]]
print(results)
str_exam = "BBA"
def counting_sort_str(string):
    length = len(string)
    count = [0]*90
    position = [0] * 90
    output = [0] * length
    for i in string:
        count[ord(i)] += 1
    for i in range(1,90):
        position[i] = position[i-1] + count[i-1]
    for i in range(length):
        output[position[ord(string[i])]] = string[i]
        position[ord(string[i])] += 1
    updated_string = ''
    for i in output:
        updated_string+=i
    string = updated_string
        
"""lists = []
for letter in str_exam:
    lists.append(letter)
print(lists)
lists[0] = "Z"
print(lists)"""
"""exam = ['A','B','C']
str = ""
for i in exam:
    str+=i
print(str)
str_exam = str
print(str_exam)"""
now = counting_sort_str(str_exam)
print(now)