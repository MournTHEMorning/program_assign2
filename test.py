# for testing purposes. Will be deleted later
print(-0%20)

#testing
#testing2 

#from here: https://docs.python.org/3/tutorial/errors.html
counter=0

while True:
#counter = 0, if you put this here, then counter will reset when looped, because try doesn't loop it's the while loop
    try: #try starts here, like try this, but the loop happens throughout
        i=int(input("hey: "))
        print("cool")
        break
    except ValueError: # the thing that captures the error
        counter+=1

    finally: #will print or do no matter what happens to try 
        print("hehe {}!".format(counter))