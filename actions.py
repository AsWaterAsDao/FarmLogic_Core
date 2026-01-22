clear()
count = 0
last_val = None
def manage_pumpkin():
	global count
	global last_val
	current_val = measure()
	if get_ground_type() != Grounds.Soil:
		till()
		plant(Entities.Pumpkin)		
	elif current_val == None :
			harvest()
			plant(Entities.Pumpkin)
	else:
		if current_val == last_val and current_val != None: 
			count += 1
		else:
			count = 1
		if count == 6: 
			harvest()
			count = 0
		last_val = current_val
def manage_carrot():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Carrot)
	
def manage_grass():
	if get_ground_type()!=Grounds.Grassland:
		till()
def manage_sunflower():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Sunflower)


	
	