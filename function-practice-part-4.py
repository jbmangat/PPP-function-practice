# 1. max_num()
def max_num(num1,num2,num3):
    print(max(num1,num2,num3))
max_num(10,23,13)

# 2. mult_list()
def mult_list(nums):
    if len(nums) == 0:
        return 1
    else:
        return nums.pop() * mult_list(nums)
print(mult_list([1,2,3,4]))

# rev_string()
def rev_string(str):
    return str[::-1]
print(rev_string('sheeeeesh'))

# num_within()
def num_within(num, min, end):
    if num > min and num < end : 
        return True
    else:
        return False
print(num_within(5,3,10))

# pascal
# 1st 2 rows
triangle = [[1],[1,1]]

def pascal(n):
    if n < 1:
        print("invalid number of rows")
    elif n == 1: 
        print(triangle[0])
    else:
        row_number = 2
        # adds correct number of rows
        while len(triangle) < n:
            # empty row
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                # appends first 1 into row
                if i == 0:
                    row.append(1)
                # appends all numbers between 1 and 1 into a row
                elif i > 0 and i < length - 1:
                    row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
                # appends last 1 into row
                else:
                    row.append(1)
            # appends rows into triangle
            triangle.append(row)
            # repeats for each row
            row_number += 1
        for row in triangle:
            print(row)

print('------')
pascal(1)
print('------')
pascal(2)
print('------')
pascal(4)
