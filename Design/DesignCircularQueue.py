# https://leetcode.com/problems/design-circular-queue/description/

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0]*k
        self.start =0
        self.length = 0
        self.index =0
        

    def enQueue(self, value: int) -> bool:
        #print(value)
        if self.index == self.k:
            return False
        self.queue[(self.start + self.index) % self.k] = value
        #print("inside if qnqueue", self.queue)
        self.index +=1

        return True 
   
    def deQueue(self) -> bool:
        if self.index ==0:
            return False
            
        self.index -=1 
        self.start = (self.start + 1) % self.k 
        return True
        

    def Front(self) -> int:
        if self.index ==0:
            return -1

        return self.queue[self.start]

    def Rear(self) -> int:
        if self.index ==0:
            return -1

        return self.queue[(self.start + self.index - 1) % self.k]

    def isEmpty(self) -> bool:
        if self.index == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        # print(self.length)
        # print(self.k)
        if self.index == self.k:
            return True
        else:
            return False 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
