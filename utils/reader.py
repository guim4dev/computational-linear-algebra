import numpy as np

def getMatrixA(file_path):
  matrixA = []
  with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
      new_line = line.split(' ')
      new_line = [int(x) for x in new_line]
      matrixA.append(new_line)

  return np.matrix(matrixA)

def getVectorB(file_path):
  vectorB = []
  with open(file_path, 'r') as file:
    lines = file.readlines()
    vectorB = [int(x) for x in lines]

  return np.array(vectorB)