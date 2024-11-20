#there are two players hand and broker.
#The goal is to score less than the broker.
# if it is greater than 17.
import random as rd
li=[1,2,3,4,5,6,7,8,9,10,10,10,10]
hli=[]
broli=["close","close"]
broli[0]=(rd.choice(li))
print()
print(f"brokers card\'s are {broli}")
print()
broli[1]=(rd.choice(li))
hli.append(rd.choice(li))
print(f"your card is {hli}")
print()
end=0
print("HIT={take another one card}")
print()
print("stay={Don\'t take another one card}")
print()
while( end==0 ):


    val=1
    x=1
    while(x==1 and sum(hli)<22):

        hli.append(rd.choice(li))

        print(f"your card\'s are {hli}")
        sh=sum(hli)
        print("Your  sum is :",sh)
        print()
        if (sh>21):
            print("You lose the1 game")
            val=0
            break
        
        elif (sh==21):
            print("You won the1 game")
            val=0
            break
        x=int(input("If you want to \"hit\" enter \"1\" else enter \"0\"  to stay "))
    if val:
        d=input("enter to see The broker\'s side game")
        while(sum(broli)<22):
            print(f"brokers card\'s are {broli}")

            sb=sum(broli)
            print()
            print("the broker sum is :",sb)
            print()

            if (sb>21):
                print("Broker lost2 th game")
                break
            elif sb>sh:
                print("Broker won2 th game")
                break
            elif sb < sh and sb<21:
                broli.append(rd.choice(li))

            d=input("enter to see step by step")

           
        


    end=1










