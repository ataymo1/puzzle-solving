class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        dead = set(deadends)
        visited = set()

        res = -1
        turns = 0
        queue = deque()
        queue.append(["0000"])

        if "0000" in deadends:
            return -1

        while queue:

            cur_level = queue.popleft()
            next_level = []

            for combination in cur_level:
                
                if combination == target:
                    return turns
                
                cur_num = int(combination)
                for i in range(4):
                    p_one = combination[:i] + str((int(combination[i]) + 1) % 10) + combination[i+1:]
                    m_one = combination[:i] + str((int(combination[i]) - 1) % 10) + combination[i+1:]

                    if p_one not in visited and p_one not in dead:
                        next_level.append(p_one)
                        visited.add(p_one)
                    if m_one not in visited and m_one not in dead:
                        next_level.append(m_one)
                        visited.add(m_one)
            if next_level:
                queue.append(next_level)
                turns += 1

        return -1




        
        