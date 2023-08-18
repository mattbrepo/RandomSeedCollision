# %%
import random
from tqdm import tqdm
import plotly.express as px

#
# Get the first value of a newline initilized random function
def get_first_rnd(seed, size):
  random.seed(seed)
  return random.randint(0, size)

#
# Test a pair of seeds
def test_seed_pair(seedx, seedy, init_size, max_test, print_val):
  count_eq = 0
  size = init_size
  for i in range(0, max_test):
    x = get_first_rnd(seedx, size)
    y = get_first_rnd(seedy, size)
    if x == y:
      count_eq = count_eq + 1    
    if print_val:
      print(str(size) + ': ' + str(x == y) + ' - ' + str(x) + ' - ' + str(y))
      
    size = size + 512

  return count_eq

#
# Get seedy staring from seedx and an index
def get_seedy(seedx, i):
  return seedx + 1 + i

#
# MAIN
#

sizex = 1024
seedx = 1
max_test = 10000
max_test_1 = 100

# --- 10 bin histogram of random integer value
# %%
rnd_vals = []
for i in tqdm(range(0, max_test), desc="Loading..."):
  seedy = get_seedy(seedx, i)
  rnd_vals.append(get_first_rnd(seedy, sizex))
px.histogram(rnd_vals, nbins=10, title='10 bin histogram of random integer value (size=' + str(sizex) + ')')

# --- 10 bin histogram of collisions
# %%
x = get_first_rnd(seedx, sizex)
collisions = []
for i in tqdm(range(0, max_test), desc="Loading..."):
  seedy = get_seedy(seedx, i)
  y = get_first_rnd(seedy, sizex)
  if x == y:
    count_eq = test_seed_pair(seedx, seedy, sizex, max_test_1, False)
    collisions.append((seedy, count_eq))

print('')
print('max_test: ' + str(max_test))
print('count collisions: ' + str(len(collisions)))

col_vals = list(map(lambda t: t[1], collisions))
px.histogram(col_vals, nbins=10, title='10 bin histogram of collisions over ' + str(max_test_1) + ' random calls')

# --- table of two seeds having 30 or more collisions with different sizes
# %%
collisions_30 = list(filter(lambda t: t[1] >= 30, collisions))
print('count at least 30 collisions: ' + str(len(collisions_30)))
print('seeds: ' + ', '.join(map(str, collisions_30)))
test_seed_pair(seedx, collisions_30[0][0], sizex, max_test_1, True)
