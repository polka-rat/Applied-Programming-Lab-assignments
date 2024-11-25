import unittest
import numpy as np
from matmul import matrix_multiply

class TestMatrixMultiplication(unittest.TestCase):
    def test_valid_multiplication(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_different_dimensions(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[1, 2], [3, 4], [5, 6]]
        expected_result = [[22, 28], [49, 64]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_1x1_matrices(self):
        matrix1 = [[5]]
        matrix2 = [[10]]
        expected_result = [[50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_incompatible_dimensions(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_empty_matrix(self):
        matrix1 = []
        matrix2 = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_non_numeric_elements(self):
        matrix1 = [[1, "a"], [3, 4]]
        matrix2 = [[1, 2], [3, 4]]
        with self.assertRaises(TypeError):
            matrix_multiply(matrix1, matrix2)

    def test_float_values(self):
        matrix1 = [[1.5, 2.5], [3.5, 4.5]]
        matrix2 = [[5.5, 6.5], [7.5, 8.5]]
        expected_result = [[27.0, 31.0], [53.0, 61.0]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_negative_values(self):
        matrix1 = [[-1, -2], [-3, -4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = [[-19, -22], [-43, -50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_zero_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[0, 0], [0, 0]]
        expected_result = [[0, 0], [0, 0]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_empty_matrix(self):    
        matrix1 = [[], []]
        matrix2 = [[1, 0], [0, 1]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_large_matrices(self):
        matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        expected_result = [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_identity_matrix(self):
        matrix1 = [[1, 2], [3, 4]]
        identity_matrix = [[1, 0], [0, 1]]
        expected_result = [[1, 2], [3, 4]]
        self.assertEqual(matrix_multiply(matrix1, identity_matrix), expected_result)

    def test_stress_test(self):
        size = 1000
        matrix = []
        for i in range(size):
            matrix.append([1] * size)  # Simplified matrix creation

    #     # Convert to NumPy array
    #     matrix_np = np.array(matrix)
        
    #     # Perform matrix multiplication using NumPy
    #     ans_matrix = np.matmul(matrix_np, matrix_np)
        
    #     # Compare the result with your own matrix_multiply function
    #     self.assertEqual(matrix_multiply(matrix, matrix), ans_matrix.tolist())


if __name__ == "__main__":
    unittest.main()
