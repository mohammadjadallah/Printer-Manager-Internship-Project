import clr
clr.AddReference(r"E:\BioStar 2 Device SDK\Example\cli\csharp\common\lib\x64\libssl-1_1-x64.dll")  # Load the LogControl.dll assembly

from BS_SDK_V2_x64 import LogControl  # Import the LogControl namespace

# Create an instance of the LogControl class
log_control = LogControl()

# Call methods from the LogControl class
log_control.getLog(None, 1, False)  # Replace the arguments as needed
