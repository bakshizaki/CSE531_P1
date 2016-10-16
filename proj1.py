'''
Created on 14-Oct-2016

@author: zaki
'''

import numpy
import math
from math import floor
from collections import defaultdict

class Heap():
    
    heap_array=[]
    position={}
    def __init__(self,init_array=[]):
        
        for i in range(len(init_array)):
            self.insert(init_array[i][0],init_array[i][1])
    
    def insert(self,v,key_value):
        self.heap_array.append((v,key_value))
        self.position[v]=len(self.heap_array)-1
        self.heapify_up(len(self.heap_array)-1)
        
        
    def heapify_up(self,i):
        
        while(i>0):
            j = int(floor(i/2))
            if self.heap_array[i][1] < self.heap_array[j][1]:
                temp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[j]
                self.heap_array[j] = temp
                self.position[self.heap_array[i][0]]=i
                self.position[self.heap_array[j][0]]=j
                i=j
            else:
                break
    
    def print_heap(self):
        print self.heap_array
    
    def extract_min(self):
        ret=self.heap_array[0]
        self.heap_array[0]=self.heap_array[-1]
        self.position[self.heap_array[0][0]]=0
        del self.heap_array[-1]
        if len(self.heap_array) >= 1:
            self.heapify_down(0)
        return ret
    
    def heapify_down(self,i):
        s = len(self.heap_array)-1
        while self.first_child(i)<=s:
            if self.first_child(i) == s or self.heap_array[self.first_child(i)][1] < self.heap_array[self.second_child(i)][1]:
                j = self.first_child(i)
            else:
                j = self.second_child(i)
            
            if self.heap_array[j][1]<self.heap_array[i][1]:
                temp = self.heap_array[i]
                self.heap_array[i]=self.heap_array[j]
                self.heap_array[j]=temp
                self.position[self.heap_array[i][0]]=i
                self.position[self.heap_array[j][0]]=j
                i=j
            else:
                break
    
    def decrease_key(self,v,key_value):
        self.heap_array[self.position[v]]=(v,key_value)
        self.heapify_up(self.position[v])
    
    @staticmethod
    def first_child(i):
        return 2*(i+1)-1
    
    @staticmethod
    def second_child(i):
        return 2*(i+1)
        
    def is_empty(self):
        if not self.heap_array:
            return True
        else:
            return False
         
            

def read_file(graph,filename):
    input_file = open(filename)
    line_read=input_file.readline().rstrip('\n')
    [nodes, edges]=line_read.split(' ')
    nodes = int(nodes)
    edges = int(edges)
    
    
    for line in input_file:
        line=line.rstrip('\n')
        str_list=line.split(' ')
        src_node=int(str_list[0])
        dest_node=int(str_list[1])
        weight=int(str_list[2])
        graph[src_node].append((dest_node,weight))
        graph[dest_node].append((src_node,weight))
    return graph,nodes

    
    
if __name__ == "__main__":
#     new_heap = Heap([(1,7),(2,5),(3,4),(4,1),(7,3)])
#     new_heap.decrease_key(1, 2)
#     while(new_heap.is_empty()==False):
#         print new_heap.extract_min()
#     print new_heap.position
    
    
    graph=defaultdict(list)
    graph,total_nodes=read_file(graph, "test5")
    
#     print graph
    
    #######
    d={}
    pi={}
    d[1]=0
    S=[]
    is_added={}
    mst=[]
    mst_weight=0
    for i in range(2,total_nodes+1):
        d[i]=float("inf")
    heap=Heap()
    for i in range(1,total_nodes+1):
        heap.insert(i, d[i])
        is_added[i]=0

    for i in range(1,len(graph)+1):
        (node,dv)=heap.extract_min()
        mst_weight=mst_weight+dv
        S.append(node)
        is_added[node]=1
        if i!=1:
            mst.append((pi[node],node))
        for j in graph[node]:
            if is_added[j[0]]==0:
                if j[1] < d[j[0]]:
                    d[j[0]] = j[1]
                    heap.decrease_key(j[0],d[j[0]])
                    pi[j[0]]=node
    
    
    print mst    
    print mst_weight
    
        
        
        
        
        
        
        