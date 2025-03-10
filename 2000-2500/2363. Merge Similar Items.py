class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1 = sorted(items1, key=lambda x: x[0])
        items2 = sorted(items2, key=lambda x: x[0])
        i = 0
        j = 0
        result = []
        while i < len(items1) and j < len(items2):
            if items1[i][0] == items2[j][0]:
                result.append([items1[i][0],(items1[i][1]+items2[j][1])])
                i+=1
                j += 1
            else:
                if items1[i][0] <items2[j][0]:
                    result.append(items1[i])
                    i+=1
                elif items1[i][0] >items2[j][0]:
                    result.append(items2[j])
                    j+=1

        while i < len(items1):
            result.append(items1[i])
            i+=1

        while j < len(items2):
            result.append(items2[j])
            j+=1

        return(result)