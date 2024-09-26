# # Example while loop
# count = 0
# while count < 5:
#     print(f"Count: {count}")
#     count += 1
# # break statement - quits the loop
# password = 'quit'
# while True:
#     user_input = input("Enter Password:")
#     if user_input == password:
#         print('Access Granted!')
#         break

# continue statement
count = 0
while count < 5:
    count +=1
    if count == 3:
        continue
    print(f'Count: {count}')
    