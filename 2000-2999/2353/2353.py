from collections import defaultdict
import heapq

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            # Use (-rating, food) for max-heap and lex order
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food, newRating):
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        heap = self.cuisine_to_heap[cuisine]
        while True:
            rating, food = heap[0]
            if self.food_to_rating[food] == -rating:
                return food
            heapq.heappop(heap)