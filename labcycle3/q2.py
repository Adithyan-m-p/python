import numpy as np


def pca(matrix,row,column):
    mean_vector=np.mean(matrix,axis=0)
    
    mean_adjusted_matrix= matrix -  mean_vector
    
    covariance_matrix = np.dot(mean_adjusted_matrix.T, mean_adjusted_matrix) / (matrix.shape[0] - 1)
    
    eigen_value,eigen_vector = np.linalg.eig(covariance_matrix) 
   
    print(eigen_vector.shape)
    
    sort_indices = np.argsort(eigen_value)[::-1]
    sorted_eigen_value = eigen_value[sort_indices]
    sorted_eigen_vector = eigen_vector[:,sort_indices]
    



    
    basic_vector=mean_adjusted_matrix.dot(sorted_eigen_vector)

    linear_comb_basic_vector=(matrix-mean_adjusted_matrix).T.dot(basic_vector)
    
    return linear_comb_basic_vector




row=int(input("enter the row of the matrix : "))
column=int(input("enter the column of the matrix : "))
matrix=np.array([[float(input(f"enter the element of the matrix ({i+1} {j+1}) : "))
                  for j in range(column)]for i in range (row)])

pca_matrix=pca(matrix,row,column)

print(pca_matrix)





