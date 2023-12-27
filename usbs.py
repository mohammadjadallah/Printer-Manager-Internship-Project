import win32print

def get_connected_printers():
  """Returns a list of the currently connected printers."""
  printers = []
  for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL):
    printers.append(printer[1])
  return printers

def main():
  printers = get_connected_printers()
  for printer in printers:
    print(printer)

if __name__ == "__main__":
  main()
