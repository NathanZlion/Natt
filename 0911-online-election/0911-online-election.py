class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # first process persons to hold the winner at that time
        count = defaultdict(int)
        leader = persons[0]

        for index, person in enumerate(persons):
            count[person] += 1
            
            if count[leader] <= count[person]:
                leader = person
            
            persons[index] = leader            
            
        self.persons = persons
        self.times = times

        print(self.persons)

    def q(self, t: int) -> int:
        # find the time t in self.times and it's index
        # use binary search
        # then find the corresponding winner at that index
        
        low = -1
        high = len(self.times)
        
        while high > low+1:
            mid = low + (high-low)//2
            if self.times[mid] > t:
                high = mid
            else:
                low = mid
        
        return self.persons[low]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)