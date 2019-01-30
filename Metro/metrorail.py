import random as r

class Line:
	def __init__(self, long_name, colour, train_num_prefix):
		"""
		class Line will hold and manipulate data on train lines such as what stations
		are on each individual line.
		"""
		self.long_name = long_name
		self.colour = colour
		self.train_num_prefix = train_num_prefix
		self.stations = []
		self.nb_stations = []
		self.end_points = []
		self.travel_times = [[], []]


	def __str__(self):
		return "Train lines {}".format(self.long_name)

	def set_stations(self, stations):
		'''
		Checks stations and matches with corresponding line.
		appends it to self.stations
		'''
		for z in stations:
			self.stations.append(z)
			z.lines.append(self)
			if len(z.lines) > 1:
				z.is_interchange=True
		self.end_points = [self.stations[-1], self.stations[0]]

	def get_stations(self):
		"""
		returns the name of stations on line
		"""
		names_stations = []
		for i in self.stations:
			names_stations.append(i.name)
		return names_stations

	def set_random_travel_times(self):
		for i in range(len(self.stations)-1):
			self.travel_times[0].append(r.randrange(40,120,1))
			self.travel_times[1].append(r.randrange(40,120,1))
		return self.travel_times	

	def has_station(self, stn):
		"""
		returns True or False if station is on current line or not.
		"""
		return stn in self.stations

	def index_station(self, stn):
		for i in range(len(self.stations)):
			if stn == self.stations[i]:
				return i
		return -1

	def number_stops_and_direction(self, stn_from, stn_to):
		"""
		Returns a list containing 2 elements. 1 Being the number of stops. 2 Being the end station of current line.
		"""
		
		if stn_from not in self.stations or stn_to not in self.stations:
			return [-1, None]

		index_from = self.index_station(stn_from)
		index_to = self.index_station(stn_to)
		'''
		#Debug
		print("From {0}, to {1}".format(index_from, index_to))
		for i in self.stations:
			print(i.name)
		'''
		nb_stops = []
		direction = []
		ans = index_to - index_from
		if ans < 0:
				ans *= -1
		nb_stops.append(ans)

		direction.append(self.end_points[1].name)
		return [nb_stops, direction]


