import pickle
f=open("tokens.bin",'rb')
tokens=pickle.load(f)
print(tokens)