import sys
import heapq

def frequency(data):
    
    letters = dict()

    for letter in data:
        if letters.get(letter):
            letters[letter]+=1
        else:
            letters[letter]=1

    return letters.items()

def huffman_map(tree, tempMap = dict(), encoding = ''):
    if(len(tree)==1):

        letter, charFrequency = tree[0]

        tempMap[letter] = encoding

    else:

        _, leftNode, rightNode = tree

        huffman_map(leftNode, tempMap, encoding+'0')
        huffman_map(rightNode, tempMap, encoding+'1')

    return tempMap

def huffman_tree(charFrequency):
    
    huffman_heap = []

    for frequency in charFrequency:
        heapq.heappush(huffman_heap, [frequency])

    while (len(huffman_heap)>1):

        leftNode = heapq.heappop(huffman_heap)
        rightNode = heapq.heappop(huffman_heap)

        leftFrequency, leftLetter = leftNode[0]

        rightFrequency, rightLetter = rightNode[0]

        combine = [(leftFrequency+rightFrequency, leftLetter + rightLetter), leftNode, rightNode]

        heapq.heappush(huffman_heap, combine)

    return huffman_heap.pop()

def huffman_encoding(data):
    huffmanTree = huffman_tree(frequency(data))

    huffmanMap = huffman_map(huffmanTree)

    encoded = ''.join([huffmanMap[letter] for letter in data])

    return encoded, huffmanTree
    

def huffman_decoding(data,tree):
    decoded=list()
    temp = tree

    for code in data:
        if code == '0':
            temp = temp[1]
        else:
            temp = temp[2]

        if (len(temp) == 1):
            letter, charFrequency = temp[0]
            decoded.append(letter)
            temp = tree

    decodedMessage = ''.join(decoded)

    return decodedMessage
    

if __name__ == "__main__":
    codes = {}


    print("-----------------------------Test 1-------------------------------------")

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    print("-----------------------------Test 2-------------------------------------")

    a_great_sentence = "Getting the hospital ready to receive patients is crucial. The flow must be carried out in accordance with the principle of “three zones and two passage”. Which in practice means unilateral entry and exit, and between them should be taken into account contaminated zone, potentially contaminated and clean. The communication route should also include the research room, laboratory, observation room and resuscitation room in turn."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("-----------------------------Test 3-------------------------------------")

    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print("-----------------------------Test 4-------------------------------------")

    a_great_sentence = "AAAAA"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