class Station:
	def __init__(self, name, code):
		"""
		class Station will store data such as what line it is on. 
		Also each indiviual name and code.
		"""
		self.name = name
		self.code = code
		self.lines = []
		self.is_interchange = ''
		self.default_interchange_time = 60

		####
		# co ordinates appended as [self, y, x] then reverse [x, y, self]
		self.co_ord = [self]
		####

	def is_on_line(self, line):
		"""
		Uses station and confirms if its on the line specified.
		"""
		if line in self.lines:
			if not(line.has_station(self)): #self as a parameter
				print("Warning! Inconsistent situation: station {0} claims to be on line {1},"
				 "but that line fails to list it as one of its stations!").format(self, line.long_name)
				return True
		return line.has_station(self) #this expression is boolean rather than return true then return false

	def single_line(self, destination):
		line_current_station = self.lines
		line_destination_station = destination.lines
		list_of_times = []
		list_of_lines = []
		index_lines = []
		final_time = 0
		x = ""

		for find_common in line_current_station:
			for find_common2 in line_destination_station:
				if find_common2 == find_common:
					if find_common not in list_of_lines:
						list_of_lines.append(find_common)
						list_of_times.append(find_common.travel_times)					
						x = find_common

		# (1) To get the time from current station to destination station. First direction is needed.
		# (1)If the index of current station is greater than the index of destination station. Then train is headed towards end_point
		# Else, headed towards cpt. (2) Switch to appropriate list in travel_times (0 if headed end_point, 1 if headed cape_town.).
		# Add times in travel_times from smallest index till biggest index of index_current_station and index_destination_station. 	
	
		if x != "":

			for index in range(len(list_of_lines)):
				index_current_station = list_of_lines[index].index_station(self)
				index_destination_station = list_of_lines[index].index_station(destination)
				inter = 0

				# Check for is_interchange True. +1 for each interchange. Multiply that by default_interchange_time.
				for line in list_of_lines[index].stations[index_current_station : index_destination_station+1]:
					if line.is_interchange == True: inter += 1
				added_time_interchange = inter * self.default_interchange_time
				time = added_time_interchange	
				# (1)
				if index_current_station > index_destination_station:
					# Towards Cape town
					val = 1
					list_of_times = list_of_lines[index].travel_times[val][index_destination_station : index_current_station]

				else:
					# Towards End point
					val = 0
					list_of_times = list_of_lines[index].travel_times[val][index_current_station : index_destination_station]
				
				for times in list_of_times:
					time += times

				if final_time == 0:
					final_time = time
					i = index
				elif time < final_time:
					final_time = time
					i = index
				
		 		
			shortest_route_station = list_of_lines[i]

			stops_and_dirction = shortest_route_station.number_stops_and_direction(self, destination)
			minutes = int(final_time/60)
			sec = int(final_time%60)
			'''
			return [("From {0} to {1} on line {2}. Towards {3}. Number of stops {4}. Time taken {5}sec, ({6}min, {7}sec)".format(
				self.name, destination.name, shortest_route_station, list_of_lines[i].end_points[val].name , stops_and_dirction[0][0], final_time, minutes, sec)), final_time, val]
			'''
			return [self.name, destination.name, shortest_route_station, list_of_lines[i].end_points[val].name , stops_and_dirction[0][0], final_time, minutes, sec, final_time, val]
		else:
			return None

	def route_to(self, destination):
		x = self.single_line(destination)
		if x != None:
			print("From {0} to {1} on line {2}. Towards {3}. Number of stops {4}. Time taken {5}sec ({6}min, {7}sec)".format(
				x[0], x[1], x[2].long_name, x[3], x[4], x[5], x[6], x[7]))
			
		if x ==	 None:
			# if here no common line was found. In that case find a common station within each line:
			# Once common station and shortest route has been found. Run same code as if on one line (x != "":)
			line_current_station = self.lines
			line_destination_station = destination.lines
			common_stations = []
			common_line = []
			list_of_times = []
			dis_index = []
			time = 0
			final_time = 0

			for cur in line_current_station:            # Scans through list of lines on current possible line
				for des in line_destination_station:    # Scans through list of lines on possible destination line
					for sta_cur in cur.stations:	    # Scans through individual stations of current individual line
						if not (sta_cur.is_interchange):
							continue
						for sta_des in des.stations:	# Scans through individual stations of individual line
							if not (sta_des.is_interchange):
								continue
							if sta_cur == sta_des:		# If match is found between 2 stations.
								if sta_cur in common_stations or sta_des in common_stations:
									continue
								else:
										list_of_times.append(cur.travel_times)					
										common_line.append(cur)			# Appends the same line to common_line
										common_stations.append(sta_des)	# Appends the same station to common_stations					
			

			# Find shortest route using time from potential station to destination and add to source station
			# to potental statio. The shortest time from them will be the shortest route.
			for index in range(len(common_stations)):
				potential_station = common_stations[index]
				potential_station_time = self.single_line(potential_station)[1]
				time_potential_station_to_destination = potential_station.single_line(destination)[1]
				possible_time = potential_station_time + time_potential_station_to_destination
				if index == 0:
					shortest_time = possible_time
					shor_index = 0
				elif possible_time < shortest_time:
					shortest_time = possible_time
					shor_index = index

			switch_stations = common_stations[shor_index]	# Last station scanned will be shortest route. 
			line = common_line[shor_index]	# Same goes for line. Since appended at same time as station.

			print("FROM: {0}    TO: {1}".format(self.name, switch_stations.name))
			x1 = self.single_line(switch_stations)

			print("")

			print("From {0} to {1} on line {2}. Towards {3}. Number of stops {4}. Time taken {5}sec ({6}min, {7}sec)".format(
				x1[0], x1[1], x1[2].long_name, x1[3], x1[4], x1[5], x1[6], x1[7]))

			print("")

			print("Change trains in {}".format(switch_stations.name))
			print("")
			x2 = switch_stations.single_line(destination)
			print("FROM: {0}    TO: {1}".format(switch_stations.name, destination.name))
			print("")
			print("From {0} to {1} on line {2}. Towards {3}. Number of stops {4}. Time taken {5}sec ({6}min, {7}sec)".format(
				x2[0], x2[1], x2[2].long_name, x2[3], x2[4], x2[5], x2[6], x2[7]))
			return switch_stations.single_line(destination)[0]
			