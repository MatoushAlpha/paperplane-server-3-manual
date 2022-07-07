

def log_restart():
  f = open("pp_results.txt", 'w')
  f.close()

def log_add(text_input):
  f = open("pp_results.txt", 'a')
  f.write(text_input)
  f.write("\n")
  f.close()

def log_add_inline(text_input):
  f = open("pp_results.txt", 'a')
  f.write(text_input)
  f.write("\n")
  f.close()

def log_nl():
  f = open("pp_results.txt", 'a')
  f.write("\n")
  f.close()