def job_Schedule(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    n=len(jobs)
    max_deadline=max(job[1] for job in jobs)
    job_array=[-1]*max_deadline
    for job_id,dead,prof in jobs:
        for slots in range(max_deadline-1,-1,-1):
            if(job_array[slots]==-1):
                job_array[slots]=job_id
                break
    return job_array        


jobs=[('J1',3,30),('J2',1,10),('J3',2,20),('J4',3,50),('J5',2,40)]

print(job_Schedule(jobs))