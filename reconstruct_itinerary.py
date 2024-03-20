from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build the graph
        graph = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            graph[start].append(end)

        itinerary = []

        def dfs(airport):
            # Visit all the flights starting from the airport
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            itinerary.append(airport)

        # Start the dfs from 'JFK'
        dfs('JFK')
        
        # The itinerary is constructed in reverse, so we reverse it at the end
        return itinerary[::-1]
