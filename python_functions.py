def sum_to(n):
  total = 0
  count = 0
  while count <= n :
    if count == n :
      print(total)
      return total
    else :
      total = (total + count + 1)
      count += 1


#sum_to(6)

#----------------------------

def largest(*args) :
  high_num = 0
  for arg in args:
    if high_num < arg :
      high_num = arg
  print(high_num)
  return high_num

  ## ** alternate answer below

# def largest(*args) :
#   print(max(args))
#   return max(args)

#largest(1,3,45,7,98,0)

#-----------------------------

def occurences(str1, str2) :
  print(str1.count(str2))
  return str1.count(str2)

#occurences('banana candy', 'an')

#---------------------------------

def product(*args) :
  total = 1
  for arg in args:
    total = total * arg
  print(total)
  return total

product(4, 0.5, 5)