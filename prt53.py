# restore ip addresses
def restore_ip_addresses(s):
    result = []
    
    def backtrack(start, path):
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return
        
        if len(path) >= 4:
            return
        
        for end in range(start + 1, min(start + 4, len(s) + 1)):
            segment = s[start:end]
            
            # check validity
            if len(segment) > 1 and segment[0] == '0':
                continue
            if int(segment) > 255:
                continue
            
            backtrack(end, path + [segment])
    
    backtrack(0, [])
    return result

s = "25525511135"
print("valid IP addresses:", restore_ip_addresses(s))


# wildcard matching
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    
    # handle pattern starting with *
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[j-1] == '?' or s[i-1] == p[j-1]:
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]

s = "aa"
p = "a*"
print(f"'{s}' matches '{p}'?", is_match(s, p))
