import sys
input = sys.stdin.readline

antenna = int(input().rstrip())
eye = int(input().rstrip())

if (antenna >= 3) and (eye <= 4):
    print('TroyMartian')
if (antenna <= 6) and (eye >= 2):
    print('VladSaturnian')
if (antenna <= 2) and (eye <= 3):
    print('GraemeMercurian')