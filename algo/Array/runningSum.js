const runningSum = function (nums) {
  let sum = 0;
  const result = [];
  for (let i = 0; i < nums.length; i++) {
    result.push(sum + nums[i]);
    sum += nums[i];
  }
  return result;
};
