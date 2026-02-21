def decode(text):
    real=""
    codeword=text
    for i in range(len(codeword)):
       if (i+1)%3!=0:
          if i%3!=0:
             real+=codeword[i]
    return real
