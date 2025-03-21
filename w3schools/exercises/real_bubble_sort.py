"""Real Life use cases of Bubble Sort"""
def leaderboard_ranking_bubble(array):
    """LeaderBoard Ranking using Bubble Sort bubbling small values to right"""
    size = len(array)
    for i in range(size-1):
        for j in range(size-i-1):
            if array[j][1] < array[j+1][1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array

scores = [("Alice", 450), ("Bob", 300), ("Timothy", 300), ("Rebecca", 300), ("Charlie", 600)]
print("Exercise 1")
print("===============")
print(leaderboard_ranking_bubble(scores))
print("")

def sort_prices(array,order):
    """Imagine an Ecommerce site that needs to sort prices in Cheapest to Expensive and Vice versa"""
    size = len(array)
    for i in range(size-1):
        swapped = False
        for j in range(size-1, i, -1):
            if (order == 'ascending' and array[j] < array[j-1]) or (order == 'descending' and array[j] > array[j-1]):
                array[j], array[j-1] =   array[j-1], array[j]
                swapped = True
        if not swapped:
            break
    return array
prices = [1999, 499, 799, 1299, 899]
print("Exercise 2")
print("===============")
print("Cheapest: ",sort_prices(prices,"ascending"))
print("Most Expensive: ",sort_prices(prices,"descending"))
print("")