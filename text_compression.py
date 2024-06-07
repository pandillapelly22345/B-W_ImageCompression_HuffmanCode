import heapq
from collections import defaultdict

# Function to calculate character frequencies
def calculate_frequency(text):
    frequency = defaultdict(int) # default dict - to count occurences of each charecter. It set the default value as 0. 
    for char in text:
        frequency[char] += 1
    return frequency

# Node class for Huffman tree
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char #the character associated with the node.
        self.freq = freq #the character fequency associated with the node.
        self.left = left #left child of the node, which represents 0.
        self.right = right #right child of the node, which represents 1.

    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman tree
def build_huffman_tree(text):
    frequency = calculate_frequency(text)
    queue = [Node(char, freq) for char, freq in frequency.items()] # Creating a list of leaf nodes, each representing a character and its frequency

    heapq.heapify(queue)

    while len(queue) > 1:
        # Pop two nodes with the lowest frequencies from the heap
        lo = heapq.heappop(queue)
        hi = heapq.heappop(queue)
        
        # new internal node
        total = lo.freq + hi.freq
        heapq.heappush(queue, Node(None, total, lo, hi))

    return queue[0]

# Function to encode text using Huffman codes
def huffman_encode(node, text, encoding):
    if node is None: # function has reached to an empty node
        return

    if node.char is not None:
        encoding[node.char] = text

    huffman_encode(node.left, text + "0", encoding)
    huffman_encode(node.right, text + "1", encoding)

# Function to perform Huffman encoding
def huffman_encoding(text):
    node = build_huffman_tree(text)
    encoding = {}
    huffman_encode(node, "", encoding)
    encoded_text = ''.join(encoding[char] for char in text)
    return encoded_text, node

# Function to decode Huffman-encoded text
def huffman_decode(encoded_text, tree):
    current_node = tree
    decoded_text = ""

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right

        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = tree

    return decoded_text

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    text = user_input

    # Encoding
    encoded_text, huffman_tree = huffman_encoding(text)
    print("Encoded text:", encoded_text)

    # Decoding
    decoded_text = huffman_decode(encoded_text, huffman_tree)
    print("Decoded text:", decoded_text)
