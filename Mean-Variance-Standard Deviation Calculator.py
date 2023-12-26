import numpy as np

def calculate(list):
    # Check if list has 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert list to a 3x3 Numpy array
    matrix = np.array(list).reshape(3, 3)

    # Create the calculations dictionary
    calculations = {
        'mean': [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()],
        'variance': [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()],
        'max': [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()],
        'min': [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()],
        'sum': [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]
    }

    return calculations

# For testing, you can add this to your main.py and run it:
if __name__ == '__main__':
    print(calculate([0,1,2,3,4,5,6,7,8]))