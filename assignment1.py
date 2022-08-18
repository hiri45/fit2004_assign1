results = [['EAE', 'BCA', 85], ['EEE', 'BDB', 17], ['EAD', 'ECD', 21],
['ECA', 'CDE', 13], ['CDA', 'ABA', 76], ['BEA', 'CEC', 79],
['EAE', 'CED', 8], ['CBE', 'CEA', 68], ['CDA', 'CEA', 58],
['ACE', 'DEE', 24], ['DDC', 'DCA', 61], ['CDE', 'BDE', 67],
['DED', 'EDD', 83], ['ABC', 'CAB', 54], ['AAB', 'BDB', 15],
['BBE', 'EAD', 28], ['ACD', 'DCD', 50], ['DEB', 'CAA', 21],
['EBE', 'AAC', 24], ['EBD', 'BCD', 48],['EBD', 'BCD', 100]]

"""
counting_sort is a function for integers. This function is an algorithm which sorts the integers in increasing order from lowest to highest
:Input: 
argv1: list
argv2: place_value
:Output, return or postcondition: the output from using this function is the input, in the ascending order based on the number given in the [i][2]
:Time complexity: the time complexity for this function  would be O(n) as it goes through all N elements(amount of games played) within the list
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
def counting_sort_str(string,roster):
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
def analyze(results:list,score,roster):
    reverse_result = []
    for i in range(len(results)):
        reverse_result.append(results[i])
    for i in range(len(results)):
        reverse_result[i] = [reverse_result[i][1],reverse_result[i][0],100-reverse_result[i][2]]
    results += reverse_result
    for i in range(len(results)):
        results[i][0] = counting_sort_str(results[i][0],roster)
    for i in range(len(results)):
        results[i][1] = counting_sort_str(results[i][1],roster)
    radix_sort(results)
    top_10_matches = []
    updated_results = []
    for i in results:
        if i not in updated_results:
            updated_results.append(i)
    if len(updated_results)<10:
        top_10_matches.append(updated_results)
    else:
        iter_top_10 = len(updated_results)-1
        while len(top_10_matches)<10:
            top_10_matches.append(updated_results[iter_top_10])
            iter_top_10 -= 1
    searched_match = []
    for i in range(len(updated_results)):
        if updated_results[i][2] == score:
            searched_match.append(updated_results[i])
    if len(searched_match) == 0:
        scores_greater = []
        for i in range(len(results)):
            if results[i][2] > score:
                scores_greater.append(results[i])
        for i in range(len(scores_greater)):
            if scores_greater[i][2] == scores_greater[0][2]:
                searched_match.append(scores_greater[i])
    if len(updated_results)//2 < 10:
        searched_match.append(updated_results)
    return "{}\n{}".format(top_10_matches,searched_match)
print(analyze(results,64,3))