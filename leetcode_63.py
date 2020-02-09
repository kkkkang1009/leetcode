# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i-1 < 0 and j-1 < 0:
                        obstacleGrid[i][j] = 1
                    elif i-1 < 0 and j-1 >= 0:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    elif j-1 < 0 and i-1 >= 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        answer = obstacleGrid[m-1][n-1]
        return answer

# 1st - Wrong Answer
# def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#     total = self.uniquePaths(len(obstacleGrid), len(obstacleGrid[0]))
#     obstacle_x, obstacle_y = 0, 0
#     for i in range(0, len(obstacleGrid)):
#         for j in range(0, len(obstacleGrid[0])):
#             if obstacleGrid[i][j] == 1:
#                 obstacle_x = i
#                 obstacle_y = j
#                 break
#     obstacle_1 = self.uniquePaths(obstacle_x + 1, obstacle_y + 1)
#     obstacle_2 = self.uniquePaths(len(obstacleGrid) - obstacle_x, len(obstacleGrid[0]) - obstacle_y)
#     answer = total - (obstacle_1 * obstacle_2)
#
#     return answer

#     Input:[[0]]
#     0 하나나 한줄 짜리 배열에 대한 생각 못함
#     해당 조건에 대한 조건문 생성

# 2nd - Wrong Answer
# def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#     if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
#         for i in range(0, obstacleGrid[0])
#         if 1 in obstacleGrid or 1 in obstacleGrid[0]:
#             return 0
#         else:
#             return 1
#     total = self.uniquePaths(len(obstacleGrid),len(obstacleGrid[0]))
#     obstacle = False
#     obstacle_x, obstacle_y = 0, 0
#     for i in range(0, len(obstacleGrid)):
#         for j in range(0, len(obstacleGrid[0])):
#             if obstacleGrid[i][j] == 1:
#                 obstacle = True
#                 obstacle_x = i
#                 obstacle_y = j
#                 break
#     if obstacle:
#         obstacle_1 = self.uniquePaths(obstacle_x+1, obstacle_y+1)
#         obstacle_2 = self.uniquePaths(len(obstacleGrid)-obstacle_x, len(obstacleGrid[0])-obstacle_y)
#         answer = total - (obstacle_1 * obstacle_2)
#     else:
#         answer = total
#     return answer

#     Input:[[0, 1], [1, 0]]
#     장애물이 2개 이상이 될 수 있다는 것을 생각 못함
#     심지어 한 줄짜리 배열 처리 조건문도 잘못 작성
#     새로운 방식으로 접근 필요해 전체성 코드 새로 작성