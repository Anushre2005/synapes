gadgets=[
    ("Explosive Batarangs",3,True),
    ("Batarangs",5,True),
    ("Smoke Pellets",0,False),
    ("Tear Gas Grenades",2,True),
    ("Night Vision Goggles",1,True),
    ("Batclaw",0,False),
    ("Grapple Gun",3,True),
    ("Batsignal ",0,False),
    ("Utility Belt",1,True),
    ("Batmobile Tires",4,True)

]
gadgets.sort(key=lambda x:x[0] ,reverse=False)
gadgets.sort(key=lambda x:x[1] ,reverse=True)

for row in gadgets:
    print(row)
