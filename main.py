# Binary Search
# Log_2(N)

# def binary_search(list, item):
#     print("in function now")
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         print("checking . . . ")
#         mid = round((low + high) / 2)
#         guess = list[mid]
#         print("mid: ", mid)
#
#         if guess == item:
#             return mid
#
#         if guess < item:
#             low = mid + 1
#
#         else:
#             high = mid - 1
#
#     return None
#
#
# result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11)
#
# print(result)


# Binary Digit addition


# def addBinary(a: str, b: str) -> str:
#     extra_1 = [0, 0]
#     i = 0
#
#     a_array = list(a)
#     b_array = list(b)
#     binary_answer = []
#
#     inverted_a = invert(a_array)
#     inverted_b = invert(b_array)
#
#     ai_length = len(inverted_a)
#     bi_length = len(inverted_b)
#
#     inverted_a_spliced = []
#     inverted_b_spliced = []
#
#     print("a_array inverted: ", inverted_a)
#     print("===============")
#     print("b_array inverted: ", inverted_b)
#     print("===============")
#     print("inverted_a length: ", ai_length)
#     print("===============")
#     print("inverted_b length: ", bi_length)
#
#     if ai_length == 1 and bi_length == 1:
#         if inverted_a[0] == 1:
#             if inverted_b == 1:
#                 return "10"
#             else:
#                 return "1"
#         if inverted_a[0] == "0":
#             if inverted_b[0] == "1":
#                 return "1"
#             else:
#                 return "0"
#
#     if ai_length >= bi_length:
#
#         for digit in inverted_b:
#
#             if digit == "1" and inverted_a[i] == "1":  # when a is 1 and b is 1
#                 if extra_1[0] == 1:
#                     extra_1 = extraTen(1)
#                 else:
#                     extra_1 = extraTen(0)
#
#                 binary_answer.append(extra_1.pop(0))
#
#                 # print(f"extra_1 {i}: ", extra_1)
#                 # print("Binary answer: ", binary_answer)
#
#             elif digit == "1" or inverted_a[i] == "1":  # when a or b is 1 and the other is 0
#                 if extra_1[0] == 1:
#                     extra_1 = extraTen(0)
#                     binary_answer.append(extra_1.pop(0))
#                     extra_1 = [0, 0]
#                     # print(f"extra_1 {i}: ", extra_1)
#                     # print("Binary answer: ", binary_answer)
#                 else:
#                     binary_answer.append(1)
#                     # print(f"extra_1 {i}: ", extra_1)
#                     # print("Binary answer: ", binary_answer)
#             else:  # when both a and b are 0
#                 if extra_1[0] == 1:
#                     binary_answer.append(extra_1.pop(0))
#                     extra_1 = [0, 0]
#                 else:
#                     binary_answer.append(0)
#                 # print(f"extra_1 {i}: ", extra_1)
#                 # print("Binary answer: ", binary_answer)
#
#             i += 1
#
#             # if i == 1:
#             #     inverted_a_spliced.append(inverted_a[1])
#             #     print("whats the spliced invert: ", inverted_a_spliced)
#             # else:
#
#         inverted_a_spliced = inverted_a[i:]
#         print("=========")
#         print("inverted list a: ", inverted_a_spliced)
#
#         for digit in inverted_a_spliced:
#             print("digit: ", digit)
#             print("type of digit: ", type(digit))
#             print("extra 1 down here: ", extra_1)
#
#             if digit == "1" and extra_1[0] == 1:
#                 extra_1 = extraTen(0)
#                 binary_answer.append(extra_1.pop(0))
#             elif digit == "0" and extra_1[0] == 1:
#                 binary_answer.append(extra_1.pop(0))
#             elif digit == "0" and extra_1[0] == 0:
#                 binary_answer.append(0)
#             else:
#                 binary_answer.append(1)
#
#         while len(extra_1) > 0 and extra_1.count(1) >= 1:
#             binary_answer.append(extra_1.pop(0))
#         # print("Binary answer: ", binary_answer)
#
#         final_answer = invert(binary_answer)
#         # print("final answer: ", final_answer)
#
#         final_answer = "".join(str(digit) for digit in final_answer)
#
#         # print("final answer: ", final_answer)
#         return final_answer
#
#     if ai_length < bi_length:
#         for digit in inverted_a:
#             if digit == "1" and inverted_b[i] == "1":  # when a and b is 1
#                 if extra_1[0] == 1:
#                     extra_1 = extraTen(1)
#                 else:
#                     extra_1 = extraTen(0)
#                 binary_answer.append(extra_1.pop(0))
#
#             elif digit == "1" or inverted_b[i] == "1":  # when a or b is 1 and the other is 0
#                 if extra_1[0] == 1:
#                     extra_1 = extraTen(0)
#                     binary_answer.append(extra_1.pop(0))
#                     extra_1 = [0, 0]
#                     # print(f"extra_1 {i}: ", extra_1)
#                     # print("Binary answer: ", binary_answer)
#                 else:
#                     binary_answer.append(1)
#                     # print(f"extra_1 {i}: ", extra_1)
#                     # print("Binary answer: ", binary_answer)
#             else:  # when both a and b are 0
#                 if extra_1[0] == 1:
#                     binary_answer.append(extra_1.pop(0))
#                     extra_1 = [0, 0]
#                 else:
#                     binary_answer.append(0)
#
#             i += 1
#             # if i == 1:
#             #     inverted_b_spliced.append(inverted_b[1])
#             # else:
#         inverted_b_spliced = inverted_b[i:]
#         print("=========")
#         print("inverted list b: ", inverted_b_spliced)
#
#         for digit in inverted_b_spliced:
#             print("digit: ", digit)
#             print("extra 1: ", extra_1)
#             if digit == "1" and extra_1[0] == 1:
#                 extra_1 = extraTen(0)
#                 print("extra 1: ", extra_1)
#                 binary_answer.append(extra_1.pop(0))
#                 print("binary answer: ", binary_answer)
#             elif digit == "0" and extra_1[0] == 1:
#                 binary_answer.append(extra_1.pop(0))
#             elif digit == "0" and extra_1[0] == 0:
#                 binary_answer.append(0)
#             else:
#                 binary_answer.append(1)
#
#         while len(extra_1) > 0 and extra_1.count(1) >= 1:
#             binary_answer.append(extra_1.pop(0))
#         # print("Binary answer: ", binary_answer)
#
#         final_answer = invert(binary_answer)
#         # print("final answer: ", final_answer)
#
#         final_answer = "".join(str(digit) for digit in final_answer)
#
#         # print("final answer: ", final_answer)
#         return final_answer
#
#
# def extraTen(carry):
#     if carry == 0:
#         extra_1 = [0, 1]
#     else:
#         extra_1 = [1, 1]
#
#     return extra_1
#
#
# def invert(input_arr):
#     i = 0
#     # print("length of array: ", len(input_arr))
#     inverted_array = []
#     for char in input_arr:
#         inverted_array.append(input_arr[len(input_arr) - 1 - i])
#         i += 1
#     return inverted_array

#     return '{:b}'.format(int(a,2) + int(b,2))
#
# response = addBinary(a="101111", b="10")
#
# print(response)
