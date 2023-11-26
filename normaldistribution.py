

import csv
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
data = []
with open('random_numbers_summary.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        if len(row) == 2:
            range_name, count = row
            data.append((range_name, int(count)))

# Extract ranges and counts
ranges, counts = zip(*data)
counts = np.array(counts)

# Create a mapping from range names to their midpoints
range_midpoints = [int(range.split('-')[0]) + 5 for range in ranges]

# Calculate the mean and standard deviation
mean = counts.mean()
stddev = counts.std()

# Generate a KDE plot based on range midpoints
sns.set_style("whitegrid")
sns.kdeplot(range_midpoints, label='KDE Plot', color='blue')

plt.xlabel('Range Midpoints')
plt.ylabel('Density')
plt.title('Kernel Density Estimation Plot for Ranges')
plt.legend()
plt.tight_layout()

plt.show()

