from maze import *
from exception import *
from stack import *

class PacMan:
    navigator_maze = []
    def __init__(self, grid : Maze) -> None:
        self.navigator_maze = grid.grid_representation
    def find_path(self, start : tuple[int, int], end : tuple[int, int]) -> list[tuple[int, int]]:
        # IMPLEMENT FUNCTION HERE
        stack = Stack()
        m = len(self.navigator_maze)
        n = len(self.navigator_maze[0])        
        if self.navigator_maze[start[0]][start[1]] or self.navigator_maze[end[0]][end[1]]:
            raise PathNotFoundException         
        def update(x,y,s):
            if s=='l':
                return (x,y-1)
            elif s=='r':
                return (x,y+1)
            elif s=='t':
                return (x-1,y)
            else:
                return (x+1,y)

        stack.append(start)
        grid = [l[:] for l in self.navigator_maze]

        while stack.top()!=end:
            curr = stack.top()
            x = curr[0]
            y = curr[1]
            new_x,new_y=None,None
            for i in ['l','r','t','b']:
                if y==0 and i =='l':
                    continue
                if y==n-1 and i=='r':
                    continue
                if x==0 and i =='t':
                    continue
                if x==m-1 and i=='b':
                    continue
                new_x,new_y = update(x,y,i)
                if grid[new_x][new_y]==1 or (new_x,new_y)==start:
                    new_x,new_y=None,None
                    continue
                stack.append((new_x,new_y))
                grid[new_x][new_y]=1
                break
            if stack.top()==start:
                raise PathNotFoundException
                
            if (new_x,new_y)==(None,None):
                stack.pop()
            
        # print(stack.show()) 
           
        return stack.show()


