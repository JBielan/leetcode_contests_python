class Solution:
    def assignBikes(self, workers, bikes) -> int:
        def permutations(iterable, r=None):     # function for permutations
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n - r, -1))
            yield tuple(pool[i] for i in indices[:r])
            while n:
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i + 1:] + indices[i:i + 1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                else:
                    return

        workers_dic = {}        # workers and their distances to bikes will be stored here
        for i, worker in enumerate(workers):
            workers_dic[i] = []     # create an empty table for every worker
            for bike in bikes:      # for every bike
                workers_dic[i].append(abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]))      # add distance to every
                                                                                                # bike

        options = []        # all options will be stored here
        for x in permutations(range(len(workers_dic[0])), len(workers_dic)):        # every bike to every worker
            options.append(x)

        best = 999999999        # just big enough number according to specification

        for option in options:      # for every option
            current = 0
            for i in range(len(option)):
                current += workers_dic[i][option[i]]        # sum distances for the option

            if current < best:      # if current option is better than best, just overwrite best as current
                best = current

        return best     # return best