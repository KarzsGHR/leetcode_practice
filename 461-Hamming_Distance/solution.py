# Solution
class Solution(object):
	def hammingDistance(self,x, y):
		t=0
		for xb,yb in zip('{:032b}'.format(x),'{:032b}'.format(y)):
			if xb != yb:
				t+=1
		return t


# test Case
a=Solution()

print a.hammingDistance(1,4)