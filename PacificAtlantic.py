class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific_list = collections.deque([])
        atlantic_list = collections.deque([])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0 or col == 0:
                    pacific_list.append((row, col))
                if row == len(matrix) - 1 or col == len(matrix[0]) - 1:
                    atlantic_list.append((row, col))     
        def bfs(deq):
            visited = set(deq)
            while deq:
                row, col = deq.popleft()
                for new_row, new_col in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                    if 0 <= new_row <= len(matrix) - 1 and 0 <= new_col <= len(matrix[0]) - 1 and (new_row, new_col) not in visited and matrix[new_row][new_col] >= matrix[row][col]:
                        visited.add((new_row, new_col))
                        deq.append((new_row, new_col))
            return visited
        return bfs(pacific_list) & bfs(atlantic_list)
