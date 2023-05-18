class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        split_path = [x for x in path.split("/") if x != "" and x != "."]
        for ele in split_path:
            if ele == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(ele)
        return "/" + "/".join(stack)