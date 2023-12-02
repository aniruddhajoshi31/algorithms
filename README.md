# algorithms

This is just a personal reference repo of Data Structures and Algorithms. 

### Binary Search vs Linear Search
- Binary search is O(log n), while linear search is O(n). Binary search halves the search space at each operation, while linear search reduces the search space by exactly one element at an operation.
- Linear search is simple to write, while binary search can introduce bugs.

### Arrays vs Linked Lists
- If you want to store n items together, your computer may find memory blocks that sit right next to each other and create an array of n items in memory.
- If you want to add more items, but there's some other program using the memory right after your initial array ends, your computer would need to find another place to fit n + 1 items right next to each other. A get around is that it could initially just offer you 10 * n space for storage, but you might not ever use that much space (memory wastage) or you might end up with a case where you have  10 * n + 1 items, in which case your computer would need to find at least that much space again and copy all of the items from your initial array into the new location in the exact order. This can be a very slow process.
- In linked list, your items can be anywhere, and each item has the address of the next item in the order your intended them to be in. 
