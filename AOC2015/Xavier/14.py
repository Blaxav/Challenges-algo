import sys


class Deer:
    def __init__(self, name, speed, time, rest):
        self._name = name
        self._speed = speed
        self._time = time
        self._rest = rest
        self._cycle_dist = self._speed * self._time
        self._score = 0

    def distance(self, duration):
        # Whole cycles
        n_cycles = duration // (self._time + self._rest)
        total_dist = n_cycles * self._cycle_dist

        # + Cycles not finished
        duration = duration % (self._time + self._rest)
        if duration < self._time:
            total_dist += duration * self._speed
        else:
            total_dist += self._cycle_dist
        return total_dist


if __name__ == '__main__':

    deers = []
    input_data = open(sys.argv[1], 'r')
    for line in input_data:
        name = line.split()[0]
        speed = int(line.split()[3])
        time = int(line.split()[6])
        rest = int(line.split()[-2])
        deers.append(Deer(name, speed, time, rest))

    duration = 2503
    id_win = []
    best_dist = 0
    for t in range(1, duration + 1):
        id_win = []
        best_dist = 0
        for i in range(len(deers)):
            if deers[i].distance(t) > best_dist:
                id_win = [i]
                best_dist = deers[i].distance(t)
            elif deers[i].distance(t) == best_dist:
                id_win.append(i)

        #print(deers[id_win]._name, "  ", best_dist, "  ", deers[id_win]._score)
        for id in id_win:
            deers[id]._score += 1

    for d in deers:
        print(d._name, "  ", d._score)
