# class Test:
# 	def __init__(self):
# 		pass
		

# 	def solution(self, A, B):
# 		A_check_list = []
# 		B_check_list = []
# 		A_rotations = 0
# 		B_rotations = 0
# 		for i in range(len(A)):
# 			if i == 0:
# 				A_check_list.append(A[i])
# 				B_check_list.append(B[i])
# 			else:
# 				if A[i] == A_check_list[-1]:
# 					A_check_list.append(A[i])
# 				else:
# 					if B[i] == A_check_list[-1]:
# 						A_check_list.append(B[i])
# 						B_rotations += 1
# 				if B[i] == B_check_list[-1]:
# 					B_check_list.append(B[i])
# 				else:
# 					if A[i] == B_check_list[-1]:
# 						B_check_list.append(A[i])
# 						A_rotations += 1
# 			i += 1
# 		if len(A_check_list) == len(A) or len(B_check_list) == len(B):
# 			return A_rotations if A_rotations > B_rotations else B_rotations
# 		return -1

	    

# if __name__ == "__main__":
# 	test = Test()
# 	A = [1,2,3,6,3,2]
# 	B = [2,1,2,2,2,4]
# 	print(test.solution(A, B))

class Test:
	def __init__(self):
		pass
		

	def solution(self, plants, capacity):
		initial_cap = capacity
		total_steps = 0
		i = 0
		for plant in plants:
			if plant <= capacity:
				capacity = capacity - plant
				total_steps += 1
				i += 1
			else:
				capacity = capacity + initial_cap - plant
				i += 1
				total_steps = (i*3)+2

		return total_steps
	    

if __name__ == "__main__":
	test = Test()
	plants = [2,1,1] 
	capacity = 3
	print(test.solution(plants, capacity))


# class Test:
# 	def __init__(self):
# 		pass
		

# 	def solution(self, S, K):
# 		upper_S = S.upper()
# 		print(upper_S)
# 		no_dash_S = upper_S.replace("-", "")
# 		print(no_dash_S)
# 		if len(no_dash_S) <= K:
# 			return no_dash_S
# 		i = 0
# 		j = 1
# 		final_string_list = []
# 		for character in no_dash_S:
# 			if i%K == 0 and i != 0:
# 				final_string_list.insert(0, "-")
# 			final_string_list.insert(0, no_dash_S[-j])
# 			i += 1
# 			j += 1
# 		final_string = "".join(final_string_list)
# 		print(final_string)
# 		# final_string = []
	    

# if __name__ == "__main__":
# 	test = Test()
# 	S = "2-4A0r7-4k"
# 	K = 4
# 	test.solution(S, K)

# class Test:
#     def __init__(self, name="Empty"):
#         self.name = name
    
#     def print_name(self):
#         print(self.name)

# if __name__ == "__main__":
#     patrick = Test("Pat")
#     patrick.print_name()


# import sys
# import fileinput
# from math import acos, sin, cos, radians, floor
# RADIUS_MILES = 3963

# /*
#  * Complete the 'countSubarrays' function below.
#  *
#  * The function is expected to return a LONG_INTEGER.
#  * The function accepts following parameters:
#  *  1. INTEGER_ARRAY numbers
#  *  2. INTEGER k
#  */

# long countSubarrays(vector<int> numbers, int k) {
#     std::cout << numbers[0] << std::endl;
#     vector<long> subarray_products;
#     int index = 0;
#     long less_products = 0;
#     for (int i = 0; i < numbers.size(); i++) {
#         std::cout << "current start is: " << numbers[i] << std::endl;
#         subarray_products.push_back(0);
#         int inner_index = i;
        
#         for (int j = numbers.size()-1; j >= i; j--) {
#             if (subarray_products[index] == 0) {
#                 subarray_products[index] = numbers[inner_index];
#                 if (subarray_products[index] <= k) {
#                     less_products++;
#                 }
#                 std::cout << subarray_products[index] << std::endl;
#             } else {
#                 subarray_products[index] = subarray_products[index] * numbers[inner_index];
#                 if (subarray_products[index] <= k) {
#                     less_products++;
#                 }
#                 std::cout << subarray_products[index] << std::endl;
#             }
#             inner_index++;
#         }
#         index++;
#     }
#     return less_products;
# }


# class PathCalculator:
#     def __init__(self):
#         self.routes_dict = {}
#         self.distances_list = []
    
#     def process(self, line: str) -> str:
#         self.routes_dict.update({
#             int(line.split(":")[2]) : [line.split(":")[0], line.split(":")[1]]
#             })
#         self.distances_list.append(int(line.split(":")[2]))
#         if len(self.distances_list) == 1:
#             return "NONE"
#         print(self.distances_list)


# if __name__ == "__main__":
#     path_calc = PathCalculator()
#     print(path_calc.process("CHI:NYC:719"))
#     print(path_calc.process("NYC:LA:2414"))
#     print(path_calc.process("NYC:SEATTLE:2448"))
#     print(path_calc.process("NYC:HAWAII:4924"))

# class DestinationCalculator:
#     def __init__(self):
#         self.arrival_city_bool = False
#         self.cities_list = []
#         self.city_info_dict = {}
#         pass
    
