
# Control flow is like a decisionmaking process that a computer makes based on the information given to it
# the decision can be based on the result of an equation, the value of a variable, or something else

x = 11

if x > 10:
    print("x is bigger than 10!")
elif x < 10:
    print("x is less than or equal to 10!")
else:
    print("x is 10!")

# with if elif else statements, only one will trigger at a time
# these are good for when you know your variable will only pass one of the conditions
# example: x cannot be both greater than and less than 10...

y = 11
if y > 10:
    print("y is bigger than 10!")
if y > 15:
    print("y is also bigger than 15!")

# if statements don't rely on each other, so both of these can trigger
# these are good for when a variable could pass two or more conditions
# example: y can be both greater than 10 and greater than 15