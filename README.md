# Floating Point Compression with Lossy and Lossless Compression

This is a Python script that demonstrates the compression of floating point data using a combination of lossy and lossless compression techniques. The script performs K-means clustering on the input data points, assigns cluster IDs to each point, and then applies Huffman encoding to compress the cluster IDs.

## Prerequisites

- Python 3.x
- Libraries: numpy, os

## Usage

1. Ensure that you have Python 3.x installed on your system.
2. Install the required libraries by running the following command:
  

   pip install numpy
   
3. Save the script to a Python file (e.g., compression_script.py).
4. Prepare your input data by storing the floating point values in a text file (e.g., input_data.txt).
5. Open the Python script and replace 'file_path' in read_data_from_file(file_path) with the path to your input data file (e.g., 'input_data.txt').
6. Adjust the num_clusters variable to specify the desired number of clusters for K-means clustering.
7. Run the script using the following command:
  

   python compression_script.py
   
8. The compressed output will be saved in a file named 'output_compressed.txt' in the current working directory.
9. The script will print the sizes of the input and compressed files, as well as the path to the compressed file.

## Script Overview

1. Read the floating point data points from the input file.
2. Perform K-means clustering on the data to assign cluster IDs to each point.
3. Calculate the frequency of each cluster ID.
4. Build a Huffman tree based on the frequency of cluster IDs.
5. Generate Huffman codes for each cluster ID.
6. Encode the cluster IDs using the Huffman codes.
7. Write the encoded bits to a compressed file.
8. Print the sizes of the input and compressed files, as well as the path to the compressed file.

## Note

- This script assumes that the input data points are stored in a text file, with one floating point value per line.
- The compression process is lossless for the cluster IDs but may result in lossy compression for the original floating point values.
