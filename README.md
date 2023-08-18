# RandomSeedCollision
Analysis on collision between random with different seeds.

**Language: Python**

**Start: 2023**

## Why
I came across a situation where a random function using two different [seeds](https://en.wikipedia.org/wiki/Random_seed) yields the same integer value. The situation can be described with two calls of the same random function (_R_):

$$ x = R(\text{seedx}, \text{size}) $$
$$ y = R(\text{seedy}, \text{size}) $$

where _size_ is the maximum value that _R_ can return. 

The collision (i.e., when _x_ is equal to _y_) is understandably possible especially if _size_ is small. Anyway, I wrote this code to investigate a little this case. In particular, when _x_ and _y_ keep on having the same value even if the _size_ is changed.

### A few observations
The following histogram show the distribution of calling the random function with 10,000 different seeds:

![histogram 1](/images/histogram1.png)

The last bin is smaller simply because it contains a set of only 24 possible values (1001-1024) instead of the 200 of the other bins.

The following histogram show the distribution of the random collision between the _seedx_ (equal to 1) and the 10,000 different seeds (_seedy_) over 100 random calls:

![histogram 2](/images/histogram2.png)

In total there are 10 _seedy_ that give the same random value as _seedx_ for the selected _size_ (1024). This was expected since:

$$ \frac{10000}{1024} \approx 10 $$

More surprising, there are two _seedy_ that have 30 or more random values in common with _seedx_. The 100 calls where performed by incrementing the _size_ of 512 each time.

For example _seedx_ equal to 1 and _seedy_ equal to 6401:

 size | equal | x | y |
------|-------|---|----
 1024 | True | 275 | 275
 1536 | True | 275 | 275
 2048 | True | 550 | 550
 2560 | True | 550 | 550
 3072 | True | 550 | 550
 3584 | True | 550 | 550
 4096 | True | 1100 | 1100
 4608 | True | 1100 | 1100
 5120 | True | 1100 | 1100
 5632 | True | 1100 | 1100
 6144 | True | 1100 | 1100
 6656 | True | 1100 | 1100
 7168 | True | 1100 | 1100
 7680 | True | 1100 | 1100
 8192 | True | 2201 | 2201
 8704 | True | 2201 | 2201
 9216 | True | 2201 | 2201
 9728 | True | 2201 | 2201
 10240 | True | 2201 | 2201
 10752 | True | 2201 | 2201
 11264 | True | 2201 | 2201
 11776 | True | 2201 | 2201
 12288 | True | 2201 | 2201
 12800 | True | 2201 | 2201
 13312 | True | 2201 | 2201
 13824 | True | 2201 | 2201
 14336 | True | 2201 | 2201
 14848 | True | 2201 | 2201
 15360 | True | 2201 | 2201
 15872 | True | 2201 | 2201
 16384 | False | 4402 | 4403
 16896 | False | 4402 | 4403
 17408 | False | 4402 | 4403
 17920 | False | 4402 | 4403
 18432 | False | 4402 | 4403
 18944 | False | 4402 | 4403
 19456 | False | 4402 | 4403
 19968 | False | 4402 | 4403
 20480 | False | 4402 | 4403
 20992 | False | 4402 | 4403
 21504 | False | 4402 | 4403
 22016 | False | 4402 | 4403
 22528 | False | 4402 | 4403
 23040 | False | 4402 | 4403
 23552 | False | 4402 | 4403
 24064 | False | 4402 | 4403
 24576 | False | 4402 | 4403
 25088 | False | 4402 | 4403
 25600 | False | 4402 | 4403
 26112 | False | 4402 | 4403
 26624 | False | 4402 | 4403
 27136 | False | 4402 | 4403
 27648 | False | 4402 | 4403
 28160 | False | 4402 | 4403
 28672 | False | 4402 | 4403
 29184 | False | 4402 | 4403
 29696 | False | 4402 | 4403
 30208 | False | 4402 | 4403
 30720 | False | 4402 | 4403
 31232 | False | 4402 | 4403
 31744 | False | 4402 | 4403
 32256 | False | 4402 | 4403
 32768 | False | 8805 | 8806
 33280 | False | 8805 | 8806
 33792 | False | 8805 | 8806
 34304 | False | 8805 | 8806
 34816 | False | 8805 | 8806
 35328 | False | 8805 | 8806
 35840 | False | 8805 | 8806
 36352 | False | 8805 | 8806
 36864 | False | 8805 | 8806
 37376 | False | 8805 | 8806
 37888 | False | 8805 | 8806
 38400 | False | 8805 | 8806
 38912 | False | 8805 | 8806
 39424 | False | 8805 | 8806
 39936 | False | 8805 | 8806
 40448 | False | 8805 | 8806
 40960 | False | 8805 | 8806
 41472 | False | 8805 | 8806
 41984 | False | 8805 | 8806
 42496 | False | 8805 | 8806
 43008 | False | 8805 | 8806
 43520 | False | 8805 | 8806
 44032 | False | 8805 | 8806
 44544 | False | 8805 | 8806
 45056 | False | 8805 | 8806
 45568 | False | 8805 | 8806
 46080 | False | 8805 | 8806
 46592 | False | 8805 | 8806
 47104 | False | 8805 | 8806
 47616 | False | 8805 | 8806
 48128 | False | 8805 | 8806
 48640 | False | 8805 | 8806
 49152 | False | 8805 | 8806
 49664 | False | 8805 | 8806
 50176 | False | 8805 | 8806
 50688 | False | 8805 | 8806
 51200 | False | 8805 | 8806
 51712 | False | 8805 | 8806
