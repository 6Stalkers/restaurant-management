print(
                '''menu
      s.no. item        price
      1.    pizza       100/-
      2.    tikki       70/-
      3.    panipuri    50/-
      4.    rasgulla    14/-(1 piece)
      5.    gulab jamun 14/-(1 piece)
      6.    ckn. tikka  180/-
      7.    mtn. chaap  250/-
      8.    burger      50/-
      9.    lassi       40/-
      10.   kulfi faluda70/-'''
      )

ch=int(input("enter your choice"))
for i in range (1,11,1):
    if ch!=0:
       o=int(input("enter your order"))
    if o==1:
           Q= int(input("enter quantity"))
           O= "PIZZA"
           pr= Q*100
    elif o==2:
            Q=int(input("enter quantity"))
            O="TIKKI"
            pr= Q*70
    elif o==3: 
            Q=int(input("enter quantity"))
            O="PANIPURI"