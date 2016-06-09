class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        slashStack = ['/']
        for i in range(0, len(paths)):
            if paths[i] == '..':
                if len(slashStack) != 0:
                    slashStack.pop()
                if len(slashStack) != 0:
                    slashStack.pop()
                if len(slashStack) == 0:
                    slashStack.append('/')
                continue
            if paths[i] == '' or paths[i] == '.':
                continue
            slashStack.append(paths[i])
            slashStack.append('/')
        if len(slashStack) != 1:
            slashStack.pop()
        return "".join(slashStack)

mytest = Solution()
path = "/home/../../.."
print mytest.simplifyPath(path)
