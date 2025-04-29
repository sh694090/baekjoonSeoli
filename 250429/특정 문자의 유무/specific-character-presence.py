from sys import stdin as s

inp = s.readline().strip()

ee_exists = 'No'
ab_exists = 'No'

if 'ee' in inp:
    ee_exists = 'Yes'

if 'ab' in inp:
    ab_exists = 'Yes'

print(ee_exists, ab_exists)