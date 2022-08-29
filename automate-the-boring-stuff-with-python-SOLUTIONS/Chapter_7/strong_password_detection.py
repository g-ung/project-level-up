#! python 3
'''
Strong Password Detection
Write a regular expression to make sure a password string is a
is a strong password.

REQUIREMENTS
1. Has at least eight characters
2. Contain at least one uppercase 
3. Contains at lease one lowercase character
4. Contains at least one digit
5. Contains at lease one special character (additona required added by me)

'''
import re

def pwd_evaulator(password):
    # regex to check password complexity requirements
    '''
    Use positive lookahead assertion in the regex to search
    for each password requirement
    REFERENCE:
    https://www.regular-expressions.info/lookaround.html
    https://automatetheboringstuff.com/2e/chapter7/
    '''
    is_strong_pwd = re.compile(r'''(
            ^(?=.*[a-z])        # match lowercase chars, 0 or more
            (?=.*[A-Z])         # match uppercase chars, 0 or more
            (?=.*[0-9])         # match digit, 0 or more
            (?=.*[!@#$%^&*+])   # special character, 0 or more
            .{8,}$              # match at least 8 chars
            )''', re.VERBOSE)
    
    pwd_evaluation = is_strong_pwd.fullmatch(password)
    
    if pwd_evaluation: 
        return True

def main():
    print("Please enter your password. Password word must be at least eight charaters long. Have uppercase and lowercase, one special character, and a digit\n")
    check_pwd = pwd_evaulator(input("Please enter your password: "))
    
    if check_pwd == True:
        print("Your password meets the password requirement, password is: STRONG")
    else:
        print("Your password does not meet the password requirements!")

if __name__ == '__main__':
    main()
