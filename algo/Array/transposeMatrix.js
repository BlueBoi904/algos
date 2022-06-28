const transpose = function (matrix) {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix.length; j++) {
      matrix[i][j] = matrix[j][i];
      matrix[j][i] = matrix[i][j];
    }
  }
  console.log(matrix);
};

transpose([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]);
