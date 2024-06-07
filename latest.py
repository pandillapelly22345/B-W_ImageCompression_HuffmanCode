import matplotlib.pyplot as plt
from PIL import Image
from collections import defaultdict
import heapq
import numpy as np
import cv2

# Function to count pixel occurrences in the image
def count_pixel_occurrences(image):
    flattened_image=image.flatten().tolist() #image(2D array of pixels)--converted in list(1D)
    #flatten()--converts in 1D ARRAY---tolist()--converts in list 1D
    pixel_counts=defaultdict(int) #defaultdict for storing pixel counts--key value pairs, if not specified assigns 0

    #iterating through our list of pixel_counts
    for pixel in flattened_image:
        pixel_counts[pixel] += 1

    return pixel_counts #returning the pixel_counts

# Node class for Huffman tree
class HuffmanNode:
    #self--instance of class
    #pixel--pixel value of this Node
    #frequency---is pixel frequency(how frequwnt it occurs
    # #left,right--left and right children of the node
    def __init__(self, pixel, frequency, left=None, right=None): #constructor method __init__
        self.pixel = pixel #stores the pixel value for this node in variable pixell
        self.frequency = frequency #stores pixel freq. of this node in variable frequency
        self.left = left #left child of this Node
        self.right = right #right child of this Node

    def __lt__(self, other): #lt--less than
        return self.frequency < other.frequency #comparing the frequency and then returning true or false

# Function to build the Huffman tree
def build_huffman_tree(image):
    # Count the frequencies of each pixel in the image
    pixel_counts = count_pixel_occurrences(image)#here :)
    #create a list of HuffmanNode objects, where each node represents a pixel and its frequency
    nodes = [HuffmanNode(pixel, freq) for pixel, freq in pixel_counts.items()]

    # Convert the list of nodes into a min heap
    # ---which is a priority queue 
    heapq.heapify(nodes) #where the node with the smallest frequency is always at the front.

    while len(nodes) != 1: #jab tak we are not left with only the root node
        lo = heapq.heappop(nodes) #pop the node with lowest freq
        #pop the node with hi freq
        hi = heapq.heappop(nodes) #here
        total_frequency = lo.frequency + hi.frequency #combined freq cal
        #new node crearion
        new_node = HuffmanNode(None, total_frequency, lo, hi)#new node--pixel value=None,two popped nodes are its lft n rgt children
        heapq.heappush(nodes, new_node)

    return nodes[0]  #root is  remaining node

# Function to generate Huffman codes for each pixel
def generate_huffman_codes(node, code, encoding):
    if node is None: #current node is None--- we've reached a leaf node or an empty node in the Huffman tree
        return #nothing to be done

    if node.pixel is not None: #then update the encoding dict
        encoding[node.pixel] = code
    #it uses "0" for the left child and "1" for the right child
    # #constructing the Huffman codes for each pixel and updating the encoding dict
    generate_huffman_codes(node.left, code + "0", encoding)
    generate_huffman_codes(node.right, code + "1", encoding)

# Function to perform Huffman encoding
def huffman_encoding(image):
    #building the h.tree---using--pixel frequencies in the image
    tree = build_huffman_tree(image)
    codes = {} #empty dict create---store huffman codes for each pixel
    generate_huffman_codes(tree, "", codes) #generating huffman code for each pixel n storing it in the "codes" dict

    # Encode the image using Huffman codes
    encoded_image = ''.join(codes[pixel] for pixel in image.flatten().tolist())
    return encoded_image, tree #encoded img and huffman tree

# Function to decode Huffman-encoded image
def huffman_decode(encoded_image, tree, image_shape):
    #encoded_image ---huffman encoded binary string.
    #tree --the huffman tree built during encoding process
    #image_Shape---shape o original img
    current_node = tree #current node---initial. at root 
    decoded_pixels = [] #will store decoded pixel values

    #iterate
    for bit in encoded_image: #each bit in the Huffman-encoded binary string
        #current bit---if the bit is "0", it moves to the left child; if "1", it moves to the right child
        current_node = current_node.left if bit == "0" else current_node.right

        if current_node.pixel is not None: #checks if the current node is a leaf node 
            decoded_pixels.append(int(current_node.pixel)) #if the current node is a leaf node-- append the pixel value to list
            current_node = tree #reset to root

    # Convert the list of decoded pixels to a NumPy array and reshape
    decoded_image = np.array(decoded_pixels).reshape(image_shape)
    return decoded_image #yes got the image

# Function to load image
def load_image(file_path):
    image = Image.open(file_path) # Open the image file
    # Convert the image to grayscale for simplicity
    image = np.array(image.convert("L"))
    return image #as a numpy array

def gaussian_smoothing(image):
    # Apply Gaussian smoothing to the image
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

if __name__ == "__main__":

    # Loading the lotus.jpg image
    #loads the image lotus.jpg  from the path provided, stores the image data in the variable image_data
    image_data = load_image(r"C:\Users\hp\Desktop\DiscreteMP\lotus.jpg")

    # Gaussian smoothing before compression
    smoothed_image = gaussian_smoothing(image_data)

    # Original Image
    print("ORIGINAL IMAGE") #Prints a heading "ORIGINAL IMAGE"
    print(image_data)  # and then prints the original image data ---the pixel values

    # Encoding
    encoded_image, huffman_tree = huffman_encoding(image_data) #encode the image by calling funct. huffman_encoding
    #It returns the encoded image and the Huffman tree---stored in encoded_image and huffman_tree
    print("\nENCODED IMAGE") #prints--ENCODED IMAGE heading
    print(encoded_image)
    #  print the encoded image
    #ldfcin

    # Compression Ratio
    #divide the original image size (in bytes) by the size of the encoded image
    original_size = image_data.nbytes
    encoded_size = len(encoded_image)
    compression_ratio = original_size / encoded_size #formula
    print("\nCOMPRESSION RATIO is : ", compression_ratio) #prints the heading compression ratio and its value

    # Decoding
    #decode the encoded image using huffman tree
    decoded_image = huffman_decode(encoded_image, huffman_tree, image_data.shape) #for decoding --call funct. huffman_decode
    print("\nDECODED IMAGE") #prints thedecoded image
    print(decoded_image)

    # PLOTTING OF ALL THE IMAGES---ORIGINAL , DECODED, DIFF
    plt.figure(figsize=(10, 4)) #plot ka size is 10x4 inches

        #plotting original image
    plt.subplot(1, 4, 1) #the first subplot(1 row,3 columns,1st position) 
    plt.imshow(image_data, cmap='gray') #original image shown in gray colourmap--as image is BLACK AND WHITE
    plt.title('ORIGINAL IMAGE')

        ##plotting smoothed image
    plt.subplot(1, 4, 2)
    plt.imshow(smoothed_image, cmap='gray')
    plt.title('SMOOTHED IMAGE')

        #plotting decode image
    plt.subplot(1, 4, 3)#the SECOND subplot(1 row,3 columns,2ND position) 
    plt.imshow(decoded_image, cmap='gray')#DECODED image shown in gray colourmap--as image is BLACK AND WHITE
    plt.title('DECODED IMAGE')

        #plotting the difference image
    plt.subplot(1, 4, 4)#the THIRD subplot(1 row,3 columns,3RD position) 
    plt.imshow(image_data - decoded_image, cmap='gray')#DIFFERENCE image shown in gray colourmap--as image is BLACK AND WHITE
    plt.title('DIFFERENCE')

    plt.show()#SHOWS THE ---PLOTS
