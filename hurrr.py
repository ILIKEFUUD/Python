
import re
if not re.match(r'^([a-z0-9\:])+$', password):
	exit(-1)
appa = [[ord(c) for c in x] for x in password.split(":")]
if int(appa[0][9] - appa[0][14]) != -1 :
	exit(-1)
if int(appa[0][8] - appa[0][15]) != 48 :
	exit(-1)
if int(appa[0][5] * appa[0][8]) != 9999 :
	exit(-1)
if int(appa[0][1] + appa[0][4]) != 199 :
	exit(-1)
if int(appa[0][7] ^ appa[0][7]) != 0 :
	exit(-1)
if int(appa[0][3] / appa[0][6]) != 0 :
	exit(-1)
if int(appa[0][5] * appa[0][13]) != 9797 :
	exit(-1)
if int(appa[0][0] - appa[0][9]) != 3 :
	exit(-1)
if int(appa[0][9] * appa[0][7]) != 9894 :
	exit(-1)
if int(appa[0][1] * appa[0][14]) != 9898 :
	exit(-1)
if int(appa[1][1] % appa[1][10]) != 105 :
	exit(-1)
if int(appa[1][13] / appa[1][3]) != 0 :
	exit(-1)
if int(appa[1][12] - appa[1][8]) != -1 :
	exit(-1)
if int(appa[1][12] + appa[1][6]) != 222 :
	exit(-1)
if int(appa[1][12] - appa[1][14]) != -18 :
	exit(-1)
if int(appa[1][10] ^ appa[1][0]) != 1 :
	exit(-1)
if int(appa[1][8] * appa[1][3]) != 11322 :
	exit(-1)
if int(appa[1][8] * appa[1][9]) != 11322 :
	exit(-1)
if int(appa[1][12] - appa[1][8]) != -1 :
	exit(-1)
if int(appa[1][13] * appa[1][6]) != 12584 :
	exit(-1)
if int(appa[0][5] / appa[0][4]) != 1 :
	exit(-1)
if int(appa[0][13] - appa[0][1]) != -4 :
	exit(-1)
if int(appa[0][0] ^ appa[0][13]) != 5 :
	exit(-1)
if int(appa[0][3] * appa[0][3]) != 10000 :
	exit(-1)
if int(appa[0][2] * appa[0][9]) != 9409 :
	exit(-1)
if int(appa[0][3] / appa[0][2]) != 1 :
	exit(-1)
if int(appa[0][10] % appa[0][15]) != 0 :
	exit(-1)
if int(appa[0][7] * appa[0][11]) != 10302 :
	exit(-1)
if int(appa[0][1] / appa[0][4]) != 1 :
	exit(-1)
if int(appa[0][15] % appa[0][15]) != 0 :
	exit(-1)
if int(appa[0][12] ^ appa[0][4]) != 0 :
	exit(-1)
if int(appa[0][0] + appa[0][9]) != 197 :
	exit(-1)
if int(appa[0][7] * appa[0][11]) != 10302 :
	exit(-1)
if int(appa[0][0] * appa[0][1]) != 10100 :
	exit(-1)
if int(appa[0][4] % appa[0][11]) != 98 :
	exit(-1)
if int(appa[0][9] % appa[0][4]) != 97 :
	exit(-1)
if int(appa[0][9] ^ appa[0][7]) != 7 :
	exit(-1)
if int(appa[0][1] % appa[0][4]) != 3 :
	exit(-1)
if int(appa[0][0] / appa[0][8]) != 1 :
	exit(-1)
if int(appa[0][14] / appa[0][14]) != 1 :
	exit(-1)
if int(appa[0][7] / appa[1][12]) != 1 :
	exit(-1)
if int(appa[0][3] % appa[1][5]) != 100 :
	exit(-1)
if int(appa[0][15] + appa[1][0]) != 166 :
	exit(-1)
if int(appa[0][10] ^ appa[1][4]) != 9 :
	exit(-1)
if int(appa[0][4] / appa[1][10]) != 0 :
	exit(-1)
if int(appa[0][12] + appa[1][3]) != 209 :
	exit(-1)
if int(appa[0][7] + appa[1][0]) != 217 :
	exit(-1)
if int(appa[0][5] / appa[1][1]) != 0 :
	exit(-1)
if int(appa[0][5] + appa[1][7]) != 210 :
	exit(-1)
