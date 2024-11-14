from flight import Flight
from helper import Heap,Queue

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        self.m = len(flights)
        self.adj = [[] for i in range(self.m)]
        for flight in flights:
            idx = flight.start_city
            
            self.adj[idx].append(flight)
    
        self.flight_adj_pri = [None] * self.m
        for flight in flights:
            idx = flight.flight_no
            self.flight_adj_pri[idx] = flight

        self.flight_adj = [[] for i in range(self.m)]
        for i in range(self.m):
            flight = self.flight_adj_pri[i]
            for next_flight in self.adj[flight.end_city]:
                if next_flight.departure_time >= flight.arrival_time + 20:
                    self.flight_adj[i].append(next_flight)

        # self.flight_adj = [[] for i in range(self.m)]
        # for city in self.adj:
        #     for flight in city:
        #         end_city = flight.end_city
        #         for next_flight in self.adj[end_city]:
        #             if next_flight.departure_time >= flight.arrival_time + 20:
        #                 self.flight_adj[flight.flight_no].append(next_flight)


               
        pass
    
    def least_flights_ealiest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        if start_city == end_city:
            return []

        source = start_city
        target = end_city
        que = Queue()
        min_stops = float('inf')
        min_time = float('inf')
        required_path = None

        # Array to track best (stops, time) for each city, indexed by city ID
        # Assuming self.m is the number of cities
        best_time = [(float('inf'), float('inf'))] * self.m

        # Initialize queue with starting position
        que.append((0, source, FlightNode(None, None), t1))  # stops, curr_position, path, curr_time

        while not que.is_empty():
            stops, position, path, curr_time = que.pop()

            # If this path exceeds the minimum stops found, skip further exploration
            if stops > min_stops:
                continue

            # Check if we have reached the target city
            if position == target:
                # Primary: fewer stops; Secondary: earlier arrival time
                if stops < min_stops or (stops == min_stops and curr_time < min_time):
                    required_path = path
                    min_time = curr_time
                    min_stops = stops
                continue

            # If this path does not improve on best_time for the current position, skip it
            best_stops, best_arrival_time = best_time[position]
            if stops > best_stops or (stops == best_stops and curr_time >= best_arrival_time):
                continue

            # Update best_time with the better path
            best_time[position] = (stops, curr_time)

            outgoing_cities = []
            flights_used = [None] * self.m
            for flight in self.adj[position]:
                arrival_city = flight.end_city

                # Apply timing constraints based on the current city
                if position == source:
                    if flight.arrival_time > t2 or flight.departure_time < curr_time:
                        continue
                else:
                    if flight.arrival_time > t2 or flight.departure_time < curr_time + 20:
                        continue

                # Choose the best (earliest arrival) flight for each outgoing city
                if flights_used[arrival_city] is None or flights_used[arrival_city].arrival_time > flight.arrival_time:
                    flights_used[arrival_city] = flight
                    outgoing_cities.append(flight.end_city)

            # Enqueue the best outgoing flights
            for outgoing_city in outgoing_cities:
                required_flight = flights_used[outgoing_city]
                new_path = FlightNode(required_flight, path)
                que.append((stops + 1, required_flight.end_city, new_path, required_flight.arrival_time))

        # If no path was found, return an empty list
        if required_path is None:
            return []

        # Reconstruct path from end to start
        ans = []
        while required_path.curr is not None:
            ans.append(required_path.curr)
            required_path = required_path.prev

        return ans[::-1]





        if start_city == end_city:
            return []
        source = start_city
        target = end_city
        visited = [float('inf')] * self.m
        que = Queue()
        min_stops = float('inf') #change this
        min_time = float('inf')
        required_path = None
        que.append((0,source,FlightNode(None,None),t1)) #stops,curr_position,path[list],curr_time
        visited[source] = 0
        while not que.is_empty():
            curr = que.pop()
            stops = curr[0]
            position = curr[1]
            path = curr[2]
            curr_time = curr[3]
            if stops > min_stops:
                continue
            if position == target:
                if stops < min_stops:
                    required_path = path
                    min_time = curr_time
                    min_stops = stops
                if stops == min_stops:
                    

                    if curr_time < min_time:
                        required_path = path
                        min_time = curr_time
                continue  
            if position == source :
                outgoing_cities = []
                flights_used = [None] * self.m
                for flight in self.adj[position]:
                    arrival_city = flight.end_city

                    if stops+1>visited[arrival_city] or  flight.arrival_time>t2 or flight.departure_time < curr_time:
                        continue

                    if flights_used[arrival_city] is None:
                        outgoing_cities.append(flight.end_city)
                        flights_used[arrival_city] = flight
                    else:
                        if flights_used[arrival_city].arrival_time > flight.arrival_time:
                              flights_used[arrival_city] = flight

                for outgoing_city in outgoing_cities:
                    required_flight = flights_used[outgoing_city]              
                    new_path = FlightNode(required_flight,path)
                    visited[required_flight.end_city] = stops+1
                    que.append((stops+1,required_flight.end_city,new_path,required_flight.arrival_time))
                    # visited[required_flight.end_city] = True 
            else:
                outgoing_cities = []
                flights_used = [None] * self.m
                for flight in self.adj[position]:
                    arrival_city = flight.end_city

                    if stops+1<visited[arrival_city] or flight.arrival_time>t2 or flight.departure_time < curr_time + 20:
                        continue

                    if flights_used[arrival_city] is None:
                        outgoing_cities.append(flight.end_city)
                        flights_used[arrival_city] = flight
                    else:
                        if flights_used[arrival_city].arrival_time > flight.arrival_time:
                              flights_used[arrival_city] = flight

                for outgoing_city in outgoing_cities:
                    required_flight = flights_used[outgoing_city]              
                    new_path = FlightNode(required_flight,path)
                    visited[required_flight.end_city] = stops+1
                    que.append((stops+1,required_flight.end_city,new_path,required_flight.arrival_time))
                    # visited[required_flight.end_city] = True  
        ans = []
        if required_path is None:
            return []
        while required_path.curr is not None:
            ans.append(required_path.curr)
            required_path = required_path.prev

        return ans[::-1]  
                       
            
        # source = start_city
        # end = end_city
        # if source == end:
        #     return []
        # overall_best_stop = float('inf')
        # overall_best_path = None
        # overall_best_time = float('inf')
        # for start_flight in self.adj[source]:
        #     best_stop = float('inf')
        #     best_path = None
        #     best_time = float('inf')
        #     que =   Queue()
        #     visited = [False] * self.m
        #     que.append((0,start_flight,FlightNode(start_flight,None)))
        #     while not que.is_empty():
        #         curr = que.pop()
        #         stop = curr[0]
        #         curr_flight = curr[1]
        #         path = curr[2]
        #         if stop > overall_best_stop:
        #             continue
        #         if curr_flight.arrival_time > t2:
        #             continue
        #         if curr_flight.end_city == end_city:
        #             if stop < best_stop:
        #                 best_stop = stop
        #                 best_path = path
        #                 best_time = curr_flight.arrival_time
        #             if stop == best_stop and curr_flight.arrival_time < best_time:
        #                 best_path = path
        #                 best_time = curr_flight.arrival_time    
        #         for next_flight in self.flight_adj[curr_flight.flight_no]:
        #             if next_flight.arrival_time > t2:
        #                 continue
        #             if not visited[next_flight.flight_no]:
        #                 new_path = FlightNode(next_flight,path)
        #                 que.append((stop+1,next_flight,new_path))
        #                 visited[next_flight.flight_no] = True
        #     if best_stop != float('inf'):
        #         if best_stop < overall_best_stop:
        #             overall_best_stop = best_stop
        #             overall_best_path = best_path
        #             overall_best_time = best_time
        #         if best_stop == overall_best_stop and best_time < overall_best_time:
        #             overall_best_path = best_path
        #             overall_best_time = best_time
        # ans = []
        # while overall_best_path is not None:
        #     ans.append(overall_best_path.curr)
        #     overall_best_path = overall_best_path.prev  
        # return ans[::-1]                


    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        if start_city == end_city:
            return []
        
        source = start_city
        destination = end_city
      
        overall_best_cost = float('inf')
        overall_best_path = None
        for start_flight in self.adj[source]:
            if start_flight.departure_time<t1:
                continue
            if  start_flight.arrival_time > t2:
                continue
            best_cost = float('inf')
            best_path = None
            cost_array = [float('inf')] * self.m
            cost_array[start_flight.flight_no] = start_flight.fare
            heap = Heap([],comp1)
            heap.insert((start_flight.fare,start_flight,FlightNode(start_flight,None)))
            while not heap.is_empty():
                top = heap.extract()
                cost = top[0]
                path = top[2]
                curr_flight = top[1]
                if curr_flight.arrival_time > t2:
                    continue
                if cost > best_cost:
                    continue
                if curr_flight.end_city == destination:
                    if best_cost is None or cost < best_cost:
                        best_cost = cost
                        best_path = path
                    continue
                for next_flight in self.flight_adj[curr_flight.flight_no]:
                    if next_flight.arrival_time > t2:
                        continue
                    if cost + next_flight.fare <= cost_array[next_flight.flight_no]:
                        new_path = FlightNode(next_flight,path)
                        cost_array[next_flight.flight_no] = cost + next_flight.fare
                        heap.insert((cost+next_flight.fare,next_flight,new_path))
            if best_cost!=float('inf'):
                if best_cost < overall_best_cost:
                    overall_best_cost = best_cost
                    overall_best_path = best_path    

        ans = []
        while overall_best_path is not None:
            ans.append(overall_best_path.curr)
            overall_best_path = overall_best_path.prev

        return ans[::-1]                    


    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        source = start_city
        destination = end_city

        if start_city == end_city:
            return []

        overall_best_stop = float('inf')
        overall_best_path = None
        overall_best_cost = float('inf')

        for start_flight in self.adj[source]:
            if start_flight.departure_time<t1:
                continue
            if  start_flight.arrival_time > t2:
                continue
            best_stop = float('inf')
            best_path = None
            best_cost = float('inf')
            cost_array = [float('inf')] * self.m
            cost_array[start_flight.flight_no] = start_flight.fare
            heap = Heap([],comp2)
            heap.insert((0,start_flight.fare,start_flight,FlightNode(start_flight,None)))
            while not heap.is_empty():
                top = heap.extract()
                stops = top[0]
                cost = top[1]
                path = top[3]
                curr_flight = top[2]
                if curr_flight.arrival_time > t2:
                    continue
                if cost > best_cost:
                    continue
                if curr_flight.end_city == destination:
                    if best_stop is None or stops < best_stop:
                        best_stop = stops
                        best_path = path
                        best_cost = cost
                    if best_stop == stops and cost < best_cost :
                        best_path = path  
                        best_path = cost  
                    continue

                for next_flight in self.flight_adj[curr_flight.flight_no]:
                    if next_flight.arrival_time > t2:
                        continue
                    if cost + next_flight.fare <= cost_array[next_flight.flight_no]:
                        new_path = FlightNode(next_flight,path)
                        cost_array[next_flight.flight_no] = cost + next_flight.fare
                        heap.insert((stops+1,cost+next_flight.fare,next_flight,new_path))
            if best_stop!=float('inf'):
                if best_stop < overall_best_stop:
                    overall_best_stop = best_stop
                    overall_best_path = best_path 
                    overall_best_cost = best_cost
                if best_stop == overall_best_stop and best_cost < overall_best_cost:
                    overall_best_path = best_path 
                    overall_best_cost = best_cost      

        ans = []
        while overall_best_path is not None:
            ans.append(overall_best_path.curr)
            overall_best_path = overall_best_path.prev

        return ans[::-1] 


class FlightNode:
    def __init__(self,curr,prev):
        self.curr = curr
        self.prev = prev 
def comp1(a,b):
    return a[0]<b[0]
def comp2(a,b):
    return (a[0],a[1])<(b[0],b[1])