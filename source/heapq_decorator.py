import heapq


class HeapqDecorator:
    def __init__(self):
        self.__queue = []
        heapq.heapify(self.__queue)

    def push(self, priority, item):
        heapq.heappush(self.__queue, (priority, item))

    def pop(self):
        return heapq.heappop(self.__queue)

    def contains(self, item):
        # I can't shadow tuple type, so I add i as prefix
        for ituple in self.__queue:
            if ituple[1] == item:
                return True

        return False

    def __getitem__(self, priority):
        result = []
        for ituple in self.__queue:
            if ituple[0] == priority:
                result.append(ituple[1])

        return result

    def priority(self, item) -> int:
        for ituple in self.__queue:
            if hash(ituple[1]) == hash(item):
                return ituple[0]

        raise ObjectNotFoundException

    def update(self, priority, item) -> None:
        for i in range(len(self.__queue)):
            if hash(self.__queue[i][1]) == hash(item):
                self.__queue[i] = (priority, item)
        heapq.heapify(self.__queue)

    def __len__(self) -> int:
        return len(self.__queue)


class ObjectNotFoundException(Exception):
    pass
