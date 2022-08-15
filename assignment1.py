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
def counting_sort(list,place):
    length = len(list) 
    output = [0]*length
    count = [0]*10

    for i in range(0,length):
        val = (list[i][2]//place)%10
        count[val] += 1
    for i in range(1,10):
        count[i]+=count[i-1]
    for i in range(length-1,-1,-1):
        val = (list[i][2]//place)%10
        output[count[val]-1] = list[i]
        count[val] -= 1
    for i in range(0,length):
        list[i] = output[i]

def radix_sort(list):
    place = 1
    scores = []
    for i in range(len(list)):
        scores.append(list[i][2])
    max_score = max(scores)

    while max_score // place > 0:
        counting_sort(list,place)
        place*=10

radix_sort(results)
print(results)
#def analyze(results, roster, score):