def valid_parentheses(string):
    brack_count = 0
    for x in string:
        if x == "(":
            brack_count +=1
            if brack_count < 0:
                return False
        if x == ")":
            brack_count -=1
            if brack_count < 0:
                return False
    if brack_count != 0:
        return False
    else:
        return True

    print(brack_count)



        # initalise parenthesis count
        # iterate through string, increasing or decreasing count for 'left' or 'right' paranthesis
        # while count is above 0, return true unless count is odd
        # reutn false if count falls below zero

print(valid_parentheses("  ("))
print(valid_parentheses(''))
print(valid_parentheses(")test"))
print(valid_parentheses("hi())("))


# string
#     left_p = 0
#     right_p = 0
#     if string:
#         if (string[0] ==")"):
#             return False
#         if (string[-1] == "("):
#             return False
#         if "(" or ")" in string:
#             for x in string:
#                 if x == "(":
#                     left_p += 1
#                 if x == ")":
#                     right_p += 1
#             # print(f"left_p ={left_p}",f"right_p ={right_p}")
#             if left_p != right_p:
#                 return False
#             else:
#                 return True
#         else:
#             return True
#     else:
#         return True
