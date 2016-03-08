from .models import Profile, Event
from collections import OrderedDict

#graph = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6},'g': {5, 6, 7}, 'h': {8}}


def Max_bpm(graph):
		matching = {}
		for u in graph:
			for v in graph[u]:
				if v not in matching:
					matching[v] = u
					break
		
		while 1:
			# structure residual graph into layers
			# pred[u] gives the neighbor in the previous layer for u in U
			# preds[v] gives a list of neighbors in the previous layer for v in V
			# unmatched gives a list of unmatched vertices in final layer of V,
			# and is also used as a flag value for pred[u] when u is in the first layer
			preds = {}
			unmatched = []
			pred = dict([(u,unmatched) for u in graph])
			for v in matching:
				del pred[matching[v]]
			layer = list(pred)
			
			# repeatedly extend layering structure by another pair of layers
			while layer and not unmatched:
				newLayer = {}
				for u in layer:
					for v in graph[u]:
						if v not in preds:
							newLayer.setdefault(v,[]).append(u)
				layer = []
				for v in newLayer:
					preds[v] = newLayer[v]
					if v in matching:
						layer.append(matching[v])
						pred[matching[v]] = v
					else:
						unmatched.append(v)
			
			# did we finish layering without finding any alternating paths?
			if not unmatched:
				unlayered = {}
				for u in graph:
					for v in graph[u]:
						if v not in preds:
							unlayered[v] = None
				return (matching,list(pred),list(unlayered))

			# recursively search backward through layers to find alternating paths
			# recursion returns true if found path, false otherwise
			def recurse(v):
				if v in preds:
					L = preds[v]
					del preds[v]
					for u in L:
						if u in pred:
							pu = pred[u]
							del pred[u]
							if pu is unmatched or recurse(pu):
								matching[v] = u
								return 1
				return 0

			for v in unmatched: recurse(v)




def execute(event_list,Venue):
	graph_dict={}
	

	for event in event_list:
		first = str(event.first_day_preference)+str(event.first_time_preference)
		second = str(event.second_day_preference)+str(event.second_time_preference)
		third = str(event.third_day_preference)+str(event.third_time_preference)

		if event.Venue == Venue:			
			
			graph_dict[event.name]=[first,second,third]
		
		
			
	print graph_dict
	timing,y,x= Max_bpm(graph_dict)
	print timing


	left_events=[]
	dict_events={}


	for time in timing:
		dict_events[timing[time]]=time

	print "=========================================================================="
	print dict_events
	print "=========================================================================="

	for event in event_list:
		if event.Venue == Venue:		
			if event.name in dict_events:
				 event.Actual_day=dict_events[event.name][0]
	 			 event.Actual_time=dict_events[event.name][1]
	 		else:
	 			left_events.append(event.name)
	 			event.Actual_day='$'
	 			event.Actual_time='$'

	print left_events

	# print "=========================================================================="

	# for time in timing:
	# 	for event in event_list:
	# 		if timing[time] == event.name:
	# 			event.Actual_day=time[0]
	# 			event.Actual_time=time[1]

	return left_events


def bpm(event_list):

	# execute(event_list,'1')

	left_events={}

	left_events=execute(event_list,'1')
	left_events.append(execute(event_list,'2'))
	left_events.append(execute(event_list,'3'))
	left_events.append(execute(event_list,'4'))
	left_events.append(execute(event_list,'5'))

	for event in event_list:
		x = Event.objects.get(name = event.name)


		x.past_Actual_time=x.Actual_time
		x.past_Actual_day=x.Actual_day
		
		x.Actual_time=event.Actual_time
		x.Actual_day=event.Actual_day

		x.save()
		x = Event.objects.get(name = event.name)	


	return left_events
	
	
	
	
	
	
	


	
