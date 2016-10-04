#插入排序算法
def insertionSort(alist):
	start_time = time.time()
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index
		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1
		alist[position]=currentvalue
	print time.time() - start_time
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

#选择排序

def selectionSort(alist):
	for fiilslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1,fiilslot + 1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location
		temp = alist[fiilslot]
		alist[fiilslot] = alist[positionOfMax]
		alist[positionOfMax] = temp


#合并排序
def mergeSort(alist):
	print("Splitting",alist)
	if len(alist) > 1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i = 0
		j = 0
		k = 0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i = i + 1
			else:
				alist[k] = righthalf[j]
				j = j + 1
			k = k + 1
		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i = i + 1
			k = k + 1
		print("Merging",alist)

#冒泡算法

def bubbleSort(alist):
	for i in range(len(alist)-1,0,-1):
		for j in range(i):
			if alist[j] > alist[j + 1]:
				temp  = alist[j]
				alist[j] = alist[j + 1]
				alist[j + 1] = temp



##quicksort 1

def quicksort(array):
	less = []
	equal = []
	greater = []
	if len(array) > 1:
		pivot = array[0]
		for x in array:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		# Don't forget to return something!
		return quicksort(less)+equal+quicksort(greater)# Just use the + operator to join lists
		# Note that you want equal ^^^^^ not pivot
	else:# You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
		return array

##quicksort 2

def quicksort(alist):
	if not alist:
		return []
	pivots = [x for x in alist if x == alist[0]]
	less = quicksort([x for x in alist if x < alist[0]])
	greater = quicksort([x for x in alist if x > alist[0]])
	return less + pivots + greater

#Max Subarray Naive
#works for all numbers ,even all negative.

def MaxSubarray(alist):
	if alist is None or len(alist) == 0:
		return 0
	maxSum = alist[0]
	miniSum = 0
	sum = 0
	for x in alist:
		sum += x
		if sum - miniSum > maxSum:
			maxSum = sum - miniSum
		if sum < miniSum:
			miniSum = sum
	return maxSum

#Max Subarray Naive 2 
#doesn't work for all negative numbers ,just return 0

def MaxSubarray(alist):
	max = 0
	sum = 0
	for x in alist:
		sum += x
		if sum < 0:
			sum = 0
		elif (max < sum):
			max = sum
	return max


#Max Subarray D&C

def MaxCrossingSubarray(a,low,mid,high):
	leftSum = None
	maxLeft = 0
	sum1 = 0
	for i in range(mid,low - 1, -1):
		sum1 = sum1 + a[i]
		if None == leftSum:
			leftSum = sum1
			maxLeft = i
		elif sum1 > leftSum:
			left_sum = sum1
			maxLeft = i
	rightSum = None
	sum2 = 0
	maxRight = 0
	for j in range(mid + 1,high + 1):
		sum2 = sum2  + a[j]
		if None == rightSum:
			rightSum = sum2
			maxRight = j
		elif sum2 > rightSum:
			rightSum = sum2
			maxRight = j
	return maxLeft,maxRight,leftSum + rightSum

def MaximumSubarray(a,low,high):
	mid = (low + high)/2
	leftSum = a[low]
	rightSum = a[high]
	if high == low:
		return low,high,a[low]
	else:
		mid == (low + high)/2
		leftLow,leftHigh,leftSum = MaximumSubarray(a,low,mid)
		rightLow,rightHigh,rightSum = MaximumSubarray(a,mid + 1,high)
		crossLow,crossHigh,crossSum = MaxCrossingSubarray(a,low,mid,high)
		if leftSum >= rightSum and leftSum >= crossSum:
			return leftLow,rightHigh,rightSum
		elif rightSum >= leftSum and rightSum >= crossSum:
			return  rightLow,rightHigh,rightSum
		else:
			return crossLow,crossHigh,crossSum
MaximumSubarray(a,0,len(alist) - 1)

#Strassen algorithm

