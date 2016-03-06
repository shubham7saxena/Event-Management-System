from hopcroftkarp import HopcroftKarp
#graph = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6},'g': {5, 6, 7}, 'h': {8}}



# HopcroftKarp(graph).maximum_matching()


def bpm(event_list):
	graph_dict={}
	for event in event_list:
		print (event.name)
		print (event.first_time_preference)
		print (event.Actual_time)
		graph_dict[event.name]={event.first_time_preference,event.second_time_preference,event.third_time_preference}
	
	print graph_dict
	print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"

	timing= HopcroftKarp(graph_dict).maximum_matching()
	print timing

	for event in event_list:
		if (event.name).encode('ascii', 'ignore') in timing:
			event.Actual_time=timing[(event.name).encode('ascii', 'ignore')]
	
