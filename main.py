clear()
while True:
	
		for i in range (get_world_size()):
			for j in range(get_world_size()):
				harvest()
				if num_items(Items.Hay) >3000:
					if i>j:
						plant(Entities.Bush)
					elif i==j:
						plant(Entities.Tree)
					else :
						if get_ground_type() != Grounds.Soil:
							till()
						plant(Entities.Carrot)				
				move(North)
			move(East)