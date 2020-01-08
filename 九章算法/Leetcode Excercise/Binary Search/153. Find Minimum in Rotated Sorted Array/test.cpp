#include <iostream>
#include <string>

using namespace std;


int findMin(vector<int>& nums) {
   	int start = 0;
    int end = nums.length-1;
    return end;    
    }


int main(){
	vector<int> nums = {1,2,3,4};
	cout<<findMin(nums);
}
