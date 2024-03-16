#include <iostream>
using namespace std;

int binarySearch(int list[], int size, int item) {
  //cout << list[4];
  int low = 0; 
  int high = size - 1;

  while (low <= high) {
    int mid = low + high;
    int guess = list[mid];
    if (guess == item) {
      return mid;
    }
      
    else if (guess > item) {
      high = mid - 1;
    }
      
    else {
      low = mid + 1;
    }
  }
  return -1;
  
}

int main() {
  int list[5] = {1,3,5,6,7};  // Entered list
  int len = sizeof(list)/sizeof(list[0]);  // Length of list
  int item = 2;  // Item intended to find
  cout << binarySearch(list, len, item);
}
