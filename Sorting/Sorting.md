## Merge Sort

```c++
public class Solution{
  public void sortInteger(int [] A){
    if (A == null || A.length == 0){
      return;
    }
    int [] temp = new int [A.length]; //开辟新数组
    mergeSort(A,0,A.length - 1, temp); //新数组作为参数传递进排序函数
  }
  
  //分治，切分到只有一个数的情况。
  private void mergeSort(int[] A, int start, int end, int[] temp){
    if(start >= end){
      return;
    }
    mergeSort(A, start, (start+end)/2, temp);
    mergeSort(A, (start+end)/2, end, temp);
    merge(A,start,end,temp);
  }
  
  private void merge(int[] A, int start, int end, int[] temp){
    int mid = (start+end)/2
    int leftindex = start;
    int rightindex = mid+1;
    int index = start;
    
    while (leftindex <= mid && rightindex<=end){
      if(A[leftindex]<A[rightindex]){
        temp[index++] = A[leftindex++];
      }else{
        temp[index++] = A[rightindex++];
      }
    }
    
    //解决尾部。下面两个while只有一个会运行。
    while(leftindex<=mid){
      temp[index++] = A[leftindex++];
    }
    while(rightindex<=end){
      temp[index++] = A[rightindex++];
    }
  }
  
  //把temp数组的复制到A数组
  for(int i =start; i<= end; i++){
    A[i] = temp[i];
  }
  
  
}
```



![Merge Sorting](/Users/zhou/Desktop/Travail/Algorithms/Sorting/mergesort.jpeg)

