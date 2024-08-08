import itertools
from itertools import combinations
Kevin={
    "Halsey","Taylor Swift","Mitski","joji","Shawn Mendes","Sabrina Carpenter","Nicky Minaj","Conan Gray","One Direction","Justin Bieber"
      },
Stuart={
    "kendric Lamar","Steve Lacy","Tyler The Creator","Joji","TheWeekend","Coldplay","Kenye West","Travis Scott","Frank Ocean","Brent Faiyaz"
       },
Bob={
    "Conan Gray","joji","Dove Cameron","Mitski","Arctic Monkeys","Steve Lacy","kendric Lamar","Isabel LaRosa","Shawn Mendes","Coldplay"
    },
Edith={
    "Metallica","Billie Eilish","TheWeekend","Mitski","NF","Conan Gray","kendric Lamar","Nicky Minaj","Kenye West","Coldpay"
      }
DJs=[Kevin,Stuart,Bob,Edith]
    
pairs=(itertools.combinations(DJs,2))
# pairs={(i,j),(i,j),(i,j),(),}
pairs_with_overlap=[]
overall_percentage=[]

def calculate_intersection(set1,set2):
    intersection=set1.intersection(set2)
    return (len(intersection)/len(set1))*100,
    return (len(intersection)/len(set2))*100


for items in pairs:
    overlap_percentage1,overlap_percentage2 = calculate_intersection(items[0], items[1])

    
    if overlap_percentage1>=30 & overlap_percentage2>=30:
        overall_overlap=max(overlap_percentage1,overlap_percentage2)
        pairs_with_overlap.append(items)
        overall_percentage.append(overall_overlap)

print(pairs_with_overlap)       
