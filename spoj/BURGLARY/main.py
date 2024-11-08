
def subset_sum(arr, k):
    def recursion(arr, k, i):
        # Sum is zero means we have found a subset.
        if k == 0:
            return True
        
        # At the end of the arr if the sum > 0 then
        # this subset sum does not equal to sum.
        if i == len(arr):
            return False
        
        # In case the current arr element is greater than
        # the sum k only consider excluding the element.
        if arr[i] > k:
            return recursion(arr, k, i+1)
        # To generate all subsets we've to include and exclude
        # the element at each index.
        else:
            return recursion(arr, k-arr[i], i+1) or recursion(arr, k, i+1)
    
    return recursion(arr, k, 0)


def main():
    t = int(input())
    for case in range(1, t + 1):
        n, d = map(int, input().split())
        weights = list(map(int, input().split()))
        result = subset_sum(weights, d)
        print(f"Case #{case}: {result}")

if __name__ == "__main__":
    main()