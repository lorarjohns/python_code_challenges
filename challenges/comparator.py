import heapq


class Checker:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, players):
        for player in players:
            heapq.heappush(self._queue, player.comparator())
            self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)

    def sort(self):
        heapq.heapify(self._queue)
        return heapq.nsmallest(len(self._queue), self._queue)


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self) -> str:
        return f"{self.name} {self.score}"

    def comparator(self):
        return (-self.score, self.name)


if __name__ == "__main__":
    data = [['Smith', 20], ['Jones', 15], ['Jones', 20]]
    players = [Player(*p) for p in data]
    #
    #comp = Checker()
    #comp.push(players)
    #print("\n".join(comp.sort()))
    # print(comp.sort())

    for p in sorted(players, key=Player.comparator):
        print(p)