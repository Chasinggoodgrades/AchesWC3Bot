import commandlist

def handle(msg) -> str:
  msg = msg.lower()

  if msg == 'help':
    return 'Here is a list of commmands: ' + str(commandlist.cmds)