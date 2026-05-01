class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for courses, pre in prerequisites:
            preMap[courses].append(pre)
        
        visitedSet = set()

        def dfs(courses):
            if courses in visitedSet:
                return False
            
            if preMap[courses] == []:
                return True
            
            visitedSet.add(courses)
            for pre in preMap[courses]:
                if not dfs(pre):
                    return False
            
            visitedSet.remove(courses)
            preMap[courses] = []
            return True
        
        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True
