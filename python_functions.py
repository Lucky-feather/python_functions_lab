
def sum_to(n):
  total = 0
  count = 0
  while count <= n :
    if count == n :
      print(total)
      break
    else :
      #print(f'count: {count} / total: {total}')
      total = (total + count + 1)
      count += 1



sum_to(6)