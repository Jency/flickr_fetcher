
import sys
import argparse
import re
import os

from numpy import array, zeros, mean, std, sort, add, subtract, divide, dot, sqrt
from numpy import linalg as la
from scipy.cluster.vq import vq, kmeans, whiten

import vlad

parser = argparse.ArgumentParser(description = 'K-means clustering util for image feature processing.')
parser.add_argument('-d', help = 'The directory of vlad feature files.')
parser.add_argument('-q', help = 'The filename of query photo id list.')
parser.add_argument('-g', help = 'The filename of groundtruth photo id list.')
parser.add_argument('-o', help = 'The output file.')
 
args = parser.parse_args()


photos = vlad.list_files(args.d)
query = vlad.load_list(args.q)

groundtruth = []
if args.g != None:
    groundtruth = vlad.load_list(args.g)
else:
    groundtruth = query

dist = vlad.do_query(photos, query)
(ap, map_value) = vlad.validate(dist, query, groundtruth)

print("AP: ")
print(ap)
print("MAP: ")
print(map_value)

