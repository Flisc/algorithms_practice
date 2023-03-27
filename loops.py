myStr = "This is a great day!"
for x in myStr:
    print(x, end=" ")
    if x == "d":
        break

print("\n\n")

# remember: range(start, stop[, step])
for i in range(10, 50, 5):
    print(i, sep=",", end="...")

print("\n\n")
# list =[1,2,3, 'asd', 'last']
n = int(input("Enter the desired number of iterations!\n"))
for i in range(n):
    if i >= 4:
        break
    print(i + 1)
else:
    print("Nice! You wanted less than 5 iterations.")
