import hashlib
import datetime



class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = self.data

      sha.update(hash_str)

      return sha.hexdigest()


class BlockChain(object):
	"""docstring for BlockChain"""
	def __init__(self):

		self.head = None

	def append(self, value):
		if value is None:
			return

		if self.head is None:
			self.head = Block(datetime.datetime.now(), value, None)
			return
		# Move to the tail (the last node)
		node = self.head

		nextNode = node.next

		newNode = Block(datetime.datetime.now(), value, node.hash)

		newNode.next = nextNode

		node.next = newNode


		# while node.next:
		# 	node = node.next
		
		# node.next = Block(datetime.datetime.now(), value, node.hash)

		return



		
blockChain = BlockChain()

blockChain.append("We are going to encode this string of data!".encode('utf-8'))

blockChain.append("new string data".encode('utf-8'))


print("-----------------------------Test 1-------------------------------------")

print("The message ", blockChain.head.data, " is encoded to ", blockChain.head.hash)


print("-----------------------------Test 2-------------------------------------")

print("The message ", blockChain.head.next.data, " is encoded to ", blockChain.head.next.hash)


print("-----------------------------Test 3-------------------------------------")


print("The message ", blockChain.head.next.next.data, " is encoded to ", blockChain.head.next.next.hash)
