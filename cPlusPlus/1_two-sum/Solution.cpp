#nclude<iostream>
#include<vector>
using namespace std;

class Solution{
	public:
		vector<int> twoSum(vector<int& nums, int target){
			int length = nums.size();
			vector<int> result;
			if(length < 2){
				return;
			}
			else{
				for(auto firstPointer = 0; firstPointer <= length; firstPointer++){
					for(auto secondPointer = firstPointer + 1; secondPointer <= length; secondPointer++){
						if(nums.at(firstPointer) + nums.at(secondPointer) == target){
							result.push_back(firstPointer);
							result.push_back(secondPointer);
							return result;
						}
					}
				}
			}
			return;
		}
};

int main(){
	return 0;
}
