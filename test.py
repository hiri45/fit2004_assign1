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

#nums = [[3,'a'],[1,'p'],[3,'c'],[7,'f'],[5,'g'],[3,'b'],[7,'d'],[8,'w']]
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
#radix_sort(results)
#print(results)
str_exam = "BBA"
def counting_sort_str(string,roster):
    #roster = len(string)
    count = [0]*90
    position = [0] * 90
    output = [0] * roster
    for i in string:
        count[ord(i)] += 1
    for i in range(1,90):
        position[i] = position[i-1] + count[i-1]
    for i in range(roster):
        output[position[ord(string[i])]] = string[i]
        position[ord(string[i])] += 1
    updated_string = ''
    for i in output:
        updated_string+=i
    string = updated_string
    return string
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
#now = counting_sort_str(str_exam)
#print(now)
"""def counting_sort_letters(list,place):
    length = len(list)
    count = [0]*90
    position = [0] * 90
    output = [0] * length
    strings = []
    for i in range(length):
        strings.append(list[i][place])
    for i in range(1,90):
        position[i] = position[i-1] + count[i-1]
    for i in range(length):
        output[position[ord(list[i][place])]] = list[i][place]
        position[ord(list[i][place])] += 1
    #updated_string = ''
    #for i in output:
        #updated_string+=i
    #list[] = """
#str_exam = counting_sort_str(str_exam)
#print(str_exam)
#results[0][0] = counting_sort_str(results[0][0])
#print(results)
#for i in range(len(results)):
#    results[i][0] = counting_sort_str(results[i][0])
#for i in range(len(results)):
#    results[i][1] = counting_sort_str(results[i][1])
#print(results)
length = len(results)
top_10_matches = []
#for i in range(length-1,length-11,-1):
    #print(results[i])
if length<10:
    top_10_matches.append(results)
else:
    iter = length-1
    while len(top_10_matches)<10:
        top_10_matches.append(results[iter])
        iter -= 1
#print(top_10_matches)
score = 21
searched_matchess = []
for i in range(length):
    if results[i][2] == score:
        searched_matchess.append(results[i])
iters = 0
if len(searched_matchess) == 0:
    while results[iters][2] < score:
        iters += 1
    for i in range(length):
        if results[i][2] == results[iters][2]:
            searched_matchess.append(results[i])
if length//2 < 10:
    searched_matchess.append(results)
#print(searched_matchess)
#top_10_matches.append(searched_matches)
resultsss = [['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
['ABB', 'BBB', 68], ['BAB', 'BBB', 52]]

updated = []

def analysis(results,score,roster):
    reverse_result = []
    for i in range(len(results)):
        reverse_result.append(results[i])
    for i in range(len(results)):
        reverse_result[i] = [reverse_result[i][1],reverse_result[i][0],100-reverse_result[i][2]]
    results += reverse_result
    radix_sort(results)
    for i in range(len(results)):
        results[i][0] = counting_sort_str(results[i][0],roster)
    for i in range(len(results)):
        results[i][1] = counting_sort_str(results[i][1],roster)
    top_10_matches = []
    if len(results)<10:
        top_10_matches.append(results)
    else:
        iter_top_10 = len(results)-1
        while len(top_10_matches)<10:
            top_10_matches.append(results[iter_top_10])
            iter_top_10 -= 1
    searched_matches = []
    for i in range(len(results)):
        if results[i][2] == score:
            searched_matches.append(results[i])
    if len(searched_matches) == 0:
        #iters = 0
        #while results[iters][2] < score:
            #iters += 1
        #for i in range(len(results)):
            #if results[i][2] == results[iters][2]:
                #searched_matches.append(results[i])
        scores_greater = []
        for i in range(len(results)):
            if results[i][2] > score:
                scores_greater.append(results[i])
        for i in range(len(scores_greater)):
            if scores_greater[i][2] == scores_greater[0][2]:
                searched_matches.append(scores_greater[i])
    if len(results)//2 < 10:
        searched_matches.append(results)
    print(top_10_matches)
    print(searched_matches)
analysis(resultsss,71,3)
#print(radix_sort(resultsss))\
print(45//1)