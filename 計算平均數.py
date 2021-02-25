def my_mean(input_list):
    '計算平均數'
    def my_sum(input_list):
        '計算總和'
        temp_sum = 0
        for i in input_list:
            temp_sum += i
        return temp_sum
    def my_length(input_list):
        '計算個數'
        temp_length = 0
        for i in input_list:
            temp_length += 1
        return temp_length
    return my_sum(input_list) / my_length(input_list)
my_list = [51, 8, 18, 13, 6, 64]
print(my_mean(my_list))