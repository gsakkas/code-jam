from math import pi, acos, sqrt, cos, sin


def read_int():
    return int(raw_input())


def read_float():
    return float(raw_input())


def solve(a):
    theta = pi / 4 + acos(a / sqrt(2))
    fst_th = theta
    snd_th = pi / 2 + theta
    fst_pt = (0.5 * cos(fst_th), 0.5 * sin(fst_th), 0.0)
    snd_pt = (0.5 * cos(snd_th), 0.5 * sin(snd_th), 0.0)
    thr_pt = (0.0, 0.0, 0.5)
    return [fst_pt, snd_pt, thr_pt]


def prety_print(coords):
    x, y, z = coords
    print x, y, z


if __name__ == "__main__":
    t = read_int()
    for test in xrange(t):
        a = read_float()
        print "Case #{}:".format(t)
        map(prety_print, solve(a))
    exit(0)
