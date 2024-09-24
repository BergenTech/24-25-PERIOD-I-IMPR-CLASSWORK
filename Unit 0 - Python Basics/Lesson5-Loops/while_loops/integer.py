# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == 'q':  # quit
#         break
#     number = int(value)
#     if number % 2 == 0:  # an even number
#         continue
#     print(number, "squared is", number*number)
# print("Exiting the program!")
count = 0
while count < 5:
    print(count, end="-")
    count +=1
    print(f"count is:{count}")

