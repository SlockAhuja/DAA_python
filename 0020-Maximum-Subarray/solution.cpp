class Solution {
public:
    int solve(vector<int>& nums, int low, int high) {
        if (low == high)
            return nums[low];

        int mid = low + (high - low) / 2;

        int left = solve(nums, low, mid);
        int right = solve(nums, mid + 1, high);

        int sum = 0;
        int leftSum = INT_MIN;

        for (int i = mid; i >= low; i--) {
            sum += nums[i];
            leftSum = max(leftSum, sum);
        }

        sum = 0;
        int rightSum = INT_MIN;

        for (int i = mid + 1; i <= high; i++) {
            sum += nums[i];
            rightSum = max(rightSum, sum);
        }

        int cross = leftSum + rightSum;

        return max({left, right, cross});
    }

    int maxSubArray(vector<int>& nums) {
        return solve(nums, 0, nums.size() - 1);
    }
};