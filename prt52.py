# palindrome partitioning
def partition_palindrome(s):
    result = []
    
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    
    backtrack(0, [])
    return result

print("palindrome partitions of 'aab':", partition_palindrome("aab"))

# word break II
def word_break_ii(s, word_dict):
    word_set = set(word_dict)
    memo = {}
    
    def dfs(start):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                suffixes = dfs(end)
                for suffix in suffixes:
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)
        
        memo[start] = result
        return result
    
    return dfs(0)

s = "catsanddog"
word_dict = ["cat","cats","and","sand","dog"]
print("word break sentences:", word_break_ii(s, word_dict))
