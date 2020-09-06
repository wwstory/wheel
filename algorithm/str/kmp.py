
class kmp:
    def __call__(self, s, p):

        if not s or not p or (len(p) > len(s)): # 边界：都为空字符串，或模式串为空，或模式串比源串长
            return -1
        
        next_list = self.get_next(p)
        pos = -1

        i = j = 0
        while j < len(p):
            if s[i] == p[j]:
                i += 1
                j += 1
                if j == len(p):
                    pos = i - j
                    break
            else:
                j = next_list[j]
                if j == -1:
                    i += 1
                    j = 0
                if len(s) - i < len(p) - j: # 剩余子串不够匹配
                    break
        return pos


    def get_next(self, p):
        '''
            'abcabcde' -> [-1, 0, 0, 0, 1, 2, 3, 0]
            next列表存放的是，模式串第i位从头开始有多少位是相同的。
            头部增加1个'-1'值，便于操作。
        '''
        i = 0
        j = -1
        next_list = [-1]

        while i < len(p) - 1:
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                next_list.append(j)
            else:
                j = next_list[j]
        return next_list

if __name__ == "__main__":
    s = 'abcdaaaabcabcdebbb'
    k = kmp()
    print(k(s, 'abcabcde'))