if int(appa[0][9] % appa[1][11]) != 97 :
	exit(-1)
if int(appa[1][6] + appa[1][9]) != 232 :
	exit(-1)
if int(appa[1][3] * appa[1][15]) != 12210 :
	exit(-1)
if int(appa[1][14] ^ appa[1][5]) != 25 :
	exit(-1)
if int(appa[1][5] % appa[1][5]) != 0 :
	exit(-1)
if int(appa[1][1] % appa[1][11]) != 105 :
	exit(-1)
if int(appa[1][12] + appa[1][11]) != 217 :
	exit(-1)
if int(appa[1][1] * appa[1][13]) != 10920 :
	exit(-1)
if int(appa[1][5] % appa[1][5]) != 0 :
	exit(-1)
if int(appa[1][10] ^ appa[1][6]) != 11 :
	exit(-1)
if int(appa[1][14] - appa[1][6]) != -2 :
	exit(-1)
if int(appa[1][12] / appa[0][13]) != 1 :
	exit(-1)
if int(appa[1][10] ^ appa[0][10]) != 20 :
	exit(-1)
if int(appa[1][14] % appa[0][0]) != 19 :
	exit(-1)
if int(appa[1][2] - appa[0][15]) != 59 :
	exit(-1)
if int(appa[1][12] ^ appa[0][3]) != 1 :
	exit(-1)
if int(appa[1][3] + appa[0][11]) != 212 :
	exit(-1)
if int(appa[1][1] / appa[0][14]) != 1 :
	exit(-1)
if int(appa[1][12] ^ appa[0][8]) != 6 :
	exit(-1)
if int(appa[1][15] * appa[0][15]) != 5610 :
	exit(-1)
if int(appa[1][5] ^ appa[0][10]) != 8 :
	exit(-1)
if int(appa[0][12] % appa[0][3]) != 98 :
	exit(-1)
if int(appa[0][14] * appa[0][9]) != 9506 :
	exit(-1)
if int(appa[0][4] ^ appa[0][9]) != 3 :
	exit(-1)
if int(appa[0][0] / appa[0][7]) != 0 :
	exit(-1)
if int(appa[0][13] % appa[0][8]) != 97 :
	exit(-1)
if int(appa[0][1] ^ appa[0][0]) != 1 :
	exit(-1)
if int(appa[0][8] - appa[0][11]) != -2 :
	exit(-1)
if int(appa[0][14] / appa[0][9]) != 1 :
	exit(-1)
if int(appa[0][2] % appa[0][7]) != 97 :
	exit(-1)
if int(appa[0][14] - appa[0][0]) != -2 :
	exit(-1)
if int(appa[1][1] + appa[0][7]) != 207 :
	exit(-1)
if int(appa[1][8] + appa[0][11]) != 203 :
	exit(-1)
if int(appa[1][12] % appa[0][15]) != 50 :
	exit(-1)
if int(appa[1][3] % appa[0][2]) != 14 :
	exit(-1)
if int(appa[1][15] % appa[0][15]) != 8 :
	exit(-1)
if int(appa[1][13] % appa[0][0]) != 4 :
	exit(-1)
if int(appa[1][5] ^ appa[0][2]) != 15 :
	exit(-1)
if int(appa[1][0] % appa[0][14]) != 17 :
	exit(-1)
if int(appa[1][14] + appa[0][12]) != 217 :
	exit(-1)
if int(appa[1][10] % appa[0][4]) != 16 :
	exit(-1)
if int(appa[1][10] + appa[1][6]) != 235 :
	exit(-1)
if int(appa[1][15] - appa[1][3]) != -1 :
	exit(-1)
if int(appa[1][11] / appa[1][0]) != 1 :
	exit(-1)
if int(appa[1][6] - appa[1][9]) != 10 :
	exit(-1)
if int(appa[1][9] * appa[1][8]) != 11322 :
	exit(-1)
if int(appa[1][13] * appa[1][13]) != 10816 :
	exit(-1)
if int(appa[1][13] ^ appa[1][0]) != 27 :
	exit(-1)
if int(appa[1][13] % appa[1][4]) != 104 :
	exit(-1)
if int(appa[1][1] + appa[1][2]) != 215 :
	exit(-1)
if int(appa[1][4] * appa[1][1]) != 11655 :
	exit(-1)
