# take input from user

s=int(input('enter total number of seconds:'))

# calculate hours minutes and seconds

hours= s//3600

remainings= s%3600

minutes=remainings // 60

seconds=remainings%60

# display results

print(f'hours:{hours} minutes:{minutes} seconds:{seconds}')
