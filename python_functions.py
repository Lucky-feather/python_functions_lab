def sum_to(n):
  total = 0
  count = 0
  while count <= n :
    if count == n :
      print(total)
      return total
      break
    else :
      #print(f'count: {count} / total: {total}')
      total = (total + count + 1)
      count += 1

sum_to(6)

#----------------------------

def largest(*args) :
  high_num = 0
  for arg in args:
    if high_num < arg :
      high_num = arg
  print(high_num)
  return high_num

#largest(1,3,45,7,9,0)

#-----------------------------

def occurences(str1, str2) :
  print(str1.count(str2))
  return str1.count(str2)

#occurences('abcd beeb', 'ee')

#---------------------------------