#     def process(self, line: str) -> str:
#         line_format = line.split(":")[0]
#         if line_format == "LOC":
#             city_name = line.split(":")[1]
#             self.cities_list.append(city_name)
#             self.city_info_dict.update( 
#                 {city_name : [radians(float(line.split(":")[2])), radians(float(line.split(":")[3]))]} )
#             self.arrival_city_bool = True
#             return(city_name)
#         else:
#             abs_diff_long = abs(
#                 self.city_info_dict[self.cities_list[0]][1] -
#                 self.city_info_dict[self.cities_list[1]][1]
#                 )
#             angle = acos(
#                 ( sin(self.city_info_dict[self.cities_list[0]][0]) *
#                 sin(self.city_info_dict[self.cities_list[1]][0]) ) +
#                 ( cos(self.city_info_dict[self.cities_list[0]][0]) *
#                 cos(self.city_info_dict[self.cities_list[1]][0])   *
#                 cos(abs_diff_long) )
#                 )
#             distance = RADIUS_MILES * angle
#             return line.split(":")[1] + ":" + self.cities_list[0] + ":" + self.cities_list[1] + ":" + str(floor(distance))

# class DestinationCalculator:
#     def __init__(self):
#         self.depart_city_bool = True
#         self.depart_city_dict = {}
#         self.arrival_city_dict = {}
    
#     def process(self, line: str) -> str:
#         line_format = line.split(":")[0]
#         if line_format == "LOC":
#             city_name = line.split(":")[1]
#             if self.depart_city_bool:
#                 self.depart_city_dict = {
#                     "name" : city_name,
#                     "latitude" : radians(float(line.split(":")[2])),
#                     "longtitude" : radians(float(line.split(":")[3]))
#                     }
#             else:
#                 self.arrival_city_dict = {
#                     "name" : city_name,
#                     "latitude" : radians(float(line.split(":")[2])),
#                     "longtitude" : radians(float(line.split(":")[3]))
#                     }
#             self.depart_city_bool = False
#             return(city_name)
#         else:
#             abs_diff_long = abs(
#                 self.depart_city_dict["longtitude"] - 
#                 self.arrival_city_dict["longtitude"]
#                 )
#             angle = acos(
#                 ( sin(self.depart_city_dict["latitude"]) *
#                 sin(self.arrival_city_dict["latitude"]) ) +
#                 ( cos(self.depart_city_dict["latitude"]) *
#                 cos(self.arrival_city_dict["latitude"])   *
#                 cos(abs_diff_long) )
#                 )
#             distance = RADIUS_MILES * angle
#             depart_city_bool = True
#             return line.split(":")[1] + ":" + self.depart_city_dict["name"] + ":" + self.arrival_city_dict["name"] + ":" + str(floor(distance))

# if __name__ == "__main__":
#     dest_calc = DestinationCalculator()
#     print(dest_calc.process("LOC:CHI:41.836944:-87.684722"))
#     print(dest_calc.process("LOC:NYC:40.7127:-74.0059"))
#     print(dest_calc.process("TRIP:C0FFEE1C:CHI:NYC"))



# def test():
#     account_num = "1CC0FfEE"
#     if len(account_num) != 8:
#         return "INVALID"
#     for digit in account_num:
#         try:
#             int(digit, 16)
#         except ValueError:
#             return "INVALID"  
    
#     hex_string = account_num[2:8]
#     decimal_string = str(int(hex_string, 16))
#     checksum_dec = 0
#     for digit in decimal_string:
#         checksum_dec += int(digit)
#     checksum_hex = hex(checksum_dec)
#     print(checksum_hex.split("x"))
#     checksum_hex = hex(checksum_dec).split("x")[-1].upper()
#     if account_num[0:2] == checksum_hex:
#         return("VALID")
#     else:
#         return("INVALID")




# print(test())

# checksum_hex = "0x1c23"
# print(checksum_hex.split("x")[-1].upper())


# for line in sys.stdin:
#     line = line.strip()
#     well_form = "True"
#     last_num_index = -1
#     well_form_dict = {
#     "(":")",
#     ")":"(",
#     "[":"]",
#     "]":"[",
#     "{":"}",
#     "}":"{"
#     }
#     for char in line:
#         if well_form_dict[char] != line[last_num_index]:
#             well_form = "False"
#             break
#         last_num_index -= 1
#     print(well_form)
    

# for line in sys.stdin:
#     num = line
#     num = num.strip()
#     happy_num = False
#     sum_squares = 0
#     list_prev_num = []
#     while(True):
#         string_num = str(num)
#         list_squares = []
#         for digit in string_num:
#             square_digit = int(digit)*int(digit)
#             list_squares.append(square_digit)
#         sum_squares = sum(list_squares)
#         print(sum_squares)
#         if sum_squares == 1:
#             happy_num = True
#             print(1)
#             break
#         if sum_squares in list_prev_num:
#             print(0)
#             break
#         num = sum_squares
#         list_prev_num.append(sum_squares)
#         print(list_prev_num)




