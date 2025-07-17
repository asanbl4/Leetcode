class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = [i for i in path.split('/') if i != '']
        stk = []
        for i in range(len(directories)):
            try:
                if directories[i] == '..':
                    stk.pop(-1)
                elif directories[i] == '.':
                    pass
                else:
                    stk.append(directories[i])
            except IndexError:
                stk = []
        return '/' + '/'.join(stk)



if __name__ == '__main__':
    path = "/.../"
    print(Solution().simplifyPath(path))