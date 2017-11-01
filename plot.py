import csv
import matplotlib.pyplot as plt
import numpy as np

def column(matrix, i):
	return np.array([row[i] for row in matrix])

data = []

with open('data.dat', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	spamreader.next()
	for row in spamreader:
		data.append(np.array(row,dtype=int))
		
plt.xkcd()

mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)
plt.gcf().subplots_adjust(bottom=0.15)

year = column(data,0)
all = column(data,1)
fails = column(data,2)


ind = np.arange(len(year)) 
width = 0.35      

p1 = plt.bar(ind, all, width, color='#d62728')
p2 = plt.bar(ind, fails, width)

plt.ylabel('Students')
plt.xlabel('Year')
plt.title('Students per year')
plt.xticks(ind , year)
plt.yticks(np.arange(0, max(all)+2, 1))
plt.legend((p1[0], p2[0]), ('Pass', 'Fail'),loc=2)

plt.savefig('students_per_year.png', format='png', dpi=150)

plt.close()


request = column(data,4)
merged = column(data,5)

ind = np.arange(len(year)) 
width = 0.35      

p1 = plt.bar(ind, request, width, color='#d62728')
p2 = plt.bar(ind, merged, width)
plt.gcf().subplots_adjust(bottom=0.15)

plt.ylabel('Pull requests')
plt.xlabel('Year')
plt.title('Pull requests and merged pull requests')
plt.xticks(ind , year)
plt.yticks(np.arange(0, max(request)+2, 5))
plt.legend((p1[0], p2[0]), ('Requested', 'Merged'),loc=2)

plt.savefig('pull_per_year.png', format='png', dpi=150)
