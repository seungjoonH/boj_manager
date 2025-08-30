name, _, *teams = map(str.strip, open(0))

def prob(team):
  l, o, v, e = map((team + name).count, "LOVE")
  return ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100

l = list(map(prob, teams))
print(min(teams, key=lambda t: (-prob(t), t)))