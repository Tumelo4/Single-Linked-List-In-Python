# Creating Node class

class Node:
	# constructor
	def __init__(self, data,next=None):
		self.data = data;
		self.next = next;

	def getData(self):
		return self.data;


class LinkedList:
	# constructor
	def __init__(self):
		self.head = None;

	# return the size of linked
	def size(self):
		count = 0;
		curr = self.head;

		while(curr):
		
			count = count + 1;
			curr = curr.next;
		
		return count;

	# add data at the beginning of linked using data that is pass as argument
	def prepend(self,data):
		if (self.head):
			curr = Node(data);
			curr.next = self.head;
			self.head = curr;
		else:
			self.head = Node(data);
	#  add data according to argument index
	def indexInsertion(self,data,index):
		if (index == 0):
			self.prepend(data);
		else:
			if ( index == self.size()):
				self.append(data);
			else:
				count = 0;
				curr = self.head;
				prev = None;
				while(count != index):
					prev = curr;
					curr = curr.next;
					count = count + 1;
				newNode = Node(data);
				newNode.next = curr;
				prev.next = newNode;
			
	# add data at the end
	def append(self,data):

		if(self.head):
			curr = self.head;

			while(curr.next):
				curr = curr.next;
			curr.next = Node(data);
		else:
			self.head = Node(data);

	# print all data store in the linked list
	def reverse(self):
		if(self.head):
			curr = self.head;
			prev = None;
			prepPrev = None;
			flag = False;


			while(curr):
				if (flag == False):
					if(prepPrev != None):
						prepPrev.next = None;
						prev.next = prepPrev;
						flag = True;
						
				else:
					prev.next = prepPrev;

				prepPrev = prev;
				prev = curr;
				curr = curr.next;

			if (self.size() == 2):
				prepPrev.next = None;
				prev.next = prepPrev;

			else:
				prev.next = prepPrev;
			self.head = prev;

	def printList(self):
		curr = self.head;
		string = "";
		while (curr):
			if (curr.next != None):
				string = string+str(curr.getData())+",";
			else:
				string = string+str(curr.getData());
			curr = curr.next;
		print(string);

def main():

	linkedList = LinkedList();

	linkedList.append(2);
	linkedList.append(4);
	linkedList.prepend(1);
	linkedList.indexInsertion(0,0);
	linkedList.indexInsertion(5,4);
	linkedList.indexInsertion(3,3);
	linkedList.printList();
	linkedList.reverse();
	linkedList.printList();

main();