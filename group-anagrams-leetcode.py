class Solution(object):
    def groupAnagrams(self, strs):
        final=list()
        for i in strs:
            temp=list()
            for j in strs:
                if (sorted(i)==sorted(j)):
                    temp.append(j)
            temp.sort()
            final.append(temp)
        l=[]
        [l.append(x) for x in final if x not in l]
        return(l)
