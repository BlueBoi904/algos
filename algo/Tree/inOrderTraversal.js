const inorderTraversal = function (root, arr = []) {
  if (!root) {
    return arr;
  }
  inorderTraversal(root.left, arr); // Return arr = []
  arr.push(root.val);
  inorderTraversal(root.right, arr);
  return arr;
};
