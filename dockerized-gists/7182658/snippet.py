#77
for c in 5,5,4,3,2,0,2,3,4,5,5:s=(c*' 'or'*')+'*    '[:6-c];print s+s[-2::-1]