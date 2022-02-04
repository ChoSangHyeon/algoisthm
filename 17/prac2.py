class BinaryMinHeap:
    def __init__(self):
        self.items = [None]
    def __len__(self):
        return len(self.items)-1
    def up(self):
        cur = len(self)
        par = cur // 2
        while par > 0:
            if self.items[cur]< self.items[par]:
                self.items[cur],self.items[par] = self.items[par],self.items[cur]
            cur = par
            par = cur//2

    def down(self,cur):
        if cur > len(self):
            return
        left = cur * 2
        right = cur * 2 + 1
        temp = cur
        if left<=len(self) and self.items[temp] > self.items[left]:
            temp = left
        if right<=len(self) and self.items[temp] > self.items[right]:
            temp = right
        if cur != temp:
            self.items[cur], self.items[temp] = self.items[temp],self.items[cur]
            self.down(temp)


    def insert(self,dist):
        self.items.append(dist)
        self.up()

    def extract(self):

        self.items[1],self.items[-1] = self.items[-1],self.items[1]
        root = self.items.pop()
        self.down(1)
        return root

def cal_dist(point):
    return (point[0]*point[0]+point[1]*point[1])

def k_closest(points,k):
    dist = []
    con = BinaryMinHeap()
    for i in points:
        dist.append(cal_dist(i))
        con.insert(cal_dist(i))
    for _ in range(k-1):
        con.extract()
    taget = [con.extract() for _ in range(k)][-1]
    return [points[idx] for idx,dist in enumerate(dist) if dist <= taget]
