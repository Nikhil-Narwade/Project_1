# minimum cost to hire k workers
def mincost_to_hire_workers(quality, wage, k):
    workers = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
    heap = []
    total_quality = 0
    min_cost = float('inf')
    
    for ratio, q in workers:
        heapq.heappush(heap, -q)
        total_quality += q
        
        if len(heap) > k:
            total_quality += heapq.heappop(heap)
        
        if len(heap) == k:
            min_cost = min(min_cost, total_quality * ratio)
    
    return min_cost

quality = [10,20,5]
wage = [70,50,30]
k = 2
print("min cost to hire workers:", mincost_to_hire_workers(quality, wage, k))


# candy distribution
def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    
    # left to right
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    # right to left
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    
    return sum(candies)

ratings = [1,0,2]
print("minimum candies:", candy(ratings))
