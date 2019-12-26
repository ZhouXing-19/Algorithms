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
  
  private void mergeSort(int[] A, int start, int end, int[] temp)
  
}
```

