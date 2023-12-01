# from ..septic_tank import * # why can't we have good things
exec(open('../septic_tank.py').read())

import re

# so I don't have any more accidentally global internal loop variables...
def main():
    s = 0
    r = re.compile(r'^([0-9]|one|two|three|four|five|six|seven|eight|nine)')
    for l in slorp():
    
        d = ''
        # for c in r.findall(l):
        for i in range(len(l)):
            c = l[i:]
            if r.match(c):
                c = r.match(c).group()
            else:
                continue
            if '0' <= c <= '9':
                d += c
            else:
                d += str('one|two|three|four|five|six|seven|eight|nine'.split('|').index(c)+1)
        s += int(d[0]+d[-1])
    print(s)

if __name__ == '__main__':
    main()
