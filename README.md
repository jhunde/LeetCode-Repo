# [61. Rotate List ](61_Rotate_List.py)
Example = `head = [1, 2, 3, 4, 5]` and `k = 2`

1. Count the length of the Linked List
   + This will include keeping track of the tail
2. Traverse through the Linked List from the begining (`curr = head`) until `length - (k % length) - 1`
   + Keep in mind that `- 1` is included in the range to account for the `head` 
   + This will help locate the new tail
3. Link the old `tail` back to `head` (making it circular Linked List)
4. Create a copy of the new head (`newHead = curr.next)
5. Update your tail (`curr.next = None`)
   + Keep in mid that you must make a copy of new head FIRST
6. Return the start of your Linked List 

```mermaid
graph LR;
    A1[["1"]] --> A2[["2"]];
    A2 --> A3[["3"]];
    A3 --> A4[["4"]];
    A4 --> A5[["5"]];

    subgraph "Original List"
	    A1; A2; A3; A4; A5;

		subgraph "Tail links to Head"
		    A5 --"tail.next = head" --> A1
		end

		 subgraph "Finding New Tail (k=2)" 
		    A1 -."Move length - k - 1 = 5 - 2 - 1 = 2 steps".-> A3;
	    end
    end
 
	
    subgraph "After Rotation (k=2)"
	    subgraph "new head"
			B4[[4]]
		end 
		
	    A3 --"newHead = curr.next"--> B4[["4"]];
	    B4 --> B5[["5"]];
	    B5 --> B1[["1"]];
	    B1 --> B2[["2"]];

		subgraph "break cycle"
			subgraph "new tail"
			    B3[[3]]
			end

		    B3 -.->|curr.next = None| null(["None"]);
		end
		B2 --> B3;

    end
```
