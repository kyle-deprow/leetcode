from typing import List

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.lru_queue = [None]*capacity
    self.queued = 0
    self.cache = {}
  
  def __reorder_queue(self, key: int):
    ind = self.lru_queue.index(key)
    self.lru_queue = self.lru_queue[:ind] + self.lru_queue[ind+1:self.queued] + [self.lru_queue[ind]] + [None]*(self.capacity-self.queued)

  def __str__(self):
    print(self.cache)
    print(self.lru_queue)
    return ''

  def get(self, key: int) -> int:
    if key in self.cache:
      if key != self.lru_queue[self.queued-1]:
        self.__reorder_queue(key)
      return self.cache[key]
    else:
      return -1
  
  def put(self, key: int, val: int) -> None:
    if key in self.lru_queue:
      self.cache[key] = val
      self.__reorder_queue(key)
    elif self.queued < self.capacity:
      self.lru_queue[self.queued] = key
      self.queued += 1
      self.cache[key] = val
    else:
      del self.cache[self.lru_queue[0]]
      self.lru_queue = self.lru_queue[1:] + [key]
      self.cache[key] = val

if __name__ == '__main__':
  s = LRUCache(2)
  s.put(1,1)
  s.put(2,2)
  print(s.get(1))
  s.put(3,3)
  print(s.get(2))
  s.put(4,4)
  print(s.get(1))
  print(s.get(3))
  print(s.get(4))

  # s.put(2,1)
  # s.put(2,2)
  # print(s.get(2))
  # s.put(1,1)
  # s.put(4,1)
  # print(s.get(2))

  # s.put(2,1)
  # s.put(1,1)
  # s.put(2,3)
  # s.put(4,1)
  print(s.get(1))
  print(s.get(2))
  print(s)