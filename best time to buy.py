def bestTime(prices)->int:
  minPrice=float("inf")
  maxProfit=0

  for price in prices:
    if price < minPrice:
      minPrice=price
    if maxProfit < price-minPrice:
      maxProfit= price-minPrice
  return maxProfit
print(bestTime([7,1,5,3,6,4]))