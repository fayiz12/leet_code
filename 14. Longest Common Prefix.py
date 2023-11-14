class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        common=""

        first=strs[0]
        last=strs[-1]

        for i in range(len(first)):
            if i<len(last) and first[i]==last[i]:
                common=common+(first[i])
            else:
                break

        return common        
