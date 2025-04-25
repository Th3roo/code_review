#ifndef GRAPH_SOLVER_H
#define GRAPH_SOLVER_H

#include <vector>
#include <string> // Although not directly used in signatures, often related

/**
 * @struct GraphData
 * @brief Holds the graph representation and query parameters.
 *        Used to pass data conveniently.
 */
struct GraphData {
	int n = 0;                         // Number of cities
	std::vector<std::vector<int>> adjMatrix; // Adjacency matrix (0 or 1)
	int startCityK = 0;                // Starting city (1-based)
	int requiredTransfersL = 0;        // Required number of transfers
};

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
std::vector<int> findCitiesWithExactTransfers(const GraphData& graphData);


#endif // GRAPH_SOLVER_H