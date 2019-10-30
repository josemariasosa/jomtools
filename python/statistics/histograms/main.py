score = [
209.2102175,
162.5415056,
160.5814496,
141.9988506,
141.1629691,
139.5146599,
139.4427927,
139.4084934,
138.1071475,
135.6998619,
135.6835578,
133.5420214,
132.2225531,
120.4220295,
117.8827097,
117.5229813,
117.5044603,
117.4881561,
117.4881561,
117.4881561,
116.2019372,
115.8580717,
115.83763,
115.8213259,
115.8213259,
115.362102,
115.2922665,
115.2737455,
115.2737455,
114.5884532,
113.627357,
113.6254363,
113.6254363,
113.608836,
113.6069153,
113.6069153,
113.6069153,
113.6069153,
113.6069153,
113.6069153,
113.6069153,
113.6069153,
113.6069153,
113.5698732,
113.2013826,
112.9249507,
112.9249507,
112.92303,
112.92303,
112.92303,
112.3596592,
112.3596592,
112.3577385,
112.3206964,
111.6901573,
111.6254571,
111.2561997,
110.7086194,
110.0233271,
110.0233271,
109.4110465,
107.794533,
94.96676347,
93.36395638,
92.5989915,
92.58047046,
92.54342839,
90.94846539,
90.93216125,
90.93216125,
90.93186505,
90.91364022,
90.9077983,
90.89290229,
90.36605986,
88.7348071,
88.71967134,
88.71967134,
88.71775065,
88.71775065,
88.71775065,
88.69922961,
86.36481823,
86.34851409,
84.13410349,
84.13410349
]

import matplotlib.pyplot as pl
import numpy as np

a = np.array(score)

fig = pl.hist(a,normed=0)
pl.title('Mean')
pl.xlabel("value")
pl.ylabel("Frequency")
pl.savefig("abc.png")