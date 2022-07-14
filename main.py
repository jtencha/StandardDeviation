import math

print('Calculating Standard Deviation: Input lists as "number,number,numner". ')
print("Example: 45,23,34\n")

inputed = input("Enter a list of values to calculate the Standard Deviation of: ")

final = str(inputed).split(",")

#Calculate mean
y = 0
mean = 0
for x in final:
  mean += float(x)
  y += 1

mean = mean / y

#Difference from the mean
diff_sq = 0.0
for i in final:
  diff_sq += (float(i) - float(mean)) ** 2

#Final steps
print("\n\nThe standard deviation for {0} is {1}".format(final, str(round(math.sqrt(diff_sq / (y - 1)), 2))))


  
