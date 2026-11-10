'''
    update trinket link at end
    url for students: 
        ?outputOnly=true&runOption=run

    probably depricate this, switched to html on website

'''

score = 0

# question 1
ans = input("\nWhat is the python function that displays *output* to the user? ")
if (ans == 'print') or (ans == 'print()'):
  print("Correct!")
  score = score + 1
elif ans == 'Print' or ans == 'Print()':
  print("Close. Remember that Python *is* case sensitive")
  score = score + 0.5
else:
  print("That is not correct. The correct answer was \"print\"")


# question 2
ans = input("\nWhat symbol belongs at the *end* of a conditional in python? ").lower()
if ans ==':' or ans == 'colon':
  print("Correct!")
  score = score + 1
else:
  print("That is not correct. The correct answer was \":\"")

  
# question 3
ans = input("\nWhat function allows us to get user *input* in python? ")
if ans =='input' or ans == 'input()':
  print("correct!")
  score = score + 1
elif ans == 'Input' or ans == 'Input()':
  print("Close. Remember that Python *is* case sensitive")
  score = score + 0.5
else:
  print("That is not correct. The correct answer was \"input\"")

  
# question 4
ans = input("\nWhen we use the input function, what *type* of data do we get? ")
if ans =='string' or ans == 'str':
  print("Correct!")
  score = score + 1
else:
  print("That is not correct. The correct answer was \"string\"")



# ---- results ----
if score >= 3:
  print("\nAwesome! Want to look at the source code for this program?")
  print("Copy/paste this link:")
  print("\thttps://trinket.pltw.org/python/0200a2de3d37")
  
else:
  print("\nRun this program again to retake this quiz.")