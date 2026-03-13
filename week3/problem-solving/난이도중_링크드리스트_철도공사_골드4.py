# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
import sys
input = sys.stdin.readline

class Station:
    name = None
    prev = None
    next = None
    def __init__(self, name, prev, next):
        self.name = name
        self.prev = prev
        self.next = next
        pass

class StationLine:
    stations = []
    
    def __init__(self, priorStations):
        self.stations = [None for _ in range(1000001)]
        prevStation = None

        for station in priorStations:
            curr_station = Station(station, prevStation, None)
            self.stations[station] = curr_station
            if prevStation: prevStation.next = curr_station
            prevStation = curr_station
        self.stations[priorStations[-1]].next = self.stations[priorStations[0]]
        self.stations[priorStations[0]].prev = self.stations[priorStations[-1]]
    
    def pushNext(self, i, j):
        curr_station = self.stations[i]
        ret = curr_station.next.name
        new_station = Station(j, curr_station, curr_station.next)
        self.stations[j] = new_station
        curr_station.next.prev = new_station
        curr_station.next = new_station
        return ret
    
    def pushPrev(self, i, j):
        curr_station = self.stations[i]
        prev_station = curr_station.prev
        self.pushNext(prev_station.name, j)
        return prev_station.name
    
    def popNext(self, i):
        curr_station = self.stations[i]
        ret = curr_station.next.name
        nnext_station = curr_station.next.next
        nnext_station.prev = curr_station
        curr_station.next = nnext_station
        return ret
    
    def popPrev(self, i):
        curr_station = self.stations[i]
        ret = curr_station.prev.name
        pprev_station = curr_station.prev.prev
        pprev_station.next = curr_station
        curr_station.prev = pprev_station
        return ret
        

    def printLine(self, i):
        print("=== Print Station Line ===")
        first_station = self.stations[i]
        curr_station = first_station.next
        print(first_station.name)
        while curr_station != first_station:
            print(curr_station.name)
            curr_station = curr_station.next
        print("=== === === === === === ===")

        


N, M = map(int, input().split())
line = list(map(int, input().split()))

station = StationLine(line)
outputStk = [0 for _ in range(M)]
j = 0

for i in range(M):
    line = input().split()
    cmd = line[0]
    if cmd == 'BN':
        result = station.pushNext(int(line[1]), int(line[2]))
        # station.printLine(2)
        pass
    if cmd == 'BP':
        result = station.pushPrev(int(line[1]), int(line[2]))
        pass
    if cmd == 'CN':
        result = station.popNext(int(line[1]))
        pass
    if cmd == 'CP':
        result = station.popPrev(int(line[1]))
        pass
    outputStk[j] = result
    j += 1
ans = "\n".join(map(str, outputStk))
print(ans)
