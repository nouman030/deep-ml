import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
  means= []
  matrix = np.array(matrix)
  if mode == "row":
    means=matrix.mean(axis=1)
  elif mode == 'column':
    means=matrix.mean(axis=0)
  return means