from Queue import Queue
queue = Queue()
n = int(input())
for x in range(n):
    line = str(raw_input())
    parts = line.split(" ")
    if int(parts[0]) == 1:
        queue.put(int(parts[1]))
    elif int(parts[0]) == 2:
        queue.pop()
    elif int(parts[0]) == 3:
        print queue.peek()