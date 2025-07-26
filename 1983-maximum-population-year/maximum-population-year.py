class Solution(object):
    def maximumPopulation(self, logs):
        frq=[0] * (2050-1950)

        for i in logs:  
            for j in range((i[0]-1950),((i[0]-1950)+(i[1])-i[0])):
                 frq[j]+=1


        return (frq.index(max(frq)))+1950

        