#include "Deque.h"
#include <vector>
#include <iterator> // std::begin, std::end

void FuncInsert(std::deque<int>& targetDeque) {
	size_t dequeSize = targetDeque.size();

	if (dequeSize < 5 || dequeSize % 2 == 0) {
		return;
	}

	size_t middleIndex = dequeSize / 2;

	auto middleStartIter = targetDeque.begin() + (middleIndex - 2);
	auto middleEndIter   = targetDeque.begin() + (middleIndex + 3); 

	targetDeque.insert(targetDeque.begin(), middleStartIter, middleEndIter);
}
