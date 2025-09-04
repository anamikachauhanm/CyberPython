#write a program to detect spam msgs like "buy now", "click here", "subscribe now"

spam_keywords = ["buy now", "click here", "subscribe now"]
message = input("Enter your message: ")

'''if(spam_keywords[0] in message.lower() or 
   spam_keywords[1] in message.lower() or 
   spam_keywords[2] in message.lower()):
    print("This message is considered spam.")'''
# Using any() function for better readability

if any (keyword in message.lower() for keyword in spam_keywords):
    print("This message is considered spam.")

else :
    print("this is not considered spam")    