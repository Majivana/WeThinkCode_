# ask user for their name
name = input ("what is your name?").strip().title()

# remove whitespace from str and capitalize user name
#name = name.strip().title()

#capitalize user name
# name = name.capitalize()
# name = name.title() this is used eg: name and surname
first, last = name.split(" ")

# say hello to user
print (f"hello, {first}")