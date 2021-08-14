m = float(input('Medida em metros: '))
km = m * 0.001
hm = m * 0.01
dcm = m * 0.1
dm = m * 10
cm = m * 100
mm = m * 1000
print('{:.5f}km \n{:.4f}hm \n{:.3f}dcm \n{}dm \n{}cm \n{}mm'.format(km, hm, dcm, dm, cm, mm))
