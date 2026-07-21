password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1

if password.lower() != password and password.upper() !=password :
    score += 1
    
for i in password:
    if i.isdigit():
        score +=1
        break
        
for i in password :
    if i in "@#$%":
        score += 1   
        break        

if score <= 1:
    print("Score:", score, "/4 - Weak")
elif score <= 3:
    print("Score:", score, "/4 - Okay")
else:
    print("Score:", score, "/4 - Strong")