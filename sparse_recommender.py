class SparseMatrix:
    def __init__(self):
        self.movieRecommendDict = {}        # Constructor defining a dictionary for storing non-zero elements.

    def set(self, row, col, value):         # Method to set the value at (row, col).
        if row < 0 or col < 0 or value < 0:
            raise ValueError("Row and column indices must be positive.")
        elif value != 0:  # condition to check non zero value
            self.movieRecommendDict[(row, col)] = value
        elif (row, col) in self.movieRecommendDict:
            del self.movieRecommendDict[(row, col)]  # Remove zero values to keep the matrix sparse.

    def get(self, row, col):             # Returns the value at (row, col).
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be positive.")
        else:
            return self.movieRecommendDict.get((row, col), 0)

    def recommend(self, vector):        # Method to multiply sparse matrix with given vector,returns recommendations.
        if len(vector) != len(self.movieRecommendDict):
            raise ValueError("Vector length should be same as number of columns of the movieRecommendDict.")
        recommendations = []        # Empty list for recommendations
        for i in range(len(vector)):                # Loop through each movie (i) in the range of the vector length
            recommendation = 0
            for j in range(len(vector)):
                recommendation += self.get(i, j) * vector[j]
            recommendations.append(recommendation)
        return recommendations

    def add_movie(self, matrix):            # Method to add new sparseMatrix and returns the result.
        result = SparseMatrix()
        for (row, col), value in self.movieRecommendDict.items():
            result.set(row, col, value)
        for (row, col), value in matrix.movieRecommendDict.items():
            result.set(row, col, value)
        return result
