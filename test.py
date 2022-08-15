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