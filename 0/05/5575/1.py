def encode(h, m, s): return 3600 * h + 60 * m + s
def decode(v): h, rem = divmod(v, 3600); m, s = divmod(rem, 60); return ' '.join(map(str, [h, m, s]))
def parse(t): fh, fm, fs, th, tm, ts = map(int, t); return (fh, fm, fs), (th, tm, ts)
def diff(times): f, t = parse(times); return decode(encode(*t) - encode(*f))
print(*map(diff, map(str.split, map(str.strip, open(0)))), sep='\n')