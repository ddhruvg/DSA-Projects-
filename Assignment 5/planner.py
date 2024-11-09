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
        pass
    
    def least_flights_ealiest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        # curr_time = t1
        source = start_city
        target = end_city
        visited = [False] * self.m
        que = Queue()
        min_stops = float('inf') #change this
        min_time = float('inf')
        required_path = None
        que.append((0,source,FlightNode(None,None),t1)) #stops,curr_position,path[list],curr_time
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
            # difficulty with visited array if A is visited by any flight from B once then it will be marked visited 
            # difficulty with get the minimun flight arrival time         

            if position == source :
                required_flight = None
                for flight in self.adj[position]:
                    arrival_city = flight.end_city
                    if visited[arrival_city] or flight.arrival_time>t2:
                        continue
                    new_path = FlightNode(flight,path)
                    que.append((stops+1,flight.end_city,new_path,flight.arrival_time))
                    visited[flight.end_city] = True 
            else:
                for flight in self.adj[position]:
                    if visited[arrival_city] or flight.arrival_time>t2:
                        continue
                    if flight.departure_time<curr_time+20:
                        continue
                    new_path = FlightNode(flight,path)
                    que.append((stops+1,flight.end_city,new_path,flight.arrival_time))   
                    visited[flight.end_city] = True     
        ans = []
        while required_path is not None:
            ans.append(required_path.curr)
            required_path = required_path.prev

        return ans     
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        heap = Heap()
        source = start_city
        destination = end_city
        distance_array = [float('inf')]*self.m
        distance_array[source] = 0
        heap.insert((0,source,t1)) #cost,position,time
        while not heap.is_empty():
            top = heap.extract()
            cost = top[0]
            postion = top[1]
            curr_time = top[2]

            if distance_array[postion] > cost:
                continue
            for flight in self.adj[postion]:
                if curr_time + 20 < flight.departure_time:
                    continue
                if cost + flight.fare < distance_array[flight.end_city]:
                    heap.insert
        pass
    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        source = start_city
        target = end_city
        visited = [False] * self.m
        que = Queue()
        min_stops = float('inf') #change this
        min_time = float('inf')
        required_path = []
        que.append((0,source,FlightNode(None,None),t1)) #stops,curr_position,path[list],curr_time
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
                for flight in self.adj[position]:
                    arrival_city = flight.end_city
                    if visited[arrival_city]:
                        continue
                    new_path = FlightNode(flight,path)
                    que.append((stops+1,flight.end_city,new_path,flight.arrival_time))
            else:
                for flight in self.adj[position]:
                    if visited[arrival_city]:
                        continue
                    if flight.departure_time<curr_time+20:
                        continue
                    new_path = FlightNode(flight,path)
                    que.append((stops+1,flight.end_city,new_path,flight.arrival_time))        
        ans = []
        while required_path is not None:
            ans.append(required_path.curr)
            required_path = required_path.prev

        return ans 
        pass


class FlightNode:
    def __init__(self,curr,prev):
        self.curr = curr
        self.prev = prev 
