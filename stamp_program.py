"""
start
get the numbers of sheets
sheets / 5
round answer to next number 
output the result to tghe user
end
"""


def calculate(sheet):
    answer = sheet / 5
    rounded = round(answer)
    print("Sheet is : ", sheet)
    print("The answer is: ", answer)
    print("Rounded is : ", rounded)
    print("================================")
    return rounded


output = calculate(10000)

print("The return statement is: ", output)
