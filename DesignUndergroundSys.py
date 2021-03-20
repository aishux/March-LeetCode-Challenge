class UndergroundSystem:

    def __init__(self):
        self.emp_ids = {}
        self.duration = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.emp_ids[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        source, time = self.emp_ids.pop(id)
        self.duration[(source, stationName)].append(t - time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.duration[(startStation, endStation)]) / len(self.duration[(startStation, endStation)])
