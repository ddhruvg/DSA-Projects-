# '''
#     Python file to implement the class CrewMate
# '''

# class CrewMate:
#     '''
#     Class to implement a crewmate
#     '''
    
#     def __init__(self):
#         '''
#         Arguments:
#             None
#         Returns:
#             None
#         Description:
#             Initializes the crewmate
#         '''
#         # Write your code here
#         self.load = 0
#         self.treasure = []
#         self.working = False
#         self.starting_time = 0
#         pass
#     def add_treasure(self,treasure):
#         if self.starting_time == 0:
#             self.load += treasure.size
#             self.starting_time = treasure.arrival_time

#         elif self.load - (treasure.arrival_time-self.starting_time ) <= 0:
#             self.load = treasure.size
#             self.starting_time = treasure.arrival_time

#         else:
#             self.load += treasure.size

#         self.treasure.append(treasure)

        

# # Add more methods if required



'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        # Write your code here
        self.load = 0
        self.treasure = []
        self.working = False
        self.starting_time = 0
        pass
    def add_treasure(self,treasure):
        if self.starting_time == 0:
            self.load += treasure.size
            self.starting_time = treasure.arrival_time

        elif self.load - (treasure.arrival_time-self.starting_time ) <= 0:
            self.load = treasure.size
            self.starting_time = treasure.arrival_time

        else:
            self.load += treasure.size

        self.treasure.append(treasure)

        

# Add more methods if required