import actions
while True:
	for i in range (get_world_size()):
		for j in range (get_world_size()):
			if i<6 and j<6:
				actions.manage_pumpkin()
			else:
				harvest()
				if i>=6 and j<6:
					if num_items(Items.Hay)<50000:
						actions.manage_grass()
					else:
						actions.manage_sunflower()
				elif i<6 and j>=6:
					actions.manage_carrot()
				else:
					plant(Entities.Bush)
			move(North)
		move(East)

