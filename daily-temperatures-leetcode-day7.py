class Solution(object):
    def dailyTemperatures(self, temperatures):
        final=list()
        for i in range(len(temperatures)-1):
            flag=0
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    final.append(j-i)
                    flag=1
                    break
            if (flag==0):
                final.append(0)
        final.append(0)
        return final
        
