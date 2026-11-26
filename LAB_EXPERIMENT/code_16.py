def activity_Selection(activity_list):
    activity_list.sort(key=lambda x: x[2])
    selected_activitiy = [activity_list[0][0]]
    finish_time = activity_list[0][2]

    for activity in activity_list[1:]:
        if activity[1] >= finish_time:
            selected_activitiy.append(activity)
            finish_time = activity[2]
    return selected_activitiy        

activity_list=[('A1',2,4),('A2',3,5),('A3',1,3),('A4',5,7),('A5',8,9),('A6',5,9)]
print(activity_Selection(activity_list))
