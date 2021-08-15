class ConnectFour:
  def __init__(self):
    self.board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
  ]
  def showlines(self):
    
    print('|-|-|-|-|-|-|-|')
    for row in self.board:
      print('|',end='')

      for cell in row:
        print(cell,end='')
        print('|',end='')
      print('')

con4 = ConnectFour()
con4.showlines()