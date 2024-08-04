# (arriving_time,prep_time)
customer=[
    (5,2),
    (5,4),
    (10,3),
    (20,1)
]
current_time=0
total_waiting_time=0

for arriving_time,prep_time in customer:
    starting_time=max(current_time,arriving_time)
    finishing_time=starting_time + prep_time
    waiting_time=finishing_time-arriving_time
    total_waiting_time+=waiting_time
    current_time=finishing_time
average_waiting_time=total_waiting_time/len(customer)
print(total_waiting_time)
print(average_waiting_time)
    


