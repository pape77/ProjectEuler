dictPaths = {}

def countPaths(m,n):
    if m == 0 or n == 0:
        return 1
    if (m,n) in dictPaths.keys():
        return dictPaths.get((m,n))
    #Contar volviendo por la derecha + volviendo por abajo
    dictPaths[m,n] = (countPaths(m,n-1) + countPaths(m-1,n))
    return dictPaths.get((m,n))

print(countPaths(20,20))


"""
VERSION LENTA:

gridSize = [20,20]
 
def recPath(gridSize):
    
    #Recursive solution to grid problem. Input is a list of x,y moves remaining.
    
    # base case, no moves left
    if gridSize == [0,0]: return 1
    # recursive calls
    paths = 0
    # move left when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1,gridSize[1]])
    # move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0],gridSize[1]-1])
 
    return paths
 

result = recPath(gridSize)
"""

