# RandomSeedCollision
Analysis on collision between random with different seeds.

**Language: Python**

**Start: 2023**

## Why
I came across a situation where a random function using two different [seeds](https://en.wikipedia.org/wiki/Random_seed) yields the same integer value. The situation can be described with two calls of the same random function (_R_):

$$ x = R(\text{seedx}, \text{size}) $$

$$ y = R(\text{seedy}, \text{size}) $$

where _size_ is the maximum value that _R_ can return. 

The collision (i.e., when _x_ is equal to _y_) is understandably possible especially if the _size_ is small. Anyway, I wrote this code to investigate a little this case. In particular, when _x_ and _y_ keep on having the same values even if the _size_ changes.

### A few observations
The following histogram shows the distribution of calling the random function with 10,000 different seeds:

![histogram 1](/images/histogram1.png)

The last bin is smaller simply because it contains a set of only 24 possible values (1001-1024) instead of the 200 of the other bins.

The following histogram shows the distribution of the random collision between the _seedx_ (equal to 1) and the 10,000 different seeds (_seedy_) over 100 random calls:

![histogram 2](/images/histogram2.png)

In total there are 10 _seedy_ that give the same random value as _seedx_ for the selected _size_ (1024). This was expected since:

$$ \frac{10000}{1024} \approx 10 $$

More surprising, there are two _seedy_ that have 30 or more random values in common with _seedx_. The 100 calls where performed by incrementing the _size_ of 512 each time.

For example, with _seedx_ equal to 1 and _seedy_ equal to 6401:

 n. test | size | x = y | x    | y    |
---------|------|-------|------|-------
 1       | 1024 | True  | 275  | 275
 2       | 1536 | True | 275 | 275
 3       | 2048 | True | 550 | 550
 4       | 2560 | True | 550 | 550
 5       | 3072 | True | 550 | 550
 6       | 3584 | True | 550 | 550
 7       | 4096 | True | 1100 | 1100
 8       | 4608 | True | 1100 | 1100
 9       | 5120 | True | 1100 | 1100
 10      | 5632 | True | 1100 | 1100
 11      | 6144 | True | 1100 | 1100
 12      | 6656 | True | 1100 | 1100
 13      | 7168 | True | 1100 | 1100
 14      | 7680 | True | 1100 | 1100
 15      | 8192 | True | 2201 | 2201
 16      | 8704 | True | 2201 | 2201
 17      | 9216 | True | 2201 | 2201
 18      | 9728 | True | 2201 | 2201
 19      | 10240 | True | 2201 | 2201
 20      | 10752 | True | 2201 | 2201
 21      | 11264 | True | 2201 | 2201
 22      | 11776 | True | 2201 | 2201
 23      | 12288 | True | 2201 | 2201
 24      | 12800 | True | 2201 | 2201
 25      | 13312 | True | 2201 | 2201
 26      | 13824 | True | 2201 | 2201
 27      | 14336 | True | 2201 | 2201
 28      | 14848 | True | 2201 | 2201
 29      | 15360 | True | 2201 | 2201
 30      | 15872 | True | 2201 | 2201
 31      | 16384 | False | 4402 | 4403
 32      | 16896 | False | 4402 | 4403
 33      | 17408 | False | 4402 | 4403
 34      | 17920 | False | 4402 | 4403
 35      | 18432 | False | 4402 | 4403
 36      | ..... | False | .... | ....
 
 This is clearly not compatible with a [truly random function](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) because, similar to rolling two dice, the probability of getting any specific number (_k_) from both seeds would be:

$$ P (x = y = k) = \frac{1}{\text{size}} \cdot \frac{1}{\text{size}} $$

 and the probability of getting two equal numbers for a specific size should be:

 $$ P (x = y) = \frac{\text{size}}{\text{size} \cdot \text{size}} = \frac{1}{\text{size}} $$

therefore in a truly random environment, the probability of getting the same number for the first 2 sizes is:

 $$ P = \frac{1}{1024} \cdot \frac{1}{1536} \approx 6 \cdot 10^{-7}  $$