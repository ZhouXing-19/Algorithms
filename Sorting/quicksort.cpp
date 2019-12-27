#include <iostream>
#include <string>
#include <iterator>

using namespace std;

int partition(int *A, int start, int end){
  int partitionIndex = start;
  int pivot = A[end];
  for(int i=start;i<end;i++){
    if(A[i]< pivot){
      swap(A[i],A[partitionIndex++]);
    }
  }
  swap(A[end],A[partitionIndex]);
  return partitionIndex;
}

void QuickSort(int *A, int start, int end){
  if(start<end && start>=0){
    int partitionindex = partition(A, start, end);
    QuickSort(A,start,partitionindex-1);
    QuickSort(A,partitionindex+1,end);
  }
}

int main(){
  int A[] = {2,1,9,0,4,7,2,3};
  QuickSort(A,0,7);
  for(int i=0;i<8;i++) cout<<A[i]<<" ";
  return 0;
}