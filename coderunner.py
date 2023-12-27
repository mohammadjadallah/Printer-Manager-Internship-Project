# import clr
# clr.AddReference(r"C:\Users\Wesam\source\repos\MyCSharpDLL\MyCSharpDLL\bin\Debug\net7.0\MyCSharpDLL.dll")

# from MyCSharpDLL import MyMath

# # Create an instance of MyMath class
# my_math_instance = MyMath()

# # Call the Add function from the DLL
# result = my_math_instance.Add(5, 3)
# print("Result of Add function:", result)
# result = my_math_instance.Add(10, 5)
# print("Result of Add function:", result)
# result = my_math_instance.Add(13, 15)
# print("Result of Add function:", result)

# clr.AddReference(r"C:\Users\Wesam\source\repos\calculator\calculator\bin\Debug\net7.0\calculator.dll")

# from calculator import Class1

# obj = Class1()

# result = obj.calculator(15, 10)
# print(result)

import clr

# Add reference to the compiled ClientRuntime.dll
clr.AddReference(r'C:\Users\Wesam\OneDrive\Desktop\Premium_SDK_rev165_1728\Premium_SDK_rev165_1728\PremiumSDK_rev165_EN\DemoProgram\ClientRuntime\bin\Debug\ClientRuntime.dll')
# clr.AddReference(r'E:\sdk_evolis\Evolis_SDK (version 1.2.2)_EN\platforms\windows\direct_communication\iomem.dll\c++_magnetic_encoding\ReadMagExample\iomem.dll')

# Import the PrinterCommunication class from the ClientRuntime namespace
from ClientRuntime import BusinessHelper

# Set parameters
BusinessHelper.IP = "."
BusinessHelper.Port = "EspfServer00"
BusinessHelper.CommType = "PIPE"  # Or "PIPE" depending on your communication type

# Call methods
# Rkn | Rr | Rip | Rfv | Renm | Rehn | Regw | Rmip | Rwifi;keyw | Rews | Sis | Se | Rcc |
# result = BusinessHelper.SendCommand("Evolis Primacy", "Sis", "10")
# result = BusinessHelper.SendCommand("Evolis Primacy", "Se", "10")
# result = BusinessHelper.SendEcho("Evolis Primacy")
# result = BusinessHelper.GetStatus("Evolis Primacy")
# result = BusinessHelper.PrinterGetState("Evolis Primacy")  # Result: READY,PRINTER_READY | Result: WARNING,FEEDER_EMPTY
# result = BusinessHelper.PrinterGetEvent("Evolis Primacy")
# # Request 1: Set the encoder’s coercivity
# coercivity = BusinessHelper.SendCommand("Evolis Primacy", "Pmc;h", "10")
# # Request 2: Set the encoder’s track 1 format (here ISO1).
# set_track1 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;1;1", "10")
# # Request 3: Set the encoder’s track 2 format (here ISO2).
# set_track2 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;2;2", "10")
# # Request 4: Set the encoder’s track 3 format (here ISO3).
# set_track3 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;3;3", "10")
# # Request 5: Start the sequence (initiate printer's communication)
# start_sequence = BusinessHelper.SendCommand("Evolis Primacy", "Ss", "10")
# # Request 6: Download Magnetic track 1 data to the Evolis printer
# download_magnetic_t1 = BusinessHelper.SendCommand("Evolis Primacy", "Dm;1;EVOLISCARDPRINTER", "10")
# # Request 7: Download Magnetic track 2 data to the Evolis printer
# download_magnetic_t2 = BusinessHelper.SendCommand("Evolis Primacy", "Dm;2;123456789", "10")
# # Request 8: Download Magnetic track 3 data to the Evolis printer
# download_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", "Dm;3;222002", "10")
# # Request 9: Write magnetic data to the card
# write_magnetic = BusinessHelper.SendCommand("Evolis Primacy", "Smw", "10")
# # Request 10: Read magnetic data to the card
# read_magnetic_t1 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;1", "10")
# read_magnetic_t2 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;2", "10")
# read_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;3", "10")
#
# print("Result:", "Track1:", read_magnetic_t1, "Track2:", read_magnetic_t2, "Track3:", read_magnetic_t3)

def magnatic_ecoding(track1: str, track2: int, track3: int, read: bool = False):
    # Request 1: Set the encoder’s coercivity
    coercivity = BusinessHelper.SendCommand("Evolis Primacy", "Pmc;h", "10")
    # Request 2: Set the encoder’s track 1 format (here ISO1).
    set_track1 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;1;1", "10")
    # Request 3: Set the encoder’s track 2 format (here ISO2).
    set_track2 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;2;2", "10")
    # Request 4: Set the encoder’s track 3 format (here ISO3).
    set_track3 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;3;3", "10")
    # Request 5: Start the sequence (initiate printer's communication)
    start_sequence = BusinessHelper.SendCommand("Evolis Primacy", "Ss", "10")
    # Request 6: Download Magnetic track 1 data to the Evolis printer
    download_magnetic_t1 = BusinessHelper.SendCommand("Evolis Primacy", f"Dm;1;{track1}", "10")
    # Request 7: Download Magnetic track 2 data to the Evolis printer
    download_magnetic_t2 = BusinessHelper.SendCommand("Evolis Primacy", f"Dm;2;{track2}", "10")
    # Request 8: Download Magnetic track 3 data to the Evolis printer
    download_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", f"Dm;3;{track3}", "10")
    # Request 9: Write magnetic data to the card
    write_magnetic = BusinessHelper.SendCommand("Evolis Primacy", "Smw", "10")
    # Request 10: Read magnetic data of the card
    read_magnetic_t1 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;1", "10")
    read_magnetic_t2 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;2", "10")
    read_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;3", "10")

    if read:
        print("Result:", "Track1:", read_magnetic_t1, "Track2:", read_magnetic_t2, "Track3:", read_magnetic_t3)
    else:
        return {"Track1": read_magnetic_t1, "Track2": read_magnetic_t2, "Track3": read_magnetic_t3}


mag_enco = magnatic_ecoding("JADALLAHCODE HE IS THE BEST IN THE WORLD", 795158352, 222002)
print(mag_enco)
print(mag_enco["Track1"])
print(mag_enco["Track2"])
print(mag_enco["Track3"])
