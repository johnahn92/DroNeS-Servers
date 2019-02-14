class Job:
    def __init__(self, uid, item_type, creation_time, cost_function, pick_up, destination):
        #TODO
        self.uid = uid
        self.item_type = item_type
        self.creation_time = creation_time
        self.cost_function = cost.function
        self.pick_up = pick_up
        self.destination = destination
        self.reward = self.cost_function(0)
    def updateReward(elapsed_time):
        #TODO
        self.reward = self.cost_function(self.creation_time + elapsed_time)
        
