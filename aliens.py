#aliens.py

#alien_0 = {'color' : 'green', 'points' : 5}
#print(alien_0)
#
#alien_0['x_pos'] = 10
#alien_0['y_pos'] = 25
#print(alien_0)
#
#alien_0['color'] = 'yellow'
#print(alien_0['color'])
#
#alien_0['speed'] = 'medium'
#
#if alien_0['speed'] == 'low':
#	x_inc = 1
#elif alien_0['speed'] == 'medium':
#	x_inc = 2
#else:
#	x_inc = 3
#
#alien_0['x_pos'] = alien_0['x_pos'] + x_inc
#print(f"New position: {alien_0['x_pos']}")

#create an empty list of aliens
aliens = []

#create 30 green aliens
for alien_number in range(30): #range(30) means that 'for' should iterate 30 times
	new_alien = {'color': 'green', 'points': 5, 'speed': 'low'} #in dictionaries are used 'key : value' couples. You can adress to both of them.
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien ['color'] == 'green':
		alien['color'] == 'yellow'
		alien['points'] == 10
		alien['speed'] == 'medium'


#Show first 5 aliens
for alien in aliens [:5]:
		print(alien)
print("...")

#Show total created aliens
print(f"Total number of aliens: {len(aliens)}")