import random
import pandas as pd
import math
import numpy as np


def AddStudent(Number, Name, Gender, Partner, Disliked, Row):
    global StudentList
    global integer_repeater
    StudentList.append([Number, Name, Gender, Partner, Disliked, Row])

def AddStudentFromList(Number):
    Partner = []
    Disliked = []
    for integer_repeater in range(len(partner_req)):
        b = partner_req[str(integer_repeater)][Number]
        if b * 0 == 0:
            a = int(b)
            if a == 1:
                Partner.append(integer_repeater)
            elif a == -1:
                Disliked.append(integer_repeater)
            a = 0
        integer_repeater = integer_repeater + 1
    integer_repeater = 0
    RowLimit = []
    while integer_repeater < 5:
        b = row_req[str(integer_repeater)][Number]
        if b * 0 == 0:
            a = int(b)
            if a == 1:
                RowLimit.append(integer_repeater)
            a = 0
        integer_repeater = integer_repeater + 1
    integer_repeater = 0
    AddStudent(student_list['Number'][Number], student_list['Name'][Number], student_list['Gender'][Number], Partner, Disliked, RowLimit)


def generate_seating_arrangements(num_arrangements, num_seats=30, num_people=29):
    arrangements = []
    for _ in range(num_arrangements):
        seats = list(range(0, num_people)) + [None]  # 生成0-28号和一个None
        random.shuffle(seats)  # 随机打乱座位
        # 确保最后一排有一个空位
        if None not in seats[-5:]:
            non_last_row_index = seats.index(None)
            last_row_index = random.choice(range(-5, 0))  # 在最后一排随机选择一个位置
            seats[non_last_row_index], seats[last_row_index] = seats[last_row_index], seats[non_last_row_index]

        # 将座位安排分成5排
        arrangement = [seats[integer_repeater :integer_repeater + 6] for integer_repeater in range(0, num_seats, 6)]
        arrangements.append(arrangement)
    return arrangements




'''
def score_arrangement(arrangement, preferences):
    score = 0
    for row in range(6):
        for col in range(5):
            student = arrangement[row][col]
            if student is None:
                continue
            pref = preferences[student]
            # 检查希望坐在一起的人
            for other in pref[0]:
                if other in arrangement[row]:
                    score += 1
            # 检查不希望坐在一起的人
            for other in pref[1]:
                if other not in arrangement[row]:
                    score += 1
            # 检查是否希望同行或同列都是女生
            if pref[2]:
                if all(s is None or s % 2 == 0 for s in arrangement[row]):
                    score += 1
                #if all(s is None or s % 2 == 0 for s in zip(*arrangement)[col]):
                #    score += 1
            # 检查是否希望坐在前三排
            if pref[3] and row < 3:
                score += 1
    return score
'''

num_of_rows = 6
num_of_columns = 5
max_score = 0

def score_arrangement(arrangement, preferences):
    seating = np.array(arrangement).flatten()
    score = 0
    seat_index = 0
    #print("arrangement:",arrangement)
    for student in seating:
        if student == None:
            break
        #print("seat_index:",seat_index)
        #print("student:",student)
        corresponding_row = math.floor((seat_index + 1) / num_of_columns) - 1
        #print(preferences[student][5])
        if corresponding_row in preferences[student][5]:
            score += 1
        matrix = []
        corresponding_position_in_row = ((seat_index + 1) / num_of_columns - math.floor((seat_index + 1) / num_of_columns)) * num_of_columns - 1
        if corresponding_position_in_row < 0:
            corresponding_position_in_row += num_of_columns
        if corresponding_position_in_row == 0:
            matrix.append(seat_index + 1)
            matrix.append(seat_index + num_of_columns - 1)
            if corresponding_row != 0:
                matrix.append(seat_index - num_of_columns)
                matrix.append(seat_index - num_of_columns + 1)
                matrix.append(seat_index - 1)
            if corresponding_row != num_of_rows - 1:
                matrix.append(seat_index + num_of_columns)
                matrix.append(seat_index + num_of_columns + 1)
                matrix.append(seat_index + 2 * num_of_columns - 1)
        elif corresponding_position_in_row == num_of_columns - 1:
            matrix.append(seat_index - num_of_columns + 1)
            matrix.append(seat_index - 1)
            if corresponding_row != 0:
                matrix.append(seat_index - num_of_columns)
                matrix.append(seat_index - 2 * num_of_columns + 1)
                matrix.append(seat_index - num_of_columns - 1)
            if corresponding_row != num_of_rows - 1:
                matrix.append(seat_index + num_of_columns)
                matrix.append(seat_index + 1)
                matrix.append(seat_index + num_of_columns - 1)
        else:
            matrix.append(seat_index + 1)
            matrix.append(seat_index - 1)
            if corresponding_row != 0:
                matrix.append(seat_index - num_of_columns)
                matrix.append(seat_index - num_of_columns + 1)
                matrix.append(seat_index - num_of_columns - 1)
            if corresponding_row != num_of_rows - 1:
                matrix.append(seat_index + num_of_columns)
                matrix.append(seat_index + num_of_columns + 1)
                matrix.append(seat_index + num_of_columns - 1)
        matrix_check = 0
        for seat in matrix:
            if seat > num_of_columns * num_of_rows - 1:
                matrix[matrix_check] = seat - num_of_columns
            if seat < 0:
                matrix[matrix_check] = seat + num_of_columns
            matrix_check += 1
        partner_index = 0
        disliked_index = 0
        #print("matrix:",matrix)
        for seat in matrix:
            if seating[seat] in preferences[student][3]:
                partner_index += 1
            if seating[seat] not in preferences[student][4]:
                disliked_index += 1
        if partner_index == len(preferences[student][3]):
            score += 1
        if disliked_index == len(matrix):
            score += 1
        seat_index += 1

    global max_score
    if(max_score < score):
        max_score = score
        print("raw score:",score)
    return score




