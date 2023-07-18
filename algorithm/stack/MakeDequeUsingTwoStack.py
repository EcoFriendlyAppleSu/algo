stack_01 = []
stack_02 = []

def enqueue(element):
    if not stack_01:
        stack_01.append(element)
    else:
        stack_02.append(element)

def deque():
    # stack_01 이 빈 stack이라면
    if not stack_01:
        if not stack_02:
            return None
        while stack_02:
            stack_01.append(stack_02.pop())
        return stack_02.pop()
    elif not stack_02:
        if not stack_01:
            return None
        while stack_01:
            stack_02.append(stack_01.pop())
        return stack_01.pop()

def size_of_queue():
    return len(stack_01) + len(stack_02)