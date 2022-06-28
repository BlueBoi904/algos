const isSameTree = function (p, q) {
  const tree1 = preorderTraversal(p);
  const tree2 = preorderTraversal(q);
  if (tree1.length !== tree2.length) {
    return false;
  }

  for (let i = 0; i < tree1.length; i++) {
    if (tree1[i] !== tree2[i]) {
      return false;
    }
  }

  return true;
};

const preorderTraversal = function (root, arr = []) {
  if (root === null) {
    arr.push(null);
    return arr;
  }
  // Visit root
  arr.push(root.val);
  // Traverse left

  preorderTraversal(root.left, arr);
  preorderTraversal(root.right, arr);

  return arr;
};

const isSameTree2 = function (p, q) {
  if (!q && !p) {
    return true;
  }
  if (!q || !p) {
    return false;
  }
  if (q.val !== p.val) {
    return false;
  }

  return isSameTree2(p.left, q.left) && isSameTree2(p.right, q.right);
};
