class Node:
    def __init__(self, key, value, timeStamp):
        self.key = key
        self.value = value
        self.cnt = 1
        self.timeStamp = timeStamp

# LFU Cache class
class LFUCache:

    # Constructor to initialize values
    def __init__(self, capacity):
        self.capacity = capacity
        self.curSize = 0
        self.curTime = 0
        self.cacheList = [None] * capacity

    # Function to get the key's value
    def get(self, key):
        self.curTime += 1
        for i in range(self.capacity):
            if self.cacheList[i] is not None and self.cacheList[i].key == key:
                self.cacheList[i].cnt += 1
                self.cacheList[i].timeStamp = self.curTime
                return self.cacheList[i].value
        return -1

    # Function to put a key-value pair
    def put(self, key, value):
        self.curTime += 1

        if self.capacity == 0:
            return

        for i in range(self.capacity):
            if self.cacheList[i] is not None and self.cacheList[i].key == key:
                self.cacheList[i].value = value
                self.cacheList[i].cnt += 1
                self.cacheList[i].timeStamp = self.curTime
                return

        if self.curSize < self.capacity:
            self.curSize += 1
            for i in range(self.capacity):
                if self.cacheList[i] is None:
                    self.cacheList[i] = Node(key, value, self.curTime)
                    return
        else:
            minCnt = float('inf')
            minTime = float('inf')
            minIndex = -1
            for i in range(self.capacity):
                if self.cacheList[i].cnt < minCnt or (
                    self.cacheList[i].cnt == minCnt and self.cacheList[i].timeStamp < minTime
                ):
                    minCnt = self.cacheList[i].cnt
                    minTime = self.cacheList[i].timeStamp
                    minIndex = i
            self.cacheList[minIndex] = Node(key, value, self.curTime)

if __name__ == "__main__":
    cache = LFUCache(2)
    
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1), end=" ")
    cache.put(3, 3)
    print(cache.get(2), end=" ")
    cache.put(4, 4)
    print(cache.get(3), end=" ")
    print(cache.get(4), end=" ")
    cache.put(5, 5)