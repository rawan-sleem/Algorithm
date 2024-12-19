############################Heapify Algorithm => #############################
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree


##########################Build Max-Heap Algorithm=> #############################
def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

##########################Heap-Sort Algorithm=> ################################
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    build_max_heap(arr)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

##########################Part (c): Implementation of the Algorithms ################################
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def build_max_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    build_max_heap(arr)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap
        heapify(arr, i, 0)

# Example usage
if __name__ == "__main__":
    data = [3, 19, 1, 14, 8, 7]
    print("Original array:", data)
    heap_sort(data)
    print("Sorted array:", data)
##################################Part 2###############################################
################################Union-Find (Disjoint Set Union) Algorithm
# Find function with path compression
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

# Union function with rank
def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
#################################Kruskal’s Algorithm#######################
def kruskal(graph, num_vertices):
    # Sort edges by weight
    edges = sorted(graph, key=lambda edge: edge[2])  # edge = (u, v, weight)

    parent = list(range(num_vertices))  # Each vertex is its own parent initially
    rank = [0] * num_vertices  # Rank for union by rank

    mst = []  # To store the edges of the MST
    mst_weight = 0  # Total weight of the MST

    for u, v, weight in edges:
        # Check if u and v belong to different sets
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight
################################Part (c): Implementation of Kruskal’s Algorithm
# Union-Find Helper Functions
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# Kruskal's Algorithm
def kruskal(graph, num_vertices):
    # Sort edges by weight
    edges = sorted(graph, key=lambda edge: edge[2])  # edge = (u, v, weight)

    parent = list(range(num_vertices))  # Each vertex is its own parent initially
    rank = [0] * num_vertices  # Rank for union by rank

    mst = []  # To store the edges of the MST
    mst_weight = 0  # Total weight of the MST

    for u, v, weight in edges:
        # Check if u and v belong to different sets
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))
            mst_weight += weight

    return mst, mst_weight

# Example Usage
if __name__ == "__main__":
    # Graph: List of edges (u, v, weight)
    graph = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    num_vertices = 4

    mst, mst_weight = kruskal(graph, num_vertices)
    print("Edges in MST:", mst)
    print("Total weight of MST:", mst_weight)




