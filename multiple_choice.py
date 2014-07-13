'''
multiple choice question engine version 1.1
By: ytivarg

You are welcome to use this just keep my name in header and give credit.  

HOW TO USE:
prompt ="Ask the question here"
choice =["1: first answer, "2: second","3: "third"] (no limit)
response =["response1","response2","response3"]
answer =multiple_choice.process_ans(prompt, choice, response)
'''

#test to see if a string equivalant to an integer.  Used for input validation
def isint(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
#input validation test after proven the ans is an int.  Makes sure 'ans' is in 'choice's range
def test(prompt,choice,length,ans):
        print("INVALID OPTION")
        ans=display_ques(prompt,choice,length)
        while isint(ans)==False:#test to see if the choice is an integer.
            print("INVALID OPTION")
            ans=display_ques(prompt,choice,length)
        ans=int(ans)
        return(ans)
#Displays the prompt with the possible choices, then asks for user input
def display_ques(prompt,choice,length):
    count=0
    print(prompt)
    while count < length:
        print(choice[count])
        count+=1
    ans=raw_input("Choose an answer: ")
    return(ans)
#prompt is a string.  choice and response are both lists of equal length.
def process_ans(prompt,choice,response):
    length=len(choice)
    ans=display_ques(prompt,choice,length)
    #some input validation.
    while isint(ans)==False:
        print("INVALID OPTION")
        ans=display_ques(prompt,choice,length)
    ans=int(ans)
    r=range(1, len(choice)+1)
    valid =ans in r
    #other input validation
    while (valid ==False):
        ans=test(prompt,choice,length,ans)
        valid =ans in r
    else:
        print response[ans-1]
        return(ans)
        