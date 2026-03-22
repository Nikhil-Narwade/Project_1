# backspace string compare
def backspace_compare(s, t):
    def process_string(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return ''.join(stack)
    
    return process_string(s) == process_string(t)

print("'ab#c' vs 'ad#c' equal?", backspace_compare("ab#c", "ad#c"))
print("'a##c' vs '#a#c' equal?", backspace_compare("a##c", "#a#c"))

# min stack (design stack that gets min in O(1))
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None
    
    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print("min after pushes:", min_stack.get_min())
min_stack.pop()
print("top after pop:", min_stack.top())
print("min after pop:", min_stack.get_min())


# validate stack sequences
def validate_stack_sequences(pushed, popped):
    stack = []
    i = 0
    
    for val in pushed:
        stack.append(val)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    
    return len(stack) == 0

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print("valid sequence?", validate_stack_sequences(pushed, popped))


# exclusive time of functions (call stack)
def exclusive_time(n, logs):
    result = [0] * n
    stack = []
    prev_time = 0
    
    for log in logs:
        func_id, typ, timestamp = log.split(':')
        func_id = int(func_id)
        timestamp = int(timestamp)
        
        if typ == 'start':
            if stack:
                result[stack[-1]] += timestamp - prev_time
            stack.append(func_id)
            prev_time = timestamp
        else:
            result[stack.pop()] += timestamp - prev_time + 1
            prev_time = timestamp + 1
    
    return result

logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
print("exclusive times:", exclusive_time(2, logs))
