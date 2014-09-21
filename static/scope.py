spam = 42

def eggs():
    spam = 99 # spam in this function is local
    print('In eggs():', spam)

def ham():
    print('In ham():', spam) # spam in this function is global

def bacon():
    global spam # spam in this function is global
    print('In bacon():', spam)
    spam = 0

def CRASH():
    print(spam) # spam in this function is local
    spam = 0

print(spam)
eggs()
print(spam)
ham()
print(spam)
bacon()
print(spam)
CRASH()