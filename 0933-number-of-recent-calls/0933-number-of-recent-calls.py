class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        while self.requests[0] < t-3000:
            self.requests.popleft()
        
        return len(self.requests)
        # for i in range(len(self.requests)):
        #     if self.requests[i] >= t-3000:
        #         return len(self.requests)-i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)