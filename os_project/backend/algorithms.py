import numpy as np
def fcfs(requests, head):
    """ First Come First Serve (FCFS) Scheduling """
    seek_sequence = [head] + requests
    seek_time = 0
    for i in range(1,len(seek_sequence)):
        t=abs(seek_sequence[i]-seek_sequence[i-1])
        seek_time+=t
    return {"sequence": seek_sequence, "seek_time": seek_time}

def sstf(requests, head):
    """ Shortest Seek Time First (SSTF) Scheduling """
    requests = requests.copy()
    seek_sequence = [head]
    seek_time = 0
    while(len(requests)>=1):
        min=abs(head-requests[0])
        j=0
        for i in range(1,len(requests)):
            t=abs(head-requests[i])
            if(min>t):
                min=t
                j=i
        seek_sequence.append(requests[j])
        head=requests[j]
        seek_time+=min
        requests.pop(j)    
    return {"sequence": seek_sequence, "seek_time": seek_time}

def scan(requests, head, direction="right", disk_size=200):
    """ SCAN (Elevator) Scheduling """
    left, right = [], []
    for req in requests:
        if req < head:
            left.append(req)
        else:
            right.append(req)

    left.sort()
    right.sort()
    
    if direction == "left":
        seek_sequence = left[::-1] + right
    else:
        seek_sequence = right + left[::-1]
    
    seek_sequence.insert(0, head)
    seek_time = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))

    return {"sequence": seek_sequence, "seek_time": seek_time}
