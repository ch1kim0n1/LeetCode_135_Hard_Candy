class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        if n <= 1:
            return n
        total = 1
        up = down = 0
        old_slope = 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                slope = 1
            elif ratings[i] < ratings[i-1]:
                slope = -1
            else:
                slope = 0
            if (old_slope < 0 and slope >= 0) or (old_slope > 0 and slope == 0):
                total += (up*(up+1))//2 + (down*(down+1))//2 + max(up, down)
                up = down = 0
            if slope > 0:
                up += 1
            elif slope < 0:
                down += 1
            else:
                total += 1
            old_slope = slope
        total += (up*(up+1))//2 + (down*(down+1))//2 + max(up, down)
        return total
