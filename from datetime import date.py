from datetime import date
f_date = date(1994, 12, 30)
l_date = date(2022, 7, 4)
delta = l_date - f_date
cnt_year=delta.days//365
print("Year: ",cnt_year)
cnt_mon=(delta.days%365)//30
print("Month: ",cnt_mon)
cnt_days=delta.days-((cnt_year*365)+(cnt_mon*30))
print("Days: ",cnt_days)


#New Solution
a = date(1991, 7, 20)
b = date(1999, 6, 6)

years = b.year - a.year
if b.month < a.month:
    years = years - 1
    months = (b.month+12) - a.month
else:
    months = b.month - a.month
if b.day<a.day:
    months=months-1
    #b.day+=30
    days = b.day - a.day 

print('{0} years, {1} months, {2} days'.format(years, months, days))