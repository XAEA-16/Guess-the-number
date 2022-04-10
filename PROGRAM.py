import numpy as np

count=0
scount=0
while True:
  a=input()
  if a=="":
    break
  elif int(a)<0:
    break
  else:
    b=int(np.random.randint(3,size=1))
    d=int(a)
    if d==b:

      scount+=1
      print(f"you are doing great your total winning prcentage is increasing ")
      a=int(input('1 TO START | 0 TO STOP'))
      if a==1:
        continue
      else:
        print(f'your total winning percentage is {(scount/scount+count)}  percent out of {scount+count} gussing')
        break

    else:
      count+=1
      print(f"you where close the number was {b}")
      print(" try again")
