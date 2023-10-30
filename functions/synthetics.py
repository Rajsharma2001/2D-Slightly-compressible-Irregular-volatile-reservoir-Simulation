"""
Codes to create synthetic data

@author: Yohanes Nuwara
@email: ign.nuwara97@gmail.com
"""

def synthetic_halves_boundary(xi, yi):
  """
  Create a synthetic irregular boundary condition
  as halves of each side as different boundary condition (B.C.)

  e.g. 2D regular reservoir has 100x50 dimension
  in the north and south are divided into 25 and 25 grids with 2 different B.Cs
  in the west and east are divided into 50 and 50 grids with 2 different B.Cs

  Input: 

  xi, yi = reservoir dimension (NOTE: xi, yi should be divisible by 2)

  Output:

  w_b1, w_b2 = each halves of the west boundary coordinates
  e_b1, e_b2 = each halves of the east boundary coordinates
  s_b1, s_b2 = each halves of the south boundary coordinates
  n_b1, n_b2 = each halves of the north boundary coordinates      
  """
  import numpy as np
  
  w_b1 = []; e_b1 = []
  for i in range(1,np.int((0.5*yi)+1)):
    arr1 = [1,i]
    arr2 = [xi,i]
    w_b1.append(arr1)
    e_b1.append(arr2) 

  s_b1 = []; n_b1 = []
  for i in range(1,np.int((0.5*xi)+1)):
    arr1 = [i,1]
    arr2 = [i,xi]
    s_b1.append(arr1)
    n_b1.append(arr2) 

  w_b2 = []; e_b2 = []
  for i in range(np.int((0.5*yi)+1),yi+1):
    arr1 = [1,i]
    arr2 = [xi,i] 
    w_b2.append(arr1)
    e_b2.append(arr2)

  s_b2 = []; n_b2 = []
  for i in range(np.int((0.5*xi)+1),xi+1):
    arr1 = [i,1]
    arr2 = [i,xi]
    s_b2.append(arr1)
    n_b2.append(arr2) 
  
  return w_b1, w_b2, e_b1, e_b2, s_b1, s_b2, n_b1, n_b2

def synthetic_initial_pressure2d(xi, yi, function='equilibrize', p_ref=4000):
  """
  Create synthetic initial pressure data for Slightly Compressible simulation
  """
  import numpy as np
  p_initial = np.zeros((xi,yi))

  if function=='equilibrize':
    for i in range(xi):
      for j in range(yi):
        p_initial[i,j] = p_ref

    return p_initial 

def constant_depth1d(z, xi):
  """
  Create constant depth of 1D reservoir

  Input:
  z = depth of grid blocks (float)
  xi = number of grid blocks in x-direction

  Output:
  z_array = grid block coordinates + depth of grid blocks (2D array)
  """
  import numpy as np
  x = np.arange(1, xi+1)
  z = np.full(xi, z)
  z_array = np.array([x, z])
  return z_array  

def create_depth2d(reservoir_input, model='horizontal', z=3000):
  """
  Create constant depth of 2D reservoir

  Input:
  model = option of models: 'horizontal', 'dipping_to_north', 'anticline'
  reservoir_input = reservoir data dictionary
  z = depth of grid blocks (only for model 'horizontal')

  Output:
  z_array = depth of grid blocks (2D array)
  """
  import numpy as np

  xi = reservoir_input['xi']
  yi = reservoir_input['yi']
  x, y = np.meshgrid(np.arange(1, xi+1), np.arange(1, yi+1), indexing='ij')  

  if model=='horizontal':
    z_array = np.array([[z]*yi]*xi)
  
  if model=='dipping_to_north':
    z_array = 0.5 * (100 * y + 1000) 

  if model=='anticline':
    z_array = ((x**2)-(y**2)) + 3001 # anticlinal reservoir    

  return z_array 