def rank_arrangements(arrangements, preferences):
    scores = [(score_arrangement(a, preferences), a) for a in arrangements]
    print("len:",len(scores))
    print(scores[0:10])
    scores.sort(reverse=True)
    print(scores[0:10])
    return scores



'''
#随机生成preference
import random

preferences = {}

for integer_repeater in range(1, 30):  # 我们有29个学生，编号从1到29
    wants_to_sit_by = set()
    doesnt_want_to_sit_by = set()
    
    # 随机选择0-5个学生希望坐在一起
    for _ in range(random.randint(0, 5)):
        student_id = random.randint(1, 29)
        # 确保学生不能选择自己
        if student_id != i:
            wants_to_sit_by.add(student_id)
    
    # 随机选择0-3个学生不希望坐在一起
    for _ in range(random.randint(0, 3)):
        student_id = random.randint(1, 29)
        # 确保学生不能选择自己，且不能同时出现在希望坐在一起的列表和不希望坐在一起的列表
        if student_id != integer_repeater and student_id not in wants_to_sit_by:
            doesnt_want_to_sit_by.add(student_id)
    
    # 随机选择是否希望所在的行都是同性
    wants_row_of_same_gender = random.choice([True, False])
    
    # 随机选择是否希望坐在前三排
    wants_to_sit_in_front = random.choice([True, False])
    
    preferences[i] = (wants_to_sit_by, doesnt_want_to_sit_by, wants_row_of_same_gender, wants_to_sit_in_front)

print(preferences)

preferences={
1: ({24, 22}, {16, 13}, False, True), 
2: (set(), {21, 5, 6}, False, True), 
3: ({5, 7, 10, 22, 27}, {29}, False, False), 
4: ({17}, set(), False, False), 
5: ({2, 11, 13, 15, 20}, {28, 23}, False, False), 
6: ({20}, {9, 3, 21}, False, True), 
7: ({9, 3, 4, 1}, {10, 26, 22}, True, False), 
8: ({11, 20}, {2, 7}, False, False), 
9: ({21}, {23}, False, True), 
10: ({11, 20, 23}, set(), True, False), 
11: ({8, 9, 26, 29}, {1}, True, True), 
12: ({17, 10, 5}, {1, 18, 20}, True, False), 
13: ({8, 18, 12, 7}, {25}, False, False), 
14: ({9, 26, 5, 17}, set(), True, True), 
15: ({3, 7}, set(), False, False), 
16: ({10, 23}, set(), True, True), 
17: ({3}, {8, 10, 29}, True,False), 
18: ({16, 12, 28, 7}, set(), False, True), 
19: (set(), set(), True, True), 
20: ({6}, {18, 28, 23}, False, True), 
21: ({16, 20, 7}, set(), True, False), 
22: ({8, 5, 7}, set(), True, True), 
23: ({19, 3, 12}, set(), True, False), 
24: ({25, 11, 22}, set(), False, False), 
25: (set(), {20, 29}, False, True), 
26: ({18, 29}, {17, 4}, True, True), 
27: ({9, 5, 29, 23}, {8, 15}, True, False), 
28: ({8, 17, 3, 22}, {11, 6}, True, True), 
29: ({9, 27, 14}, {26, 3, 15}, True, False)
}
'''
'''
column_num = 6
row = 5
seat_num = 30

i<seat_nu
row = i/column_num
column = i%column_num
'''


# Start of main process
student_list = pd.read_csv('data/NameList.csv')
partner_req = pd.read_csv('data/PartnerReq.csv')
row_req = pd.read_csv('data/RowReq.csv')

StudentList = []
integer_repeater = 0
while integer_repeater < 29:
    AddStudentFromList(integer_repeater)
    integer_repeater = integer_repeater + 1
integer_repeater = 0


#随机生成1000个SeatingPlan
arrangements = generate_seating_arrangements(500)
for i, arrangement in enumerate(arrangements, 1):
    if(i==999):
        print(f"Arrangement {i}:")
        for row in arrangement:
            print(row)

# 对于随机生成的arrangements进行排序
ranked = rank_arrangements(arrangements, StudentList)
print("max raw score:",max_score)

#打出排在前十位的ranked_arrangements
'''
for i, arrangement in enumerate(ranked, 0):
    if(i<10):
        print(f"rank:",ranked[i])

        print(f"score:",ranked[i][0])
        print(f"Arrangement {i}:",arrangement)
        

        for row in ranked[i][1]:
            print(row)
'''
namelist = []
for i in range(10):
    print(f"rank:",ranked[i])
    print(f"score:",ranked[i][0]/87*100)
    #print(f"Arrangement {i}:",ranked[i][1])
    for row in ranked[i][1]:
        for j in row:
            #print(j)
            if(j==None):
                name='none'
                namelist.append(name)
            else:
                namelist.append( student_list['Name'][j])
                name = student_list['Name'][j]
                #print(name)
        print(namelist)
        namelist = []

#print(score_arrangement(ranked[0][1],StudentList))
    
