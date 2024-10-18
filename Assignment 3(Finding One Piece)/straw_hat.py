# '''
#     This file contains the class definition for the StrawHat class.
# '''

# import crewmate
# import heap
# import treasure

# class StrawHatTreasury:
#     '''
#     Class to implement the StrawHat Crew Treasury
#     '''
    
#     def __init__(self, m):
#         '''
#         Arguments:
#             m : int : Number of Crew Mates (positive integer)
#         Returns:
#             None
#         Description:
#             Initializes the StrawHat
#         Time Complexity:
#             O(m)
#         '''
        
#         # Write your code here
#         crewmate_array = []
#         for i in range(m):
#             crewmate_array.append(crewmate.CrewMate())
#         self.crewmate_heap = heap.Heap(self.comparison_crewmate,crewmate_array)
#         # self.crewmate_heap.heapify()
#         self.current_time = 0
#         self.working_crewmate = []
#         self.completed_treasures = []
        
    
#     def add_treasure(self, treasure):
#         '''
#         Arguments:
#             treasure : Treasure : The treasure to be added to the treasury
#         Returns:
#             None
#         Description:
#             Adds the treasure to the treasury
#         Time Complexity:
#             O(log(m) + log(n)) where
#                 m : Number of Crew Mates
#                 n : Number of Treasures
#         '''
        
#         # Write your code here
#         self.current_time = treasure.arrival_time # updating the current time
#         target_crewmate = self.crewmate_heap.extract() # extracting the target cremate from heap

#         # updating working time of target_cremate

#         target_crewmate.add_treasure(treasure) # inserting the treasure in target_crewmate
#         # adding the target_crewmate in working_crewmate
#         if not target_crewmate.working:
#             self.working_crewmate.append(target_crewmate)
#             target_crewmate.working = True
#             target_crewmate.starting_time = self.current_time

#         self.crewmate_heap.insert(target_crewmate) #inserting upadted target_crewmate back in the heap
        
        
           
#         pass

    
#     def get_completion_time(self):
#         '''
#         Arguments:
#             None
#         Returns:
#             List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
#         Description:
#             Returns all the treasure after processing them
#         Time Complexity:
#             O(n(log(m) + log(n))) where
#                 m : Number of Crew Mates
#                 n : Number of Treasures
#         '''
#         ans = []
#         for crew_mate in self.working_crewmate:

#             treasure_heap = heap.Heap(self.comparison_treasure,[])
#             for _treasure_ in crew_mate.treasure:
#                 treasure_ = treasure.Treasure(_treasure_.id,_treasure_.size,_treasure_.arrival_time)
#                 treasure_.completion_time = _treasure_.completion_time
#                 treasure_.completion_time = treasure_.arrival_time
#                 if not treasure_heap.top():
#                     treasure_heap.insert(treasure_)
#                 else:
#                     top_treasure = treasure_heap.top()
#                     if treasure_.arrival_time-top_treasure.arrival_time < top_treasure.size:
#                         top_treasure.size = top_treasure.size - (treasure_.arrival_time-top_treasure.arrival_time)
#                         top_treasure.arrival_time = treasure_.arrival_time
#                         treasure_heap.insert(treasure_)
#                     else:    
#                         prev_completion_time = top_treasure.arrival_time
#                         while top_treasure and treasure_.arrival_time-prev_completion_time >= top_treasure.size:

#                             top_treasure.completion_time = prev_completion_time + top_treasure.size
#                             prev_completion_time = top_treasure.completion_time

#                             extracted_treasure = treasure_heap.extract()
#                             ans.append(extracted_treasure)
#                             top_treasure = treasure_heap.top()

#                         if top_treasure and treasure_.arrival_time-prev_completion_time < top_treasure.size:  
#                             top_treasure.size = top_treasure.size-(treasure_.arrival_time-prev_completion_time)
#                             top_treasure.arrival_time = treasure_.arrival_time

#                         treasure_heap.insert(treasure_) 

#             prev_completion_time = None             
#             while treasure_heap.heap:
#                 extracted_treasure = treasure_heap.extract()
#                 if prev_completion_time is None:
#                     prev_completion_time = extracted_treasure.arrival_time + extracted_treasure.size
#                     extracted_treasure.completion_time = extracted_treasure.arrival_time + extracted_treasure.size
#                 else:
#                     extracted_treasure.completion_time = prev_completion_time + extracted_treasure.size
#                     prev_completion_time = extracted_treasure.completion_time

#                 ans.append(extracted_treasure)

#         for completed_treasures in self.completed_treasures:
#             ans.append(completed_treasures)
#         ans.sort(key=lambda x: x.id)
#         return ans       



#     def get_load(self,crewmate):
#         if crewmate.working:
#             if crewmate.load - (self.current_time-crewmate.starting_time) <=0:
#                 return 0
#             else:
#                 return crewmate.load - (self.current_time-crewmate.starting_time)
#         else:
#             return 0
          
