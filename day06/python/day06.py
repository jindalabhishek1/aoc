def inp():
    fname = input("Enter input file name: ")
    # if (len(fname)) < 1: fname = "../sample_input.txt"
    try:
        fhand = open(fname)
    except:
        fname = "../sample_input.txt"
        print("Didn't entered a valid file, choose sample input file")
        fhand = open(fname)
    groupList = list()
    group = list()
    for line in fhand:
        # print("group: ", group, type(group), len(groupList))
        line = line.rstrip()
        print("Line: ", line)
        if line == '':
            groupList.append(group)
            group = []
            continue
        group.append(line)
    groupList.append(group)
    return groupList

def calc_num_of_yes(groupList):
    totalList = list()
    for group in groupList:
        listOfQuestions = list()
        for question in group:
            count = listOfQuestions.count(question)
            if count == 0:
                listOfQuestions.append(question)
        length = len(listOfQuestions)
        totalList.append(length)
    return totalList

def calc_total_yes(listOfTotalYes):
    sum = 0
    for num in listOfTotalYes:
        sum += num
    return sum

groupList = inp()
print("Questions with answer 'yes': ", groupList)
# listOfTotalYes = calc_num_of_yes(groupList)
# print("No of questions with Yes answer for all groups: ", listOfTotalYes)
# totalYes = calc_total_yes(listOfTotalYes)
# print("Total yes: ", totalYes)