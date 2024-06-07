BLACK AND WHITE IMAGE COMPRESSION


Heap Queue (heapq):
		PRIORITY QUEUE IMPLEMENTATION/BUILDING OF HUFFMAN TREE

Default Dictionary(defaultdict):
		creates a dictionary with default values.
		Here we are storing pixel frequencies.If a pixel value hasn't been encountered yet,its frequency is set by default to zero.




#FUNCTION TO CALCULATE PIXEL FREQUENCIES count_pixel_occurencies():
	--counts the no. of times a unique pixel appears in image/the frequency of each pixel in image
	The input parameter image is a 2D array representing the image.
	The flatten() method -- converts this 2D array into a 1D list(flattened_image).
	This is done because the function needs to count the frequency of each pixel,and a 1D list simplifies the iteration through all pixels.


So,this function takes an image as input, flattens it to a 1D list,
and then counts the frequency of each unique pixel value using a defaultdict.
The output is a dictionary where keys are pixel values,
and values are their respective frequencies in the image.
This frequency information is crucial for building the Huffman tree,
where pixels with higher frequencies are assigned shorter Huffman codes for more efficient compression.


#huffman tree
HuffmanNode class to structure our tree nodes and then used this to build a Huffman tree based on the pixel frequencies.


#generate huffman code
generate_huffman_codes(node, code, encoding):
assigns codes (sequences of 0s and 1s) to each pixel in the Huffman tree.
"0" for the left child and "1" for the right child.

#huffman encoding
huffman_encoding(image):
builds the Huffman tree, generates the codes, and finally encodes the image using these codes.

#huffman decoding
huffman_decode function takes a Huffman-encoded image, the Huffman tree, and the original image's shape to decode the image.




SUMMARY

open an image file--> then convert and return it as a (black and white)numpy array-->flattens the 2D pixel array to a 1d array and then to a 1D list-->

counts pixel occurrences using pixel_counts (default dictionary)-->building a huffman tree based on the pixel frequencies-->

generating huffman code(generate_huffman_codes(node, code, encoding)_assigns codes (sequences of 0s and 1s) to each pixel in the Huffman tree, "0" for the left child and "1" for the right child.)--->

huffman encoding(encoding of the image using these codes)--->huffman decoding(decodes the image)--->PLOTTING


#plotting
Loading an image and displaying its pixel values.
Performing Huffman encoding and displaying the encoded image.
Calculating the compression ratio.
Decoding the encoded image and displaying the result.
Plotting the original image, decoded image, and the difference between them.

Smoothing refers to process of reducing noise or variations in pixel intensity of an image.One way to do it is application of a gaussian filter.this filter blurs the image by convolving it with a gaussian funtion. reducing the hight frequency components.
here we noticed that huffman coding becomes more efficient when we encode smooth images.
by smotthing we can make huffman code more compact.we also noticed that smoothning increses
the effectiveness of huffman coding.smoothning helps when we want a high compression ratio that is when we want reduce the size of encoded data compared to original data in case of image.





