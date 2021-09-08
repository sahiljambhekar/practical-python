# bounce.py
#
# Exercise 1.5
BOUNCES=10
height=60
for i in range(BOUNCES):
    bounce_no = i +1
    print("{:2} {:7.4f}".format(bounce_no,height))
    height = (height * 3)/5
