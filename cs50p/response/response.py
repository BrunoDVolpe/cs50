#using either validator-collection (pip install validator-collection) or validators (pip install validators)
# from PyPI (vou usar validators)
#pip install validators
import validators

email = input("What's your email address? ")
if validators.email(email):
    print("Valid")
else:
    print("Invalid")