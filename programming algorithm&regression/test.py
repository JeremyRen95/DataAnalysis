class State:
    def __init__(self, x, y, sum):
        self.x = x
        self.y = y
        self.sum = sum
    def __str__(self):
        return 'x=%d y=%d sum=%d'%(self.x, self.y, self.sum)
class Solution(object):
    min = float('inf')
    def forward(self, a_list, b_list, prev_state):
        s1_min, s2_min, s3_min = float("inf"), float("inf"), float("inf")
        a_len = len(a_list)
        b_len = len(b_list)
        s1, s2, s3 = None, None, None
        for state in prev_state:
            if state == None: continue
            if [state.x, state.y] == [a_len-1, b_len-1] and state.sum<self.min:
                self.min = state.sum
            if (state.x+2 < a_len) and (state.sum + a_list[state.x + 1] * a_list[state.x + 2] < s1_min):
                s1 = State(state.x + 2, state.y, state.sum + a_list[state.x + 1] * a_list[state.x + 2])
                s1_min = s1.sum
            if (state.x+1 < a_len) and (state.y+1 < b_len) and (state.sum + a_list[state.x + 1] * b_list[state.y + 1] < s2_min):
                s2 = State(state.x + 1, state.y + 1, state.sum + a_list[state.x + 1] * b_list[state.y + 1])
                s2_min = s2.sum
            if (state.y+2 < b_len) and (state.sum + b_list[state.y + 1] * b_list[state.y + 2] < s3_min):
                s3 = State(state.x, state.y + 2, state.sum + b_list[state.y + 1] * b_list[state.y + 2])
                s3_min = s3.sum
        return [s1,s2,s3]
    def min_sum(self, a_list, b_list):
        prev_state = [State(-1,-1,0),State(-1,-1,0),State(-1,-1,0)]
        min = float('inf')
        while prev_state != [None, None, None]:
            prev_state = self.forward(a_list=a, b_list=b, prev_state=prev_state)
        return self.min
if __name__ == '__main__':
    a = [1,4,1,1]
    b = [2,3,4,2]
    print( Solution().min_sum(a, b) )