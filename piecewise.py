import EMA
def piecewise(alpha,beta,i):
    if EMA.ema(alpha,beta,i) > 0:
        return EMA.ema(alpha,beta,i)
    else:
        return 0
    