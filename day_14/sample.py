def sum_number(arg):
    return sum(arg)

def higher_order_function(sum_numbers,arg):
    x=sum_numbers(arg)
    return x
print(higher_order_function(sum_number,[1,2,3,4,5,6])) 
