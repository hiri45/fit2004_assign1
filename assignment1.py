"""
counting_sort is a function used for integers. This function is an algorithm which sorts the integers in increasing order from lowest to highest
it takes input value, which is a list to determine what the output value would be, since this function is to implemented within the radix sort function
there is also a place value input which is esentially the place for each digit of the number. Inside the function there are multiple empty arrays created;
count, position and output which is used to find the final output. In this function there are 4 for loops which esentially calculate the count array, position array, and output array
the final for loop changes the initial array with the updated output array values.
:Input: 
    argv1: list
    argv2: place_value
:Output, return or postcondition: 
    the output from using this function is the input, in the ascending order based on the number given in the [i][2]
:Time complexity: 
    the time complexity for this function  would be O(N+k) as it goes through all N elements(amount of games played) within the list as well as the position array
:Aux space complexity: 
    the aux space complexity for this function is O(k)
"""
def counting_sort(list,place_value):
    length = len(list) 
    # create a count and position of [0]*10 which to deal with all digits 0-9
    count_int = [0]*10
    position_int = [0]*10
    output_int = [0]*length
    # dependent on the place value selected, in the case of radix sort it starts at 1 which is the first digit, it implements the count value by 1 dependent on how many times that value occurs in the list
    for i in range(0,length):
        # modulus the score within the list depending on the place value, which gives the value for the required placeholder(ones,tens,hundreds)
        val = (list[i][2]//place_value)%10 
        count_int[val] += 1
    # the position array is then implemented using the count array
    for i in range(1,10):
        position_int[i] = position_int[i-1] + count_int[i-1]
    # the next for loop is ran to update the output array dependent on the position at each value occurs
    for i in range(length):
        val = (list[i][2]//place_value)%10
        output_int[position_int[val]] = list[i]
        position_int[val]+=1
    # the input list is then updated using the ouput array calculated before
    for i in range(0,length):
        list[i] = output_int[i]
"""
counting_sort_str is a function used for strings, in which it orders the letters within the string in alphabetical order. A single string is inputed as the input to perform the function. Just like the counting 
sort used for integers this function creates a count, position and ouput array, however in this case the position and count array consist of zeros up to 90 since the ascii value of Z is 90. It runs 4 for loops 
to implement the count, position and output array. When updating the count array the function uses the in-built function ord() to check the ascii value of each letter in the string. Since a string cannot be 
iterated over there is an updated_string variable which is used to join the letter in the output array. The original input string is then changed to equal the updated string which is the string in alphabetical
order
Input:
    argv1: string
Output, return or postcondition:
    the output is the input string ordered in alphabetical order
Time complexity:
    Since the function computes over the length of string the time complexity is O(M+k) where M is the number of characters in the string and k is the position array
Aux space complexity:
    the aux space complexity for this function is O(k)
"""
# same methods used in counting sort for integers
def counting_sort_str(string):
    length_str = len(string)
    count_str = [0]*90
    position_str = [0] * 90
    output_str = [0] * length_str
    for i in string:
        count_str[ord(i)] += 1
    for i in range(1,90):
        position_str[i] = position_str[i-1] + count_str[i-1]
    for i in range(length_str):
        output_str[position_str[ord(string[i])]] = string[i]
        position_str[ord(string[i])] += 1
    updated_string = ''
    for i in output_str:
        updated_string+=i
    string = updated_string
    return string
"""
Radix sort is a function which uses counting sort to order numbers from lowest to highest, however it divides the number up into its specific placeholder (ones,tens,hundreds), in which is sorts it based on each
digit, starting at the ones column. Initially the place value is set to 1 as it orders the ones column first. An empty array 'scores' is created to place all the numerical values from the specific list format inside it.
This is used to calculate the maximum number from that list. This is esentially an invariant or standpoint as to what place the function will go up to. The function then enters a while loop in which it will implement
counting sort on that place holder and then it will multiply the placeholder by 10 to go the next placeholder. The while loop will run until it reaches the highest placeholder.
Input:
    argv1:list
Output, return or postcondition:
    the output is the input list ordered in ascending order 
Time complexity:
    the time complexity of radix sort is O(kN) where N is the number of elements in this list and k is the number of digits in each number
Aux space complexity:
    the aux space complexity for this function is O(N + k)
"""
def radix_sort(list):
    # intializes place value as 1
    place_value = 1
    scores = []
    # appends all the scores from the input list into a seperate array to calculate the max
    for i in range(len(list)):
        scores.append(list[i][2])
    max_score = max(scores)
    # uses count sort for each digit in a number within the list to order until it reaches final placeholder
    while max_score // place_value > 0:
        counting_sort(list,place_value)
        place_value = place_value*10
"""
Analyze is a function used to find the top 10 matches within a list as well as the matches within a list equal to the input score. The function returns the top 10 matches in descending order by their scores 
represented in the input list. If there are matches between the same teams and thesame score only one of those matches will be presented in the output for top 10 matches. If there is less than 10 matches all the 
matches will be represented in the top 10 matches. For the matches outputted for the searched matches which is based on the score inputted from 0-100 it return matcheswith matches equal to the score if there is 
any, however if there are matches between the same teams only one of the matches will be includuded in thesearched matches. If the score is not found the function will return the matches with the closest score 
which is higher than the input score. If there are no matches with score higher than the inputted score there will be nothing appended to the searched matches. To calculate the values for top 10 matches and searched
matches the results array must be represented in the form [team2,team1,100-score] as well as the elements in the orgiginal list. Counting_sort_str and radix sort is used on the results to order all the values.Using this 
list an updated list is then created which doesn't inlcude any duplicates. In this case a duplicate is when team1,team2 and score is equal to other elements within the list. 
Input:
    argv1:results
    rgv2:score
    argv3:roster
Output, return or postcondition:
    the output for this function is the top 10 matches in descending order and searched matches which are the matches equal to score inputted into the function
Time complexity:
    The time complexity of this function is O(NM) where N is the elements in the list and M is the length of characters in the string
Aux space complexity:  
    aux space complexity is O(NM)
"""
def analyze(results:list,score,roster):
    # reverse result is created to implement the results in form [team2,team1,100-score]
    reverse_result = []
    for i in range(len(results)):
        reverse_result.append(results[i])
    for i in range(len(results)):
        reverse_result[i] = [reverse_result[i][1],reverse_result[i][0],100-reverse_result[i][2]]
    # reverse_results is then added to the input results list
    results += reverse_result
    # a for loop is then iterated through the list, in which counting_sort_str() is called for team1 and team2
    # this reaches the asked complexity of O(NM) where N is the number of elements in the list and M is the length of the characters within the team
    for i in range(len(results)):
        results[i][0] = counting_sort_str(results[i][0])
    for i in range(len(results)):
        results[i][1] = counting_sort_str(results[i][1])
    # radix_sort() is called to order all the arrays within the results  
    radix_sort(results)
    # updated_results is used to append elements from results which also ensures that there are no duplicates
    updated_results = []
    for i in results:
        if i not in updated_results:
            updated_results.append(i)
    top_10_matches = []
    # if-else loops used to append required results in top 10 matches
    if len(updated_results)//2<10:
        top_10_matches.append(updated_results)
    else:
        iter_top_10 = len(updated_results)-1
        while len(top_10_matches)<10:
            top_10_matches.append(updated_results[iter_top_10])
            iter_top_10 -= 1
    # searched_is used to append the required matches according to the inputted score
    searched_match = []
    # if the score is within the list
    for i in range(len(updated_results)):
        if updated_results[i][2] == score:
            searched_match.append(updated_results[i])
    # if the score isn't within the list
    if len(searched_match) == 0:
        scores_greater = []
        # appends the scores greater than the required score asked for
        for i in range(len(updated_results)):
            if results[i][2] > score:
                scores_greater.append(updated_results[i])
        # Using the scores_greater list, the for loop implements the elements with equal score to the first element of the scores_greater. This appends the closest higher score to the required score whilst checking 
        # if there are multiple elements of that higher score.
        for i in range(len(scores_greater)):
            if scores_greater[i][2] == scores_greater[0][2]:
                searched_match.append(scores_greater[i])
    return [top_10_matches,searched_match]