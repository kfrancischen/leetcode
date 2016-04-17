#include<iostream>
#include<map>
#include<vector>
using namespace std;

typedef map<int, int> HashTable;
typedef HashTable::iterator Iterator;

class Solution{
	public:
		vector<int> twoSum(vector<int>& nums, int target){
			int length = nums.size();
			vector<int> result;
			HashTable hashTable;
			for(size_t i = 0; i < length; i++){
				hashTable.insert(HashTable::value_type(nums.at(i), i));
			}
			for(size_t i = 0; i < length; i++){
				int firstPointer = nums.at(i);
				Iterator iter = hashTable.find(target - firstPointer);
				if(iter != hashTable.end() && iter->second != i){
					result.push_back(i);
					result.push_back(iter->second);
					return result;
				}
			}
			return result;
		}
};

int main(){
	Solution* mytest = new Solution();

	vector<int> test_1;
	test_1.push_back(3);
	test_1.push_back(2);
	test_1.push_back(4);

	vector<int> result_1 = mytest->twoSum(test_1, 6);
	if(result_1.size() == 2){
		cout << result_1.at(0) << "," << result_1.at(1) << endl;
	}
	return 0;
}