# s = "ABBA"
# combos = {}
# anna_count = 0
# s = s.lower()
# for x in range(len(s)):
#     current_string = ""
#     for y in range(len(s)):
#         current_string += s[y]
#         print(current_string)
#         sort_list = sorted(current_string)
#         ordered_s = ""
#         for c in sort_list:
#             ordered_s += c
#         print("current ALPHA string is: %s" % ordered_s)
#         if (combos.get(ordered_s) == None):
#             combos.update( {ordered_s : 1} )
#         else:
#             anna_count += 1
#     s = s[1:]
# print(anna_count)
#     

# class Test:
#     def __init__(self, name="Empty"):
#         self.name = name
    
#     def print_name(self):
#         print(self.name)

# if __name__ == "__main__":
#     patrick = Test("Pat")
#     patrick.print_name()

# sample_string = "GeeksQuiz"
# lower_string = sample_string.lower()
# i = -1

# all_chars_dict = {}
# non_repeat_list = []

# for c in lower_string:
#     print(lower_string[i])
#     if lower_string[i] in all_chars_dict:
#         all_chars_dict[lower_string[i]] = all_chars_dict[lower_string[i]] + 1
#     else:
#         all_chars_dict[lower_string[i]] = 1
#         non_repeat_list.append(lower_string[i])
#     i -= 1
# print (all_chars_dict)
# print("the first non-repeating character is: %s" % non_repeat_list.pop())

# x = 10 
# y = 12
# q = 3
# count = 0
# for num in range(x, y+1):
#     original_num_str = str(num)
#     product_num_str = str(num*q)
#     print("Og: %s and product: %s" % (original_num_str, product_num_str))
#     repeat = False
#     for digit in original_num_str:
#         if digit in product_num_str:
#             repeat = True
#     if not repeat:
#         count += 1
# print(count)

# l = 3 
# r = 9
# odd_list = []
# list_num = range(l, r+1)
# print(list_num)
# for x in list_num:
#     if (x%2) != 0:
#         odd_list.append(x)
# print(odd_list)

# print(2*3*5*7*11*13*17*19)

# per_worker = 60/39

# x = -10
# ap_list = [100, 100+(x), 100+(2*x), 100+(3*x), 100+(4*x), 100+(5*x)]
# sum_next_six = 100+(6*x) + 100+(7*x) + 100+(8*x) + 100+(9*x) + 100+(10*x) + 100+(11*x) 
# print(ap_list)
# print(sum(ap_list))
# print(sum_next_six*5)

# daily_price = [0, 0, 0, 0, 0, 0, 0]
# iterations = int((len(daily_price))/7) + (len(daily_price))%7
# print(iterations)
# seven_day_list = []
# formatted_prices = []
# start_index = 0
# for x in range(0,iterations):
#     seven_day_list = daily_price[start_index:start_index+7]
#     print(seven_day_list)
#     avg = sum(seven_day_list)/7
#     print()
#     formatted_prices.append(str('{:.2f}'.format(round(avg, 2)))) 
#     start_index += 1
# print(formatted_prices)

# grid = [[7,7,3,8,1], [13,5,4,5,2], [9,2,12,3,9], [6,12,1,11,41]]
# print(grid)

# row = len(grid)
# col = len(grid[0])

# print(row)
# print(col)

# for x in grid[0]:
#     print(x)
# for i in range(len(grid)-1):
#     print(grid[i+1][len(grid[0])-1])
# print(grid[-1])
# last = -2
# for i in range(len(grid[-1])-1):
#     print(grid[-1][last])
#     last -= 






# primes = []
# for j in range(int(col/2)):
#     print("CHECK")
#     for i in range(0, len(grid[j]) - j):
#         x = 2
#         num = grid[j][i]
#         is_prime = True
#         while x < num:
#             div_result = num%x
#             if (div_result == 0) or (num == 1):
#                 is_prime = False
#                 break
#             x += 1
#         if num == 1:
#             is_prime = False
#         if is_prime:
#             primes.append(num)

        
#         print(num)
#     print("NEXT")
#     for i in range(j+1, row-1):
#         x = 2
#         num = grid[i][col-j-1]
#         is_prime = True
#         while x < num:
#             div_result = num%x
#             if (div_result == 0) or (num == 1):
#                 is_prime = False
#                 break
#             x += 1
#         if num == 1:
#             is_prime = False
#         if is_prime:
#             primes.append(num)

#         print(num)
#     print("AH")
#     if j == 0:
#         offset = 0
#     else:
#         offset = 1
#     for i in range((-1-j)-offset, -(col-j+1), -1):
#         x = 2
#         num = grid[row-j-1][i]

#         is_prime = True
#         while x < num:
#             div_result = num%x
#             if (div_result == 0) or (num == 1):
#                 is_prime = False
#                 break
#             x += 1
#         if num == 1:
#             is_prime = False
#         if is_prime:
#             primes.append(num)

# print(primes)

# x = 2
# num = 1
# is_prime = True
# while x < num:
#     div_result = num%x
#     print(div_result)
#     if div_result == 0:
#         is_prime = False
#         break
#     x += 1


# print(is_prime)