import sys
from random import shuffle
from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet

Vertex= Tuple[int,int]
Edge=Tuple[Vertex,Vertex]

vertices:List[Vertex]=[]


def read_data(f):
    rows=int(f.readline())
    cols=int(f.readline())
    return rows, cols

def process(rows:int, cols:int) -> UndirectedGraph:
    vertices: List[Vertex] = []

    for i in range(rows):
        for j in range(cols):
            vertices.append(i,j)

    mfs=MergeFindSet()

    for v in vertices:
        mfs.add(v)

    edges:List[Vertex]=[]
    shuffle(edges)

    for i,j in vertices:
        if j+1<cols:
            edges.append(i,j+1)
        if i+1<rows:
            edges.append(i+1,j)

    shuffle(edges)
    corridors:List[Vertex]=[]

    for u,v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u,v)
            corridors.append(u,v)

    return UndirectedGraph(E=corridors)

def show_results(labyrinth: UndirectedGraph):
    print(labyrinth)


if __name__ == "__main__":
    rows,cols=read_data(sys.stdin)
    labyrinth=process(rows,cols)
    show_results(labyrinth)