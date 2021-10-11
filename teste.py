loss = float(input('Please type you current drawdown (em %): '))
low = 100 - loss
recovery = ((loss/low)*100)
print ('You must perform {:.2f}% to back water mark '.format(recovery))