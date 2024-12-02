import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List should contain nine numbers.")
    new_array = np.array(input_list).reshape(3, 3)
    print(new_array)
    
    calculations = {
        "mean": [
            new_array.mean(axis=0).tolist(), 
            new_array.mean(axis=1).tolist(), 
            new_array.mean().tolist()],
        "variance": [
            new_array.var(axis=0).tolist(), 
            new_array.var(axis=1).tolist(), 
            new_array.var().tolist()],
        "standard deviation": [
            new_array.std(axis=0).tolist(), 
            new_array.std(axis=1).tolist(), 
            new_array.std().tolist()],
        "max": [
            new_array.max(axis=0).tolist(), 
            new_array.max(axis=1).tolist(), 
            new_array.max().tolist()],
        "min": [
            new_array.min(axis=0).tolist(), 
            new_array.min(axis=1).tolist(), 
            new_array.min().tolist()],
        "sum": [
            new_array.sum(axis=0).tolist(), 
            new_array.sum(axis=1).tolist(), 
            new_array.sum().tolist()]
    }
    print(calculations)

calculate([1,2,3,4,5,6,7,8,9])