import math

def check():
    if len(my_list) % 2 == 0:
        even_index = (len(my_list) / 2) - 1
        even_index_pone = even_index + 1
        result = (my_list[int(even_index)] + my_list[int(even_index_pone)]) / 2
        return result
    else:
        odd_index = math.ceil(len(my_list) / 2) - 1
        return my_list[odd_index]
        
def variance(my_list, mean):
    total = 0
    for i in range(len(my_list)):
        total += (my_list[i] - mean) ** 2
    return total / (len(my_list) - 1)
    
def IQR(my_list):
    if len(my_list) % 2 == 0:
        first_list = my_list[:math.floor(len(my_list) / 2)]
        second_list = my_list[math.floor(len(my_list) / 2):]

        if len(first_list) % 2 != 0:
            half_index = math.ceil(len(first_list) / 2) - 1
            print(first_list[half_index])
            print(second_list[half_index])

        else:
            first_half_index = math.floor(len(first_list) / 2) - 1
            second_half_index = math.floor(len(first_list) / 2)
            mean_first = (first_list[second_half_index] + first_list[first_half_index]) / 2
            mean_second = (second_list[second_half_index] + second_list[first_half_index]) / 2
            return mean_second - mean_first

        print(first_list)
        print(second_list)
    else:
        
    # if len(my_list) % 2 == 0:
    #     middle_index = int(len(my_list) / 2)
    #     first_half = range(middle_index - 1)
    #     first_half_number = 0
    #     second_half = range(middle_index, len(my_list) - 1)
    #     second_half_number = 0
    #     if len(first_half) % 2 != 0:
    #         mid_first_half = math.ceil(len(first_half) / 2) - 1
    #         mid_second_half = len(first_half) + mid_first_half
    #         return my_list[second_half] - my_list[mid_first_half]
    #     else:
    #         print(my_list[:len(first_half)])
    #         print(len(second_half))
    #     # else:


my_list = [40, 22, 35, 17, 36, 52, 51, 22, 48, 39, 58, 49, 25, 47, 56, 43, 45, 16, 34, 51]
my_list.sort()
print(my_list)

total = sum(my_list)
mean = total/len(my_list)

my_variance = variance(my_list, mean)
my_sd = my_variance ** 0.5

my_dict = {}
for i in my_list:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1
        
print("The mean is "+ str(mean))
print("The median is " + str(check()))
print("The variance is %.2f" % my_variance)
print("The Standard Deviation is %.2f" % my_sd)
print(my_dict)

my_list.extend([8, 65])
my_list.sort()
print(my_list)
IQR(my_list)



