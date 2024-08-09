from collections import deque

def minOperations(n: int) -> int:
    # BFS approach
    if n <= 1:
        return 0
    
    queue = deque([(1, 0, 0)])  # (current_length_of_buffer, clipboard_content, steps)
    visited = set()  # To keep track of visited states
    
    while queue:
        buffer_len, clipboard, steps = queue.popleft()
        
        if buffer_len == n:
            return steps
        
        # Option 1: Copy all (only makes sense if clipboard is not empty)
        if buffer_len > 0 and (buffer_len, buffer_len) not in visited:
            visited.add((buffer_len, buffer_len))
            queue.append((buffer_len, buffer_len, steps + 1))
        
        # Option 2: Paste (only makes sense if clipboard is not empty)
        if clipboard > 0 and buffer_len + clipboard <= n and (buffer_len + clipboard, clipboard) not in visited:
            visited.add((buffer_len + clipboard, clipboard))
            queue.append((buffer_len + clipboard, clipboard, steps + 1))
    
    return -1  # If no solution is found


