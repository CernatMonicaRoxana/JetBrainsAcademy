# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
groups_no = int(input())

students_no = [int(input()) for i in range(0, groups_no)]
students_no.extend([None] * (len(groups) - groups_no))

print(dict(map(lambda key, value: (key, value), groups, students_no)))

print('18' + '3')