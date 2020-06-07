# Data Structure Nanodegree Project 

### Project 1 LRU Cache
For the LRU Cache I have used orderdict as it helps in maintaining the priority

The space complexity

For a cache of size x, x space is used in the memory and there is no usage of extra memory O(n) where n is memory used.

The Time complexity is O(1).

### Project 2 Recurssion
The method is recursively used to search the file with the prefix for each folder and subfolder

### Time and Space complexity

The time complexity depends on how many times the recursion call happens and how many files and subfolders are present in each folder.

If the max depth i.e. total pushes to the call stack is d and the max number of files and sub folder in any folder is L then the max complexity is O(d*L)

The space complexity is O(1)


### Project 3 Huffmann Algorithm

The implementation was divided based on the Node, map, tree and HeapQ.

### Time and Space complexity

The complexity of the algorithm is O(L*d) similar to previous explanation where L is length of code and d is the depth of tree.

The space complexity is O(n) Where n is the number of elements

### Project 4 Active Directory

It is a recursive algorithm which is called recursively till the user is found.

### Time and Space complexity

The complexity is O(groups * users) i.e. number of groups and users present in each group where groups gets pushed in the call stack for recurssion.

The space complexity is O(1)

### Project 5 BlockChain

Using Linked list to add elements to a blockchain

### Time and Space complexity

The time complexity for the append O(n) to traverse till the end of the list and then add the element to the end of the list where n is the total number of elements in the linkedlist

It can be made such that the element is added to the front and the complexity is O(1)

The space complexity is O(n) where n is the number of elements in the linkedlist

Both the versions are present in the code.

### Project 6 Union and Intersection
Used linked list for the algorithm.

Union wa allowed with duplicate values as the inputs itself had duplicate values.

Intersection was not allowed with duplicate and was eliminated with set.

### Time and Space complexity

For Union the time complexity was O(n) while for Intersection it was O(n*n) where n is the number of element in the list.

The space complexity is O(n) for union
The space complexity is O(n) for intersection where n is the total number of element in both the array
