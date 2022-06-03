class Node:
    	
	def __init__(self,data):
		self.data = data
		self.next = None
	
class Stack:
	def __init__(self):
		self.head = None
	
	def isempty(self):
		if self.head == None:
			return True
		else:
			return False
	
	def push(self,data):
		
		if self.head == None:
			self.head=Node(data)
			
		else:
			newnode = Node(data)
			newnode.next = self.head
			self.head = newnode
	
	def pop(self):
		
		if self.isempty():
			return None
			
		else:
			poppednode = self.head
			self.head = self.head.next
			poppednode.next = None
			return poppednode.data
	
	def peek(self):
		
		if self.isempty():
			return None
			
		else:
			return self.head.data
	
	def display(self):
		
		iternode = self.head
		if self.isempty():
			print("Stack Underflow")
		
		else:
			
			while(iternode != None):
				
				print(iternode.data,"->",end = " ")
				iternode = iternode.next
			return
		
MyStack = Stack()

MyStack.push(12)
MyStack.push(21)
MyStack.push(33)
MyStack.push(44)

MyStack.display()

print("\nLeft element is ",MyStack.peek())

MyStack.pop()
MyStack.pop()

MyStack.display()

print("\nRight element is ", MyStack.peek())