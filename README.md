# algorithms

This is just a personal reference repo of Data Structures and Algorithms. 

### Binary Search vs Linear Search
- Binary search is O(log n), while linear search is O(n). Binary search halves the search space at each operation, while linear search reduces the search space by exactly one element at an operation.
- Linear search is simple to write, while binary search can introduce bugs.

### Arrays vs Linked Lists
- If you want to store n items together, your computer may find memory blocks that sit right next to each other and create an array of n items in memory.
- If you want to add more items, but there's some other program using the memory right after your initial array ends, your computer would need to find another place to fit n + 1 items right next to each other. A get around is that it could initially just offer you 10 * n space for storage, but you might not ever use that much space (memory wastage) or you might end up with a case where you have  10 * n + 1 items, in which case your computer would need to find at least that much space again and copy all of the items from your initial array into the new location in the exact order. This can be a very slow process.
- In linked list, your items can be anywhere, and each item has the address of the next item in the order your intended them to be in. The packaging of this is such that you put the actual item (number or letter) with the address of the next item in something called a node. This node knows where the next node is, since it has the address of the next node.
- In linked list, you can just keep adding items to the end of the list (appending) without worrying about moving your data. The downside to this structure is that to read the contents of the last node (the number or letter stored in it), you have to start from the very first node, where you ask it where the next node is. The next node then points to its next node. Eventually, you will reach the end where the last node points to nothing (None in Python) since it does not know the address of the next item because we never kept on adding new items.
- Arrays are better if you want to randomly read any item. You don't have to start from the very item. The logic for this is simple. If your house has the address 0, your neighbor is at 1 and their next neighbor at 2 and so on, then to get to the 5th house in your neighborhood, I just enter 4 in my maps app (your house-0 1 2 3 4-5th house).
- This means, if you care about really fast insertions, linked list will be blazing, while array will be slow. If you care about really fast reading, array will be faster than linked list. In CS lingo, this means O(1) insertion for linked list, while O(n) insertion for arrays. On the reading side, O(n) read for linked list, and O(1) read for arrays.

### Appendix
- O(1) = Constant Time
- O(n) = Linear Time
- O(log n) = Logarithmic Time 
