import secrets
import string
def gennerate_password(length: int,has_uppercase: bool=True,has_numbers: bool=True,has_special: bool=True):
    pass
lowercase=string.ascii_lowercase
uppercase=string.ascii_uppercase
digits=string.digits
special_chars=string.punctuation

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length (8-32 characters): "))
            if 8 <= length <= 32:
                return length
            else:
                print("Password length must be between 8 and 32 characters.")
        except ValueError:
            print("Please enter a valid number.")

length=get_password_length()
char_sets=[lowercase]

if True:
    char_sets.append(uppercase)
if True:
    char_sets.append(digits)
if True:
    char_sets.append(special_chars)

base=[]
for char_set in char_sets:
    base.append(secrets.choice(char_set))
all_chars=''.join(char_sets)
remaining_length=length-len(base)

for i in range(remaining_length):
    random_char=secrets.choice(all_chars)
    base.append(random_char)

secrets.SystemRandom().shuffle(base)
print (''.join(base))