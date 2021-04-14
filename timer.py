import threading



def printit(function):
  threading.Timer(1.0, printit).start()
  function()

def test():
    print('hello')

printit(test)