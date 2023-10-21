//Binary search on a sorted vector to find the target element

int binarySearch(const std::vector<int>& array, int target) {
    int left = 0;
    int right = array.size() - 1;

    // Continue searching as long as the left index is less than or equal to the right index.
    while (left <= right) {
        // Calculate the middle index of the current search range.
        int mid = left + (right - left) / 2;

        // If the middle element is the target, return its index.
        if (array[mid] == target) {
            return mid;
        }
        // If the target is greater, narrow the search to the right half of the current range.
        else if (array[mid] < target) {
            left = mid + 1;
        }
        // If the target is smaller, narrow the search to the left half of the current range.
        else {
            right = mid - 1;
        }
    }

    // Target not found in the array, return -1.
    return -1;
}

/**
 * @brief Main function demonstrating the usage of the binarySearch function.
 */
int main() {
    std::vector<int> sortedArray = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    int target = 10;

    // Perform binary search on the sorted array.
    int result = binarySearch(sortedArray, target);

    // Output the result.
    if (result != -1) {
        std::cout << "Element found at index: " << result << std::endl;
    } else {
        std::cout << "Element not found in the array." << std::endl;
    }

    return 0;
}
