s='["127.0.0.1","234.93.9","431.1.1"]'

s = s.replace('[', '')
s = s.replace(']', '')
s = s.replace('"', '')
s = s.replace(',', ' ')

print(s)