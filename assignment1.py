results = [['EAE', 'BCA', 85], ['EEE', 'BDB', 17], ['EAD', 'ECD', 21],
['ECA', 'CDE', 13], ['CDA', 'ABA', 76], ['BEA', 'CEC', 79],
['EAE', 'CED', 8], ['CBE', 'CEA', 68], ['CDA', 'CEA', 58],
['ACE', 'DEE', 24], ['DDC', 'DCA', 61], ['CDE', 'BDE', 67],
['DED', 'EDD', 83], ['ABC', 'CAB', 54], ['AAB', 'BDB', 15],
['BBE', 'EAD', 28], ['ACD', 'DCD', 50], ['DEB', 'CAA', 21],
['EBE', 'AAC', 24], ['EBD', 'BCD', 48]]

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
def counting_sort(list,place_value):
    length = len(list) 
    count = [0]*10
    position = [0]*10
    output = [0]*length

    for i in range(0,length):
        val = (list[i][2]//place_value)%10
        count[val] += 1
    for i in range(1,10):
        position[i] = position[i-1] + count[i-1]
    for i in range(length):
        val = (list[i][2]//place_value)%10
        output[position[val]] = list[i]
        position[val]+=1
    for i in range(0,length):
        list[i] = output[i]
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
def counting_sort_str(list):
    count = [0] * 90
    return "chode"
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
def analyze(results:list, roster, score):
    res_len = len(results)
    for i in range(res_len):
        results.append(results[i])
    for i in range(res_len):
        results[i] = [results[i][1],results[i][0], 100-results[i][2]]
    radix_sort(results)
    top_10_matches = []
    for i in range(0,10):
        top_10_matches.append(results[i])
