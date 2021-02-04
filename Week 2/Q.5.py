''' Q5. Captchas are tools you can use to differentiate between real users and automated users,
such as bots. Create a tuple of 5 captcha in python. Your task is to randomly display a
captcha from the tuple. Then enter the captcha. If the same captcha was entered, then display
“You are not a robot”, else display “You are a robot”'''

import random
captchas = ('Rh7yA','ju97g','gP0h3','mn0Gl','Ril98')
t = random.choice(captchas)
print("Type this Captcha code:",t)

cap = input()
if(cap==t):
    print("You are not a robot")
else:
    print("You are a robot")
