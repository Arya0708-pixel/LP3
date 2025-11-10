import heapq

class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Recursive function to print Huffman Codes
def print_codes(root, code=""):
    if root is None:
        return
    if not root.left and not root.right:
        print(f"{root.ch} : {code}")
        return
    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")

# Build Huffman Tree
def build_huffman(chars, freqs):
    heap = [Node(chars[i], freqs[i]) for i in range(len(chars))]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node('-', left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    print("\nHuffman Codes:")
    print_codes(heap[0])

# Main part
n = int(input("Enter number of characters: "))
chars = input("Enter characters (no spaces): ").strip()
freqs = list(map(int, input("Enter their frequencies: ").split()))

build_huffman(list(chars), freqs)
