from re import L


a="hello coders"

print("Congratulation you have successfully entered the lottery and got a chance to win the lottery!! ")
print("select a word from: ",a)
inputs=input()
if inputs==a[0].lower() or inputs==a[1].lower() or inputs==a[4].lower() or inputs==a[6].lower() or inputs==a[8].lower() :

    print("Congratulations!!! You hit the bull's eye!!")
else : 
    print("Better luck next time...")c