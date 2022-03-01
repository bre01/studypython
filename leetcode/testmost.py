def longestCommonPrefix( strs) -> str:
        smallest=0
        for i in range(len(strs)):
            
            if len(strs[smallest])>len(strs[i]):
                smallest=i 
        length=len(strs[smallest])
        m=None
        if length==0:
            return ''
        else:
            for j in range(length):
                str=strs[0][:j+1]
                for i in strs:
                    if i[:j+1] !=str:
                        
                        return str[:j]
            return str
print(longestCommonPrefix(['a']))