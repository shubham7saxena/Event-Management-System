from .models import Profile, Event
from collections import OrderedDict

#graph = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6},'g': {5, 6, 7}, 'h': {8}}


def Max_bpm(graph):

	connected = {}
	for u in graph:
		for v in graph[u]:
			if v not in connected:
				connected[v] = u
				break
	
	while 1:
		preds = {}
		unconnected = []
		pred = dict([(u,unconnected) for u in graph])
		for v in connected:
			del pred[connected[v]]
		layer = list(pred)

		while layer and not unconnected:
			newLayer = {}
			for u in layer:
				for v in graph[u]:
					if v not in preds:
						newLayer.setdefault(v,[]).append(u)
			layer = []
			for v in newLayer:
				preds[v] = newLayer[v]
				if v in connected:
					layer.append(connected[v])
					pred[connected[v]] = v
				else:
					unconnected.append(v)

		if not unconnected:
			unlayered = {}
			for u in graph:
				for v in graph[u]:
					if v not in preds:
						unlayered[v] = None
			return (connected,list(pred),list(unlayered))

		def recurse(v):
			if v in preds:
				L = preds[v]
				del preds[v]
				for u in L:
					if u in pred:
						pu = pred[u]
						del pred[u]
						if pu is unconnected or recurse(pu):
							connected[v] = u
							return 1
			return 0

		for v in unconnected: recurse(v)




def execute(event_list,Venue):
	graph_dict={}
	

	for event in event_list:
		first = str(event.first_day_preference)+str(event.first_time_preference)
		second = str(event.second_day_preference)+str(event.second_time_preference)
		third = str(event.third_day_preference)+str(event.third_time_preference)

		if event.Venue == Venue:			
			
			graph_dict[event.name]=[first,second,third]
		
		print graph_dict
			

	timing,left_events,y= Max_bpm(graph_dict)

	for time in timing:
		for event in event_list:
			if timing[time] == event.name:
				event.Actual_day=time[0]
				event.Actual_time=time[1]

	return left_events


def bpm(event_list):

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
		print x.Actual_time


	return left_events
	
	
	
	
	
	
	


	
