#  https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=problem-list-v2&envId=trie
# Solution: Sorting + Prefix
# Method:
# - sort folders. check if left is subfolder of right

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        folders.sort()

        res = []
        for folder in folders:
            if not res or not folder.startswith(res[-1] + '/'):
                res.append(folder)
        
        return res

