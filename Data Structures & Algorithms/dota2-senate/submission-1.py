class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        bannedR, bannedD, voteR, voteD = 0,0,0,0

        for vote in senate:
            if vote == 'R':
                voteR += 1
            else:
                voteD += 1
        while voteR > 0 and voteD > 0:
            print(senate)
            nextVote = ""
            for vote in senate:
                if vote == 'R':
                    if bannedR > 0:
                        bannedR -= 1
                    else:
                        nextVote += "R"
                        voteR += 1
                        bannedD += 1
                if vote == 'D':
                    if bannedD > 0:
                        bannedD -= 1
                    else:
                        nextVote += "D"
                        voteD += 1
                        bannedR += 1
            senate = nextVote
            voteR -= bannedR
            voteD -= bannedD

        
        
        if voteR > 0:
            return "Radiant"
        return "Dire"

        