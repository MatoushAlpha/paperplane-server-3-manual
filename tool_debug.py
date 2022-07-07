

def log_restart():
  f = open("tool_debug_output.txt", 'w')
  f.close()

def log_add(text_input):
  f = open("tool_debug_output.txt", 'a')
  f.write(str(text_input))
  f.write("\n")
  f.close()

def log_nl():
  f = open("tool_debug_output.txt", 'a')
  f.write("\n")
  f.close()