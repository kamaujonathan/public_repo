class BinarySearch:
    def __init__(self,a,b):
        self.list = []
        self.a = len(list) - 1
        self.h = 0
        def search(value):
            while self.h<=self.a:
                mid = (self.h + self.a)//2
                if self.list[mid] == b:
                    return mid
                else:
                    if b < self.list[mid]:
                        self.a = mid
                    else:
                            self.h = mid
                            return mid
   

