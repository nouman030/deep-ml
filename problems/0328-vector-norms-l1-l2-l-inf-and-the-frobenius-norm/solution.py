import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    arr = np.asarray(arr)
    
    if norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("Frobenius norm requires a 2D matrix.")
        return float(np.linalg.norm(arr, ord="fro"))
    
    ord_val = 1 if norm_type == "l1" else (2 if norm_type == "l2" else np.inf if norm_type == "linf" else None)
    if ord_val is None:
        raise ValueError(f"Unknown norm type: {norm_type}")
        
    return float(np.linalg.norm(arr.ravel(), ord=ord_val))
