from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        used = [False for _ in range(len(hand))]
        hand.sort()
        nextStart = 0
        curHand = []
        while not all(used):
            print(used, nextStart, curHand)
            for i in range(nextStart, len(hand)):
                card = hand[i]
                if used[i]:
                    if i == len(hand) - 1:
                        return False
                    continue
                if not curHand:
                    curHand.append(card)
                    used[i] = True
                if card == max(curHand) + 1 or card == min(curHand) - 1:
                    # print(curHand, card, i)
                    curHand.append(card)
                    used[i] = True
                nextStart = nextStart if not used[nextStart] else nextStart + 1
                if len(curHand) == groupSize:
                    curHand = []
                    break
                if i == len(hand) - 1:
                    return False
        return True


solution = Solution()
hand = [2,1,2,4,1,3,3,3]

groupSize = 2
print(solution.isNStraightHand(hand, groupSize))