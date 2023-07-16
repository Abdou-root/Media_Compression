import math
import heapq
import os


def kmeans_clustering(data, num_clusters):
    # Initialize cluster centers
    cluster_centers = initialize_cluster_centers(data, num_clusters)
    # Assign cluster IDs to data points
    cluster_ids = assign_cluster_ids(data, cluster_centers)
    while True:
        # Update cluster centers based on current assignments
        new_cluster_centers = update_cluster_centers(data, cluster_ids, num_clusters)
        # Reassign cluster IDs based on updated cluster centers
        new_cluster_ids = assign_cluster_ids(data, new_cluster_centers)
        # Check if cluster IDs remain unchanged
        if cluster_ids == new_cluster_ids:
            break
        cluster_ids = new_cluster_ids
        cluster_centers = new_cluster_centers
    return cluster_ids, cluster_centers


def initialize_cluster_centers(data, num_clusters):
    # Return the first num_clusters points as initial cluster centers
    return data[:num_clusters]


def assign_cluster_ids(data, cluster_centers):
    cluster_ids = []
    for point in data:
        # Calculate the distances from the point to each cluster center
        distances = [euclidean_distance(point, center) for center in cluster_centers]
        # Assign the cluster ID of the closest cluster center
        cluster_id = distances.index(min(distances))
        cluster_ids.append(cluster_id)
    return cluster_ids


def update_cluster_centers(data, cluster_ids, num_clusters):
    cluster_sums = [[0, 0] for _ in range(num_clusters)]
    cluster_counts = [0] * num_clusters
    for i, point in enumerate(data):
        cluster_id = cluster_ids[i]
        # Accumulate the sum of coordinates for each cluster
        cluster_sums[cluster_id][0] += point[0]
        cluster_sums[cluster_id][1] += point[1]
        # Count the number of points assigned to each cluster
        cluster_counts[cluster_id] += 1
    # Calculate the new cluster centers as the average of the assigned points
    cluster_centers = [[sums[0] / count, sums[1] / count] if count != 0 else [0, 0] for sums, count in
                       zip(cluster_sums, cluster_counts)]
    return cluster_centers


def euclidean_distance(point1, point2):
    # Calculate the Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Convert the lines of coordinates into a list of data points
        data = [[float(coord.strip()) for coord in line.strip().split(',')] for line in lines]
    return data


def calculate_frequency(cluster_id_list):
    frequency = {}
    for cluster_id in cluster_id_list:
        # Count the frequency of each cluster ID
        frequency[cluster_id] = frequency.get(cluster_id, 0) + 1
    return frequency


def build_huffman_tree(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # Return the root of the Huffman tree
    return heap[0]


def build_huffman_codes(huffman_tree):
    huffman_codes = {}
    for pair in huffman_tree[1:]:
        symbol, code = pair
        # Extract the symbol and its corresponding code from the Huffman tree
        huffman_codes[symbol] = code
    return huffman_codes


def encode_cluster_ids(cluster_id_list, huffman_codes):
    # Convert cluster IDs to their corresponding Huffman codes and concatenate them
    return ''.join(huffman_codes[cluster_id] for cluster_id in cluster_id_list)


# Get the file path from user input
file_path = input("Enter the file path: ").strip()

# Check if the file exists
if not os.path.isfile(file_path):
    raise FileNotFoundError("Invalid file path.")

# Read data points from the file
data = read_data_from_file(file_path)

num_clusters = 8
# Perform K-means clustering on the data
cluster_ids, cluster_centers = kmeans_clustering(data, num_clusters)

cluster_id_list = cluster_ids

# Calculate the frequency of each cluster ID
frequency = calculate_frequency(cluster_id_list)
# Build the Huffman tree based on the frequency of cluster IDs
huffman_tree = build_huffman_tree(frequency)
# Generate Huffman codes for each cluster ID
huffman_codes = build_huffman_codes(huffman_tree)
# Encode the cluster IDs using Huffman codes
encoded_bits = encode_cluster_ids(cluster_id_list, huffman_codes)

compressed_file_name = 'output_compressed.txt'
compressed_file_path = os.path.join(os.getcwd(), compressed_file_name)
with open(compressed_file_path, 'w') as file:
    # Write the encoded bits to the compressed file
    file.write(encoded_bits)

input_file_size = os.path.getsize(file_path)
compressed_file_size = os.path.getsize(compressed_file_path)

# Print the file sizes and compressed file path
print(f"Input file size: {input_file_size} bytes")
print(f"Compressed file size: {compressed_file_size} bytes")
print(f"Compressed file path: {compressed_file_path}")