a = [[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]
b = [[5,5,5,5],[6,6,6,6],[7,7,7,7],[8,8,8,8]]


def new_m(p, q): # create a matrix filled with 0s
	matrix = [[0 for row in range(p)] for col in range(q)]
	return matrix

def straight(a, b): # multiply the two matrices
	if len(a[0]) != len(b): # if # of col != # of rows:
		return "Matrices are not m*n and n*p"
	else:
		p_matrix = new_m(len(a), len(b[0]))
		for i in range(len(a)):
			for j in range(len(b[0])):
				for k in range(len(b)):
					p_matrix[i][j] += a[i][k]*b[k][j]
	return p_matrix

def split(matrix): # split matrix into quarters 
	a = matrix
	b = matrix
	c = matrix
	d = matrix
	while(len(a) > len(matrix)/2):
		a = a[:len(a)/2]
		b = b[:len(b)/2]
		c = c[len(c)/2:]
		d = d[len(d)/2:]
	while(len(a[0]) > len(matrix[0])/2):
		for i in range(len(a[0])/2):
			a[i] = a[i][:len(a[i])/2]
			b[i] = b[i][len(b[i])/2:]
			c[i] = c[i][:len(c[i])/2]
			d[i] = d[i][len(d[i])/2:]
	return a,b,c,d

def add_m(a, b):
	if type(a) == int:
		d = a + b
	else:
		d = []
		for i in range(len(a)):
			c = []
			for j in range(len(a[0])):
				c.append(a[i][j] + b[i][j])
			d.append(c)
	return d

def sub_m(a, b):
	if type(a) == int:
		d = a - b
	else:
		d = []
		for i in range(len(a)):
			c = []
			for j in range(len(a[0])):
				c.append(a[i][j] - b[i][j])
			d.append(c)
	return d


def strassen(a, b, q):
	# base case: 1x1 matrix
	if q == 1:
		d = [[0]]
		d[0][0] = a[0][0] * b[0][0]
		return d
	else:
		#split matrices into quarters
		a11, a12, a21, a22 = split(a)
		b11, b12, b21, b22 = split(b)
		# p1 = (a11+a22) * (b11+b22)
		p1 = strassen(add_m(a11,a22), add_m(b11,b22), q/2)
		# p2 = (a21+a22) * b11
		p2 = strassen(add_m(a21,a22), b11, q/2)
		# p3 = a11 * (b12-b22)
		p3 = strassen(a11, sub_m(b12,b22), q/2)
		# p4 = a22 * (b12-b11)
		p4 = strassen(a22, sub_m(b21,b11), q/2)
		# p5 = (a11+a12) * b22
		p5 = strassen(add_m(a11,a12), b22, q/2)
		# p6 = (a21-a11) * (b11+b12)
		p6 = strassen(sub_m(a21,a11), add_m(b11,b12), q/2)
		# p7 = (a12-a22) * (b21+b22)
		p7 = strassen(sub_m(a12,a22), add_m(b21,b22), q/2)
		# c11 = p1 + p4 - p5 + p7
		c11 = add_m(sub_m(add_m(p1, p4), p5), p7)
		# c12 = p3 + p5
		c12 = add_m(p3, p5)
		# c21 = p2 + p4
		c21 = add_m(p2, p4)
		# c22 = p1 + p3 - p2 + p6
		c22 = add_m(sub_m(add_m(p1, p3), p2), p6)
		c = new_m(len(c11)*2,len(c11)*2)
		for i in range(len(c11)):
			for j in range(len(c11)):
				c[i][j]                   = c11[i][j]
				c[i][j+len(c11)]          = c12[i][j]
				c[i+len(c11)][j]          = c21[i][j]
				c[i+len(c11)][j+len(c11)] = c22[i][j]
		return c

strassen(a,b,4)


#random quick select


import random
def q_select(numbers, ith):
	if len(numbers) < 2:
		return numbers[0]
	# Chooses a pivot uniformly from random
	p_index = random.randint(0, len(numbers)-1)
	pivot = numbers[p_index]

	# Before the partition, swap the pivot with the last element
	numbers[p_index], numbers[-1] = (
		numbers[-1], numbers[p_index])

	# i is always the last element smaller than your pivot
	# j is always the first element larger than your pivot
	i = -1
	for j in xrange(0, len(numbers)):
		if numbers[j] < pivot:
			numbers[j], numbers[i+1] = (
				numbers[i+1], numbers[j]
			)
			i += 1

	# After partition swap back the pivot to its rightful position
	numbers[i+1], numbers[-1] = (
		numbers[-1], numbers[i+1]
	)

	# Update the new pivot index (where it should be belong now)
	p_index = i + 1

	# Since we are using zero-indexed list, subtract 1 from everything
	if p_index == ith - 1:
		return numbers[p_index]
	# When the ith order statistics is to the right of pivot
	elif ith > p_index:
		return q_select(numbers[p_index+1:], ith - p_index - 1)
	else:
		return q_select(numbers[:p_index], ith)

a = [33,23,12,67,45,78,10,39,11,58]
print q_select(a,3)

#heap sort

'''

Heapsort is an in-place sorting algorithm with worst case and average complexity of   O(n logn).

The basic idea is to turn the array into a binary heap structure, which has the property that it allows efficient retrieval and removal of the maximal element.

We repeatedly "remove" the maximal element from the heap, thus building the sorted list from back to front.

Heapsort requires random access, so can only be used on an array-like data structure.

Pseudocode:

function heapSort(a, count) is
   input: an unordered array a of length count
 
   (first place a in max-heap order)
   heapify(a, count)
 
   end := count - 1
   while end > 0 do
      (swap the root(maximum value) of the heap with the
       last element of the heap)
      swap(a[end], a[0])
      (decrement the size of the heap so that the previous
       max value will stay in its proper place)
      end := end - 1
      (put the heap back in max-heap order)
      siftDown(a, 0, end)

function heapify(a,count) is
   (start is assigned the index in a of the last parent node)
   start := (count - 2) / 2
   
   while start ≥ 0 do
      (sift down the node at index start to the proper place
       such that all nodes below the start index are in heap
       order)
      siftDown(a, start, count-1)
      start := start - 1
   (after sifting down the root all nodes/elements are in heap order)
 
function siftDown(a, start, end) is
   (end represents the limit of how far down the heap to sift)
   root := start

   while root * 2 + 1 ≤ end do       (While the root has at least one child)
      child := root * 2 + 1           (root*2+1 points to the left child)
      (If the child has a sibling and the child's value is less than its sibling's...)
      if child + 1 ≤ end and a[child] < a[child + 1] then
         child := child + 1           (... then point to the right child instead)
      if a[root] < a[child] then     (out of max-heap order)
         swap(a[root], a[child])
         root := child                (repeat to continue sifting down the child now)
      else
         return

'''


def heapsort(lst):
	''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
	# in pseudo-code, heapify only called once, so inline it here
	for start in range((len(lst)-2)/2, -1, -1):
		siftdown(lst, start, len(lst)-1)
	for end in range(len(lst)-1, 0, -1):
		lst[end], lst[0] = lst[0], lst[end]
		siftdown(lst, 0, end - 1)
	return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break



#hash table & hash map, insert ,put ,get

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self,key,data):
		hashvalue = self.hashfunction(key,len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data  #replace
			else:
				nextslot = self.rehash(hashvalue,len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot,len(self.slots))
					if self.slots[nextslot] == None:
						self.slots[nextslot]=key
						self.data[nextslot]=data
					else:
						self.data[nextslot] = data #replace

	def hashfunction(self,key,size):
		 return key%size

	def rehash(self,oldhash,size):
		return (oldhash+1)%size

	def get(self,key):
		startslot = self.hashfunction(key,len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position=self.rehash(position,len(self.slots))
				if position == startslot:
					stop = True
		return data

	def __getitem__(self,key):
		return self.get(key)

	def __setitem__(self,key,data):
		self.put(key,data)

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20]='duck'
print(H[20])
print(H[99])



#binary tree

class Tree:
	def __init__(self,value):
		self.root = None
		self.left = None
		self.right = None
		self.data = value

	def addNode(self,value):
		if self.data:
			if value < self.data:
				if self.left is None:
					self.left = Tree(value)
				else:
					self.left.addNode(value)
			elif value > self.data:
				if self.right is None:
					self.right = Tree(value)
				else:
					self.right.addNode(value)
		else:
			self.data = value

	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print self.data,
		if self.right:
			self.right.print_tree()

	def findMinNode(self,node):
		if node.left == None:
			return node.data
		else:
			node.data = node.left
			return self.findMinNode(node.left)
	def findMaxNode(self,node):
		if node.right == None:
			return node.data
		else:
			node.data = node.right
			return self.findMaxNode(node.right)

	def lookup(self, value, parent=None):
		"""
		Lookup node containing data

		@param data node data object to look up
		@param parent node's parent
		@returns node and node's parent if found or None, None
		"""
		if value < self.data:
			if self.left is None:
				return None, None
			return self.left.lookup(value, self)
		elif value > self.data:
			if self.right is None:
				return None, None
			return self.right.lookup(value, self)
		else:
			return self, parent

	def children_count(self):
		"""
		Returns the number of children

		@returns number of children: 0, 1, 2
		"""
		cnt = 0
		if self.left:
			cnt += 1
		if self.right:
			cnt += 1
		return cnt


	def delete(self, data):
		"""
		Delete node containing data

		@param data node's content to delete
		"""
		# get node containing data
		node, parent = self.lookup(data)
		if node is not None:
			children_count = node.children_count()
		if children_count == 0:
			# if node has no children, just remove it
			if parent:
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			else:
				self.data = None
		elif children_count == 1:
			# if node has 1 child
			# replace node with its child
			if node.left:
				n = node.left
			else:
				n = node.right
			if parent:
				if parent.left is node:
					parent.left = n
				else:
					parent.right = n
				del node
			else:
				self.left = n.left
				self.right = n.right
				self.data = n.data
		else:
			# if node has 2 children
			# find its successor
			parent = node
			successor = node.right
			while successor.left:
				parent = successor
				successor = successor.left
			# replace node data by its successor data
			node.data = successor.data
			# fix successor's parent's child
			if parent.left == successor:
				parent.left = successor.right
			else:
				parent.right = successor.right

testTree = Tree(8)
testTree.addNode(3)
testTree.addNode(10)
testTree.addNode(1)
testTree.addNode(6)
testTree.addNode(4)
testTree.addNode(7)
testTree.addNode(14)
testTree.addNode(13)
testTree.print_tree()
print testTree.lookup(8)[0]
testTree.delete(3)
testTree.print_tree()

