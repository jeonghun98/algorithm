# 스택
import sys
input = sys.stdin.readline
class stack :
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.items :
            return -1
        return self.items.pop()
    def top(self):
        if not self.items :
            return -1
        return self.items[-1]
    def empty(self):
        return not self.items
    def size(self):
        return len(self.items)

n = int(input())
stk = stack()
for _ in range(n) :
    data = list(input().split())
    if data[0] == 'push' :
        stk.push(int(data[1]))
    elif data[0] == 'top' :
        print(stk.top())
    elif data[0] == "size" :
        print(stk.size())
    elif data[0] == "empty" :
        print(1 if stk.empty() else 0)
    elif data[0] == "pop" :
        print(stk.pop())