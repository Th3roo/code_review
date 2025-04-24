/* Implementation of graph traversal to find cities reachable with exact transfers */
#include "GraphSolver.h"
#include <vector>
#include <queue>
#include <algorithm> // For std::sort
#include <iostream>  // For std::cerr (optional logging here)

// Allow using namespace std in .cpp files
using namespace std;

/**
 * @brief Finds cities reachable from a starting city with exactly L transfers,
 *        ensuring no shorter path exists.
 * @param graphData A structure containing the number of cities (n),
 *                  the adjacency matrix (adjMatrix), the 1-based starting
 *                  city index (startCityK), and the required number of
 *                  transfers (requiredTransfersL). Input validity is assumed
 *                  to be checked before calling this function.
 * @return std::vector<int> A vector containing the 1-based indices of the
 *         target cities, sorted in ascending order. Returns an empty vector
 *         if no such cities exist or if input parameters within graphData
 *         are logically inconsistent (e.g., K out of bounds), though primary
 *         validation should occur beforehand.
 * @throws Does not throw exceptions. Internal errors might log to std::cerr
 *         but aim to return an empty vector.
 */
vector<int> findCitiesWithExactTransfers(const GraphData& graphData) {
	int n = graphData.n;
	const vector<vector<int>>& adjMatrix = graphData.adjMatrix;
	int k = graphData.startCityK;
	int l = graphData.requiredTransfersL;

	// Basic internal sanity check (primary validation should be in main)
	if (k < 1 || k > n || l < 0 || n <= 0 || adjMatrix.empty()) {
		// cerr << "GraphSolver Error: Invalid input parameters received." << endl;
		return {}; // Return empty vector for invalid logical input
	}

	int startNode = k - 1; // Convert K to 0-based index for internal use

	// --- Breadth-First Search (BFS) Initialization ---
	// 'dist[i]' will store the minimum number of transfers from startNode to node i.
	// Initialize all distances to -1 (representing infinity/unreachable).
	vector<int> dist(n, -1);
	// Queue for BFS traversal
	queue<int> q;

	// Starting city requires 0 transfers to reach itself
	dist[startNode] = 0;
	q.push(startNode);

	// --- BFS Execution ---
	while (!q.empty()) {
		int u = q.front();
		q.pop();

		// Explore neighbors of city 'u'
		for (int v = 0; v < n; ++v) {
			// Check if there is a direct flight (edge) from u to v
			// and if city 'v' has not been visited yet (dist[v] == -1).
			// The dist[v] == -1 check ensures we find the shortest path,
			// as BFS explores layer by layer.
			if (adjMatrix[u][v] == 1 && dist[v] == -1) {
				// Found a shorter path to v (the first path found by BFS)
				dist[v] = dist[u] + 1; // Increment transfer count
				q.push(v);
			}
		}
	}

	// --- Result Collection ---
	vector<int> resultCities;
	resultCities.reserve(n); // Optimize allocation slightly

	// Iterate through all cities to find those matching the criteria
	for (int i = 0; i < n; ++i) {
		// Check if the shortest path to city 'i' has exactly 'L' transfers
		if (dist[i] == l) {
			// Add the 1-based city index to the results
			resultCities.push_back(i + 1);
		}
	}

	// --- Sorting ---
	// The problem requires the output cities to be in ascending order.
	// Although we iterate 0 to n-1, BFS discovery order doesn't guarantee
	// sorted indices in the result vector.
	sort(resultCities.begin(), resultCities.end());

	return resultCities;
}