#     def comparison_crewmate(self,crewmate1,crewmate2):
#         return self.get_load(crewmate1) < self.get_load(crewmate2)
        
#     def comparison_treasure(self,treasure1,treasure2):
#         # wait_time = self.current_time - treasure.arrival_time
#         wait_time1 = self.current_time - treasure1.completion_time
#         wait_time2 = self.current_time - treasure2.completion_time

#         #priority = treasure.size - wait_time
#         priority1 = treasure1.size - wait_time1
#         priority2 = treasure2.size - wait_time2
  
#         if priority1 == priority2:
#             return treasure1.id < treasure2.id
#         return priority1 < priority2

#     # You can add more methods if required

'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        crewmate_array = []
        for i in range(m):
            crewmate_array.append(crewmate.CrewMate())
        self.crewmate_heap = heap.Heap(self.comparison_crewmate,crewmate_array)
        # self.crewmate_heap.heapify()
        self.current_time = 0
        self.working_crewmate = []
        self.completed_treasures = []
        
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        self.current_time = treasure.arrival_time # updating the current time
        target_crewmate = self.crewmate_heap.extract() # extracting the target cremate from heap

        # updating working time of target_cremate

        target_crewmate.add_treasure(treasure) # inserting the treasure in target_crewmate
        # adding the target_crewmate in working_crewmate
        if not target_crewmate.working:
            self.working_crewmate.append(target_crewmate)
            target_crewmate.working = True
            target_crewmate.starting_time = self.current_time

        self.crewmate_heap.insert(target_crewmate) #inserting upadted target_crewmate back in the heap
        
        
           
        pass

    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        ans = []
        for crew_mate in self.working_crewmate:

            treasure_heap = heap.Heap(self.comparison_treasure,[])
            for _treasure_ in crew_mate.treasure:
                treasure_ = treasure.Treasure(_treasure_.id,_treasure_.size,_treasure_.arrival_time)
                treasure_.completion_time = _treasure_.completion_time
                treasure_.completion_time = treasure_.arrival_time
                if not treasure_heap.top():
                    treasure_heap.insert(treasure_)
                else:
                    top_treasure = treasure_heap.top()
                    if treasure_.arrival_time-top_treasure.arrival_time < top_treasure.size:
                        top_treasure.size = top_treasure.size - (treasure_.arrival_time-top_treasure.arrival_time)
                        top_treasure.arrival_time = treasure_.arrival_time
                        treasure_heap.insert(treasure_)
                    else:    
                        prev_completion_time = top_treasure.arrival_time
                        while top_treasure and treasure_.arrival_time-prev_completion_time >= top_treasure.size:

                            top_treasure.completion_time = prev_completion_time + top_treasure.size
                            prev_completion_time = top_treasure.completion_time

                            extracted_treasure = treasure_heap.extract()
                            ans.append(extracted_treasure)
                            top_treasure = treasure_heap.top()

                        if top_treasure and treasure_.arrival_time-prev_completion_time < top_treasure.size:  
                            top_treasure.size = top_treasure.size-(treasure_.arrival_time-prev_completion_time)
                            top_treasure.arrival_time = treasure_.arrival_time

                        treasure_heap.insert(treasure_) 

            prev_completion_time = None             
            while treasure_heap.heap:
                extracted_treasure = treasure_heap.extract()
                if prev_completion_time is None:
                    prev_completion_time = extracted_treasure.arrival_time + extracted_treasure.size
                    extracted_treasure.completion_time = extracted_treasure.arrival_time + extracted_treasure.size
                else:
                    extracted_treasure.completion_time = prev_completion_time + extracted_treasure.size
                    prev_completion_time = extracted_treasure.completion_time

                ans.append(extracted_treasure)

        for completed_treasures in self.completed_treasures:
            ans.append(completed_treasures)
        ans.sort(key=lambda x: x.id)
        return ans       



    def get_load(self,crewmate):
        if crewmate.working:
            if crewmate.load - (self.current_time-crewmate.starting_time) <=0:
                return 0
            else:
                return crewmate.load - (self.current_time-crewmate.starting_time)
        else:
            return 0
          
    def comparison_crewmate(self,crewmate1,crewmate2):
        return self.get_load(crewmate1) < self.get_load(crewmate2)
        
    def comparison_treasure(self,treasure1,treasure2):
        # wait_time = self.current_time - treasure.arrival_time
        wait_time1 = self.current_time - treasure1.completion_time
        wait_time2 = self.current_time - treasure2.completion_time

        #priority = treasure.size - wait_time
        priority1 = treasure1.size - wait_time1
        priority2 = treasure2.size - wait_time2
  
        if priority1 == priority2:
            return treasure1.id < treasure2.id
        return priority1 < priority2

    # You can add more methods if required