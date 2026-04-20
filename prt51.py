# remove invalid parentheses
def remove_invalid_parentheses(s):
    def is_valid(string):
        count = 0
        for c in string:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0
    
    result = []
    visited = set([s])
    queue = [s]
    found = False
    
    while queue and not found:
        level_size = len(queue)
        for i in range(level_size):
            curr = queue.pop(0)
            if is_valid(curr):
                result.append(curr)
                found = True
            
            if found:
                continue
            
            for j in range(len(curr)):
                if curr[j] in '()':
                    next_str = curr[:j] + curr[j+1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)
    
    return result

s = "()())()"
print("valid parentheses after removal:", remove_invalid_parentheses(s))
