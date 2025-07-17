class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        cur = min(len(players), len(trainers))
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        maxTrainerIdx = 0
        maxPlayerIdx = 0
        while maxPlayerIdx != len(players) and maxTrainerIdx != len(trainers):
            if trainers[maxTrainerIdx] < players[maxPlayerIdx]:
                if len(trainers) < len(players): # there can be other players there too
                    maxPlayerIdx += 1
                else:
                    maxPlayerIdx += 1
                    cur -= 1
            else:
                maxPlayerIdx += 1
                maxTrainerIdx += 1
        return cur

solution = Solution()
print(solution.matchPlayersAndTrainers([2,3,1,1,3], [2,4,2]))

