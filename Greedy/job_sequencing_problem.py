def job_sequencing(jobs, n):
    # sorting the jobs based on the profit as we need to maximize the profit
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Since we need to increase profit , we perfrom teh job on its last day
    # so that we have the previous days available with us to perform other jobs
    # for example if deadline is 6, we perfrom on 6th day . if 6th days is occupied
    # we fill the 5yh day and so on

    # get the max possible deadline value, this is the max days for all the jobs
    max_days = max(i[1] for i in jobs)

    # create an array of size max deadline and default value as -1
    jobs_days = [-1] * (max_days + 1)

    # to get the jobs count and profit
    count, total_profit = 0, 0

    # iterate over all jobs
    for sn, deadline, profit in jobs:
        # check which is the last available day of deadline is available
        for jb in range(deadline, 0, -1): 
            # fill the available slot and increase the count and profit
            # once a job is allotted break the loop and move to next job
            if jobs_days[jb] == -1:
                jobs_days[jb] = sn
                count += 1
                total_profit += profit
                break

    return count, total_profit


n = 4
jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]

n = 5
jobs = [[1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15]]
print(job_sequencing(jobs, n))
