#Finger exercise: Write a program that asks the user to input 10 integers, and then
#prints the largest odd number that was entered. If no odd number was entered, it
#should print a message to that effect.

left = 10
nums = []
while(left > 0):
	newNumber = int(input('Insert a interger, I need', left,':'))
	nums.append(newNumber)

totalEven = 0
for interger in nums:
	if interger % 2 == 0:
		totalEven += 1

if totalEven == 10 :
	print("No odd number was entered")
else:
	for num in sorted(nums, reverse = True):
		if num % 2 != 0:
			print('Largest odd number entered:',num)
			break
