class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_check = dict()

        for x in nums:
            if x not in frequent_check:
                frequent_check[x] = 1
            else:
                frequent_check[x] += 1

        answer = []
        
        for i in range(k):
            highest_element = max(frequent_check, key=frequent_check.get)
            answer.append(highest_element)
            del frequent_check[highest_element]
        return answer

        
         