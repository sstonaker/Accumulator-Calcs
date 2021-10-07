stdtemp = 60
stdpres = 14.7

print('\n\nProgram #1 Accumulator Calculations API 16D Method 2 (Ideal Gas)')
print('\nThe std temp is %s degrees and the std pres is %s psia.' %
      (stdtemp, stdpres))
print('\nUsing standard conditions...\n\n')

while True:
    try:
        numbottles = int(input('Number of Bottles?\n'))
    except ValueError:
        print('Value must be integer > 0')
        continue
    if numbottles > 0:
        break
    else:
        print('Value must be integer > 0')
        continue

precharge = int(input('Bottle Precharge Pressure?\n'))
MOP = int(input('Minimum operating Pressure? (Usually Precharge + 200psi)\n'))

while True:
    try:
        bottlesize = float(input('Bottle Size (10 or 15)?\n'))
    except ValueError:
        print('Value must equal 10 or 15')
        continue
    if bottlesize == 10 or bottlesize == 15:
        break
    else:
        print('Value must equal 10 or 15')
        continue


if bottlesize == 10:
    gasvol = 9.9
elif bottlesize == 15:
    gasvol = 13.7

syspres = 3000

p0 = precharge + stdpres
p1 = syspres + stdpres
p2 = MOP + stdpres

gasvol0 = numbottles * gasvol
liqvol0 = numbottles * gasvol - gasvol0

e1 = p0/p1
e2 = p0/p2

gasvol1 = gasvol0 * e1
gasvol2 = gasvol0 * e2
liqvol1 = (1-e1) * gasvol0
liqvol2 = (1-e2) * gasvol0

usablefluid = liqvol1 - liqvol2


print('\nMOP: %s' % MOP)
print('Usable Gas Volume: %.1f\n' % gasvol)
print('                 Gas Vol        Liq Vol')
print('p0 @ %.1f      %.2f           %.1f' % (p0, gasvol0, liqvol0))
print('p1 @ %.1f      %.1f           %.1f' % (p1, gasvol1, liqvol1))
print('p2 @ %.1f      %.1f           %.1f' % (p2, gasvol2, liqvol2))
print('\n\nUsable Liquid Volume: %.1f gal' % usablefluid)
