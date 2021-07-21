# string concatenation (putting strings together)
# suppose we want to create a string with a blank
# like "today is ___"
# day = "Tuesday"

# a few ways to do this
# print("today is " + day)
# print("today is {}".format(day))
# print(f"today is {day}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
celebrity = input("Famous person: ")

madlib = f"Developing code is {adj}! It's exciting because \
    I enjoy {verb1}. Be well and {verb2} like {celebrity}."

print(madlib)