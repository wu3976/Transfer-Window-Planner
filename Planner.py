import PeriodDictionary
name1=str(input ("The first planet/satellite: "))
name2=str(input ("The second planet/satellite: "))
index1=0
index2=0
period1=0.0
period2=0.0
p1getted=False
p2getted=False

while index1< len(PeriodDictionary.period_dict) and not(p1getted):
    if name1==PeriodDictionary.period_dict[index1][0]:
        period1=PeriodDictionary.period_dict[index1][1]
        p1getted=True
    index1+=1


while index2< len(PeriodDictionary.period_dict) and not(p2getted):
    if name2==PeriodDictionary.period_dict[index2][0]:
        period2=PeriodDictionary.period_dict[index2][1]
        p2getted=True
    index2+=1


if not (p1getted):
    period1=name1

if not (p2getted):
    period2=name2

half_period_h=pow(pow(period1, 2/3)+pow (period2, 2/3), 1.5)/pow(32, 0.5)
angle_in_degree=(180 - (360 * half_period_h / period2)) % 360
if angle_in_degree>180:
    angle_in_degree-=360

print("degree: "+str(angle_in_degree)+"\nTransfer time: "+str(half_period_h))