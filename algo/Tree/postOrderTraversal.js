const postorderTraversal = function (root, arr = []) {
  if (!root) {
    return arr;
  }
  postorderTraversal(root.left, arr);
  postorderTraversal(root.right, arr);
  arr.push(root.val);
  return arr;
};
