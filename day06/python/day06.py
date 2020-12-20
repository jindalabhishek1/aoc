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
        # print("Line: ", line)
        if line == '':
            groupList.append(group)
            group = []
            continue
        group.append(line)
    groupList.append(group)
    return groupList

def prepare_list_of_dict(groupList):
    # creating a list of dictionary of count of question with answer "yes" by group members
    totalList = list()
    for group in groupList:
        dictOfQuestions = dict()
        for person in group:
            for question in person:
                count = dictOfQuestions.get(question, 0)
                count += 1
                dictOfQuestions[question] = count
        totalList.append(dictOfQuestions)
    return totalList

def calc_num_of_yes_part_01(groupList):
    part01List = list()
    for item in groupList:
        listKeys = list(item.keys())
        lenght = len(listKeys)
        part01List.append(lenght)
    return part01List

def calc_total_yes(listOfTotalYes):
    sum = 0
    for num in listOfTotalYes:
        sum += num
    return sum

def calc_num_of_yes_part_02(groupList):
    groupListPart02 = prepare_list_of_dict(groupList)
    part02List = list()
    lengthList = list()
    for item in groupList:
        lengthList.append(len(item))

    i = 0
    for item in groupListPart02:
        valueList = list(item.values())
        length = lengthList[i]
        i += 1
        temp = valueList.count (length)
        part02List.append(temp)
    return part02List


def part_01(groupList):
    groupList = prepare_list_of_dict(groupList)
    # print (groupList)
    listOfTotalYes = calc_num_of_yes_part_01(groupList)
    # print("No of questions with Yes answer for all groups: ", listOfTotalYes)
    totalYes = calc_total_yes(listOfTotalYes)
    print("Total yes: ", totalYes)

def part_02(groupList):
    listOfTotalCommonYes = calc_num_of_yes_part_02(groupList)
    CommonYes = calc_total_yes(listOfTotalCommonYes)
    print ("Common Yes: ", CommonYes)

groupList = inp()
# print("Questions with answer 'yes': ", groupList)
part_01(groupList)
part_02(groupList)
