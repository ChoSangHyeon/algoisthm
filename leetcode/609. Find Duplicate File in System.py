import collections

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        listTemp = []
        dictTemp = collections.defaultdict(list)
        for i in paths:
            L = i.split(' ')
            for j in range(len(L)-1):                
                listTemp= listTemp + [str(L[0]+'/'+L[j+1])]
        for st in listTemp:
            name,indexTemp = st.split('(')
            index = indexTemp[:-1]
            dictTemp[index] = dictTemp[index] + [name]
        res = []
        for ans in dictTemp.values():
            if (len(ans) >=2):
                res.append(list(ans))
                
        return res