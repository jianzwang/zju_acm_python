import sys
from collections import deque

line= sys.stdin.readline()

# -1 :Don't Do anything
# 0 :fill A :p.a = a
# 1 :fill B :p.b = b
# 2 :Empty A:p.a = 0
# 3 :Empty B:p.b = 0
# 4 :pour A B : p.a = p.b + p.a < b ? 0 : b - p.b,p.b = min(b,p.b+p.a) 
# 5 :pour B A : p.b = p.a + p.b < a ? 0 : a - p.a,p.a = min(a,p.b+p.a)

sentences = {0:'fill A',1:'fill B',2:'empty A',3:'empty B',4:'pour A B',5:'pour B A'}
class Point:
	def __init__ (self,maxA,maxB):
		self.maxA = maxA
		self.maxB = maxB
		self.a = 0
		self.b = 0
		self.status = -1
		self.parent = None

	def __repr__(self):
		global flags
		return 'a:%d,b:%d,status:%d,flag:%d\n'%(self.a,self.b,self.status,flags[self.a][self.b])
	def invoke(self,i):
		maxA = self.maxA
		maxB = self.maxB

		p = Point(maxA,maxB)
		p.status = i
		p.parent = self
		if i == 0:
			p.b = self.b
			p.a = maxA
	
			
		elif i == 1:
			p.a = self.a
			p.b = maxB
			
			
		elif i == 2:
			p.a = 0
			p.b = self.b
			
			
		elif i == 3:
			p.b = 0
			p.a = self.a
			
			
		elif i == 4:
			if self.b == maxB or self.a == 0:
				p = None

			elif self.a + self.b <= maxB:
				p.a = 0
				p.b = self.a + self.b
			else:
				p.a = self.a - (maxB  - self.b)
				p.b = maxB
	
		elif i == 5:
			if self.a == maxA or self.b == 0:
				p = None
			elif self.a + self.b <= maxA:
				p.a = self.a + self.b
				p.b = 0
			else:
				p.b = self.b - (maxA - self.a)
				p.a = maxA

		return p

def printPath(p):
	global sentences
	if p and p.parent :
		printPath(p.parent)
	#sys.stdout.write(sentences.get(p.status))
	#print p.status
	#print p
	order = sentences.get(p.status)
	if order :
		print order



while line:
	tokens = line.split()
	a,b,n = int(tokens[0]),int(tokens[1]),int(tokens[2])
	flags = [ [-1 for i in range(b+1)] for j in range(b+1)]
	q = deque([Point(a,b)])
	flags[0][0] = 0
	top = q.popleft()
	while top:
		#print 'top:%s'%(top)
		if top.b == n:
			printPath(top)
			print 'success'
			break;

	
		for i in range(0,6):
			p = top.invoke(i)

			if p :
				#print p
				if flags[p.a][p.b] == -1 :
					flags[p.a][p.b] = p.status
					q.append(p)

		#print q
		top = q.popleft()

	line = sys.stdin.readline()

