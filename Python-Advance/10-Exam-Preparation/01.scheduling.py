jobs = [int(el) for el in input().split(', ')]
job_index = int(input())

total_cycles = 0
is_finished = False
count_indexes = []

search_job = jobs.pop(job_index)
jobs.insert(job_index, search_job + 0.5)

for i in sorted(jobs):
    if i == int(i):
        total_cycles += i
    else:
        ind = int(i)
        total_cycles += ind
        break
print(total_cycles)