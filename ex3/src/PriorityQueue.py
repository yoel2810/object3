from DiNode import DiNode

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def remove(self, data: int):
        return self.queue.remove(data)

    def delete(self, dist: dict) -> DiNode:
        try:
            min = 0
            for i in range(len(self.queue)):
                #print("if " + str(dist[self.queue[i].get_id()]) + " < " + str(dist[self.queue[min].get_id()]))
                if dist[self.queue[i].get_id()] < dist[self.queue[min].get_id()]:
                    min = i
            x = self.queue[min]
            del self.queue[min]
            return x
        except:
            print("ERROR! Could not delete")
            return

    #def decrease_key(self, key: int, data: DiNode):

