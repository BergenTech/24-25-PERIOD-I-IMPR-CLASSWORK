numbers = (15, 6, 5, 3, 8, 2, 9, 12)
def oddSmall(tuple_number):
    odd_numbers = ()
    smallest = 0
    # # Conventional way
    # for num in tuple:
    #     if num % 2 != 0:
    #         odd_numbers += num,
    
    # Using comprehension
    odd_numbers = tuple(num for num in tuple_number if num % 2 !=0)
    smallest = min(odd_numbers) 
    return f"""
    The odd numbers: {odd_numbers}
    The smallest number: {smallest}
    """
if __name__ == "__main__":
    print(oddSmall(numbers))