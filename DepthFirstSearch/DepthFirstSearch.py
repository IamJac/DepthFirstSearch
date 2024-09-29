from inspect import stack
import subprocess
import time
def dfs(graph,goal,start):
    if goal not in graph:
        print(F"{goal} is not in the graph")
        return
    if start not in graph:
        print(F'{start} is not in the graph')
        return
    else:
        s=stack()
        visited=set()
        if goal==start:
            print(F"{goal} is at the starting point of the search - {start}")
            return
        else:
            s.append(start)
            visited.add(start)
            while s:
                node=s.pop()
                for i in graph[node]:
                    if i not in visited:
                        if i==goal:
                            print(F'{goal} found as a successor of {node}')
                            return
                        else:
                            s.append(i)
    

graph={'A':['B','C','F','G'],
       'B':['A','C','D','G'],
       'C':['A','B','D','E','F','G'],
       'D':['B','C','E','F'],
       'E':['C','D','F'],
       'F':['A','C','D','E','G','H'],
       'G':['A','B','C','F'],
       'H':['F','I'],
       'I':['H']}
num=None
while num!="w":
    print("Input w as the element to be searched to exit")
    print()
    print("Input element to be searched")
    num=str(input())
    if num=="w":
        print("Terminating the program")
        time.sleep(1)
        break
    else:
        print("Input starting point of the search-[A,B,C,D,E,F,G,H or I]")
        num2=str(input())
        dfs(graph,num,num2)
        time.sleep(5)
        subprocess.call('cls',shell=True)
