def inp():
    fname = input("Enter input file name: ")
    if (len(fname)) < 1: fname = '../sample_input.txt'
    fhand = open(fname)
    seatIdList = list()
    for boardingPass in fhand:
        boardingPass = boardingPass.rstrip()
        tempNum = calc_seat_id(boardingPass)
        seatIdList.append(tempNum)
    return seatIdList

def calc_seat_id(boardingPass):
    boardingPass = boardingPass.replace('F', '0')
    boardingPass = boardingPass.replace('B', '1')
    boardingPass = boardingPass.replace('L', '0')
    boardingPass = boardingPass.replace('R', '1')
    # print ("Boarding Pass: ", boardingPass)
    lineNum = boardingPass[:7]
    seatNum = boardingPass[7:]
    lineNum = int(lineNum, 2)
    seatNum = int(seatNum, 2)
    seatId = lineNum * 8 + seatNum
    # print ("Line: ", lineNum, "Seat: ", seatNum, "SeatID: ", seatId)
    return seatId

def find_my_seat (seatIdList):
    temp = None
    for i in seatIdList:
        # print("i: ", i, "temp: ", temp)
        if i == seatIdList[-1]: break
        if temp is None:
            temp = i
            continue
        if (temp + 1) != i:
            mySeat = temp + 1
            print ('My seat is: ', mySeat)
            break
        temp = i

seatIdList = list()
seatIdList = inp()
seatIdList.sort()
# print(seatIdList)
highestSeatId = seatIdList[-1]
print("Highest seat id is: ", highestSeatId)
find_my_seat(seatIdList)