# 447. Number of Boomerangs

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for i in points:
            a={}
            for j in points:
                c = (i[0]-j[0])**2+(i[1]-j[1])**2  ###Calculate the (distance)^2
                if c not in a:
                    a[c]=1
                else:
                    count += a[c]
                    a[c]+=1       ### to find the number of all combinations
        return count*2        ### order matters