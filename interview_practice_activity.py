# 1
def has_string(str):
	x = "Bye"
	return x in str
print(has_string("Hello World"))
print(has_string("Bye World"))
print(has_string("bye World"))
#2
def sum_ting(num):
	if num == 1:
		return 1
	else:
		return num + sum_ting(num-1)
print(sum_ting(5))
#3	
def reverse(str):
	new = str[::-1]
	return new
print (reverse("sheeeeesh"))
#4
x = ["among us", "one Piece", "ayo"]
def cap(str_lst):
	return str_lst.upper()   

y = map(cap, x)
print(list(y))
#5
