# n = int(input())
# arr = map(int, input().split())
# listy = []
# i = 0
#
# for digit in arr:
#     print(digit)
#     listy.append(digit)
#
# listy.sort(reverse=True)
# second = listy[0]
#
# while second == listy[0]:
#     if listy[i + 1] == listy[i]:
#         print(f"listy[{i}]: ", listy[i])
#         i += 1
#
#         if i == len(listy):
#             break
#     else:
#         second = listy[i]
# print("the list only has one number")
#
# print("listy: ", listy)
# print("second: ", second)


# class MathUtils:
#
#     @staticmethod
#     def average(a, b):
#         print(f"a: {a} | b: {b}")
#         return (2 + 1) / 2
#
#
# print(MathUtils.average(2, 1))
# import math
#
#
# def find_roots(a, b, c):
#     quadratic_pos = ((-b) + (math.sqrt((b ** 2) - 4 * a * c))) / (2 * a)
#     quadratic_neg = ((-b) - (math.sqrt((b ** 2) - 4 * a * c))) / (2 * a)
#
#     answer_tuple = (quadratic_pos, quadratic_neg)
#
#     return answer_tuple
#
#
# print(find_roots(2, 10, 8))

#
# class IceCreamMachine:
#
#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings
#
#     def scoops(self):
#         list_of_combos = []
#
#         for ingredient_1 in self.toppings:
#             for ingredient_2 in self.ingredients:
#                 list_of_combos.append([ingredient_2, ingredient_1])
#
#         return list_of_combos
#
#
# if __name__ == "__main__":
#     machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
#     print(machine.scoops())  # should print: [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
a = [1, 2, 3, 4, 5, 6, 7]
n = 7
a.sort()
print(f"a: {a}")
print(f"n: {n}")
print(f"length of a: {len(a)}")
mid = int(n / 2)
print(f"mid: {mid}")
# a[mid] = 4, a[n-1] = 7
a[mid] = a[n - 1]
a[n - 1] = a[mid]
print(f"a[mid]: {a[mid]} | a[n - 1]: {a[n - 1]}")
a[mid], a[n - 1] = a[n - 1], a[mid]

st = mid + 1
ed = n - 2
print(f"st: {st} | ed: {ed}")
print(f"a[st]: {a[st]}")
print(f"a[ed]: {a[ed]}")
while st <= ed:
    # a[5] = 7
    # a[ed] = a[st]
    a[st], a[ed] = a[ed], a[st]
    st = st + 1
    ed = ed + 1
