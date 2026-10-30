import numpy as np

def cosine_similarity(vec1, vec2):
  dot_product = vec1 @ vec2
  norm_product = np.linalg.norm(vec1) * np.linalg.norm(vec2)
  return dot_product / norm_product
	