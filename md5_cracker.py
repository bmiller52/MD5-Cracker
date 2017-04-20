import md5

counter = 1

pass_in = raw_input("Please Enter the MD5 Hash: ")
pwfile = raw_input("Please Enter the File Name: ")

try:
    pwfile = open(pwfile, "r")
except:
    print("\nCould not Find File")
    quit()

for password in pwfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    print("Password Attempt %d: %s") % (counter, password.strip())

    counter += 1

    if pass_in == filemd5:
        print("\nMatch Found. \nPassword is: %s") % password
        break

else:
    print("\nPassword Not Found")
