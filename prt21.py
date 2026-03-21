# next greater element 
def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    

    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            idx = stack.pop()
            result[idx] = nums[i % n]
        if i < n:
            stack.append(i)
    
    return result
print("next greater for [1,2,1]:", next_greater_elements([1,2,1]))


# daily temperatures 
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []
    
    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result

print("days to warmer [73,74,75,71,69,72,76,73]:", 
      daily_temperatures([73,74,75,71,69,72,76,73]))


# asteroid collision 
def asteroid_collision(asteroids):
    stack = []
    
    for ast in asteroids:
        while stack and ast < 0 < stack[-1]:
            if stack[-1] < -ast:
                stack.pop()
                continue
            elif stack[-1] == -ast:
                stack.pop()
            break
        else:
            stack.append(ast)
    
    return stack

print("asteroid collision [5,10,-5]:", asteroid_collision([5,10,-5]))
print("asteroid collision [10,2,-5]:", asteroid_collision([10,2,-5]))


# simplify path 
def simplify_path(path):
    stack = []
    parts = path.split('/')
    
    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    
    return '/' + '/'.join(stack)

print("simplify '/home//foo/':", simplify_path("/home//foo/"))
print("simplify '/../':", simplify_path("/../"))


# decode string (like 3[a]2[bc] -> aaabcbc)
def decode_string(s):
    stack = []
    current_num = 0
    current_str = ''
    
    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
        elif c == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif c == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += c
    
    return current_str

print("decode '3[a]2[bc]':", decode_string("3[a]2[bc]"))
print("decode '2[abc]3[cd]ef':", decode_string("2[abc]3[cd]ef"))
