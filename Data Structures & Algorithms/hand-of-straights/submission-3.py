class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        if len(hand) % groupSize != 0:
            print("failed due to wrong sizing")
            return False

        if groupSize == 1 :
            return True
        hand.sort()
        heap = []

        for card in hand:
            # print(card)
            # print(heap)

            if not heap:
                heapq.heappush(heap, (card, card + groupSize - 1))
            else:
                cur, end = heap[0]
                if cur == card:
                    heapq.heappush(heap, (card, card + groupSize - 1))
                    continue

                if cur + 1 == card:
                    heapq.heappop(heap)
                    if end != card:
                        heapq.heappush(heap, (cur + 1, end))
                    continue
                
                # print("didnt find group")
                return False
                
        
        if heap:
            # print("still items in group")
            return False
        else:
            return True
                    






                





        