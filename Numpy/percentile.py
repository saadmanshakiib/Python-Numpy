import numpy as np

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
#What is the age that 90% of the people are younger than?
print(f"The age from where 90% of the people are younger than : ${np.percentile(ages,90)}")

scores = [45, 52, 61, 68, 72, 75, 78, 82, 85, 90, 92, 95, 98]
# find top 10% marks
print(f"Top 10% marks : ${np.percentile(scores,90)}")

# find lowest 10% marks
print(f"Lowest 10% marks : ${np.percentile(scores,10)}")

