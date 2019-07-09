# --------------------------------------------------
# Re-Limiter.py
# v1.0 - 7/9/2019

# Justin Grimes (@zelon88)
#   https://github.com/zelon88/Re-Limiter
#   https://www.HonestRepair.net

# Made on Windows 7 with Python 2.7.12

# This program is for replacing delimiters in files containing separated data.
# For example, you can use this program to convert a comma separated file into a tab separated file
# --------------------------------------------------

# --------------------------------------------------
# VALID ARGUMENTS / PARAMETERS / SWITCHES
# If you combine multiple verbosity or log levels the last specified will be used.

#  h - Display help text. 1st argument.

#  <delimiter to be replaced> - 1st argument.

#  <delimiter to replace with> - 2nd argument.

# <C:\Path\To\InputFile.csv> - 3rd argument.

# <C:\Path\To\OutputFle.txt> - 4th argument.

#  f - Forced overwrite. Optional. 5th, 6th, or 7th argument.

#  v0 - Verbosity 0. Optional. Disable output. 5th, 6th, or 7th argument.
#  v1 - Verbosity 1. Optional. Only errors are output. 5th, 6th, or 7th argument.
#  v2 - Verbosity 2. Optional. Everything is output. 5th, 6th, or 7th argument.

#  l0 - Log level 0. Optional. Disable logging. 5th, 6th, or 7th argument.
#  l1 - Log level 1. Optional. Only errors logged. 5th, 6th, or 7th argument.
#  l2 - Log level 2. Optional. Everything is logged. 5th, 6th, or 7th argument.
# --------------------------------------------------

# --------------------------------------------------
# EXAMPLE COMMANDS

# Display help text.
#  Re-Limiter.py h
# Replace "," with " " from c:\TestFolder\test.csv and save it to c:\TestFolder\output.txt.
#  Re-Limiter.py , " " c:\TestFolder\test.csv c:\TestFolder\output.txt
# Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt.
#  Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f
# Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt with full logging.
#  Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f l2
# Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt with full verbosity.
#  Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f v2
# Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt with no logs or verbosity.
#  Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f v0 l0
# --------------------------------------------------

# --------------------------------------------------
# Load required modules and set global variables.
import sys, getopt, datetime, os
progFileName = "Re-Limiter.py"
progName = "Re-Limiter"
progVers = "v1.0"
progDesc = 'This program allows you to convert the delimiting characters in delimited files into other characters while preserving original data.'
logPrefix = 'OP-Act: '
scriptPath = os.path.dirname(sys.argv[0]) 
forced = False
currentPath = os.path.dirname(__file__)
logFile = os.path.join(currentPath, 'Re-Limiter.log')
now = datetime.datetime.now()
time = now.strftime("%B %d, %Y, %H:%M")
error = feature = inputFile = inputPath = outputPath = outputFile = ''
errorCounter = 0
logging = 1
verbosity = 2
# --------------------------------------------------

# --------------------------------------------------
# A function to print output to the console in a consistent manner.
def printGracefully(logPrefix, message):
  print (logPrefix+message+'.')
  return 1
# --------------------------------------------------

# --------------------------------------------------
# A function to kill the program gracefully during unrecoverable error.
# The errorMessage will be displayed to the user, unless the s switch is set.
# Note this uses sys.exit(), which not only kills this script but the entire interpreter.
def dieGracefully(errorMessage, errorNumber, errorCounter):
  print ('ERROR-'+str(errorCounter)+'!!! '+str(progName)+str(errorNumber)+': '+str(errorMessage)+' on '+str(time)+'!')
  sys.exit()
  return 1
# --------------------------------------------------

# --------------------------------------------------
# A function to write an entry to the logFile. 
# Do not punctuate your log entries with punctuation, or it will look strange.
# Set the errorNumber to 0 for regular prefix (default is "OP-Act").
# If the entry is an error message, set errorNumber to an int greater than 0.
def writeLog(logFile, logEntry, time, errorNumber, errorCounter):
  if os.path.isfile(logFile): append = "ab"
  else: append = "wb+"
  if errorNumber > 0: entryPrefix = 'ERROR-'+str(errorCounter)+'!!! '+str(progName)+str(errorNumber)+': '
  else:  entryPrefix = logPrefix
  entrySufix = ' on '+str(time)+'.'
  with open(logFile, append) as logData:
    logData.write(entryPrefix+logEntry+entrySufix+"\n")
    logData.close
  return 1
# --------------------------------------------------

# --------------------------------------------------
# Process user supplied arguments/parameters/switches.
def parseArgs(logging, verbosity, argv, errorCounter):
  forced = False
  # Check if any arguments were passed.
  try: opts, args = getopt.getopt(argv,"h")
  except getopt.GetoptError: 
    print (str(progFileName)+' <old delimiter> <new delimiter> <inputFile> <outputFile> <options>')
  if len(sys.argv) <= 1:
    print ('\nType "'+str(progFileName)+' help" to display '+str(progName)+' usage & version information.\n')
    sys.exit(2)
  if sys.argv[1] == 'h' or sys.argv[1] == 'help':
    # Print the help text if the "h" argument is passed
    print ('\n'+str(progName)+' '+str(progVers)+', by Justin Grimes (@zelon88) - https://www.HonestRepair.net\n')
    print ('\n'+str(progDesc)+'\n\n'+str(progFileName)+' <old delimiter> <new delimiter> <inputFile> <outputFile> <options>\n')
    print (' Options: ')
    print ('----------')
    print ('  h = Display Help & Version Information')
    print ('  help = Display Help & Version Information')
    print ('----------')
    print ('  f = Force Overwrite Of Output File')
    print ('  force = Force OverWrite Of Output File')
    print ('  forced = Force OverWrite Of Output File')
    print (' ---------')
    print ('  v0 = Display No Messages')
    print ('  v1 = Display Warning Messages Only') 
    print ('  v2 = Display All Messages')
    print (' ---------')
    print ('  l0 = Record No Logs')
    print ('  l1 = Record Warning Logs Only') 
    print ('  l2 = Record All Logs')
    sys.exit(2)
  if len(sys.argv) > 4:
    # Set the logging level from argument 4.
    if sys.argv[5] == 'l0': logging = 0
    if sys.argv[5] == 'l1': logging = 1
    if sys.argv[5] == 'l2': logging = 2
    # Set the verbosity level from argument 4.
    if sys.argv[5] == 'v0': verbosity = 0
    if sys.argv[5] == 'v1': verbosity = 1
    if sys.argv[5] == 'v2': verbosity = 2
    # Set forced overwrite from argument 4.
    if sys.argv[5] == 'f' or 'force' in sys.argv[5]: forced = True
  if len(sys.argv) > 5:
    # Set the logging level from argument 5.
    if sys.argv[6] == 'l0': logging = 0
    if sys.argv[6] == 'l1': logging = 1
    if sys.argv[6] == 'l2': logging = 2
    # Set the verbosity level from argument 5.
    if sys.argv[6] == 'v0': verbosity = 0
    if sys.argv[6] == 'v1': verbosity = 1
    if sys.argv[6] == 'v2': verbosity = 2
    # Set forced overwrite from argument 5.
    if sys.argv[6] == 'f' or 'force' in sys.argv[6]: forced = True
  if len(sys.argv) > 6:
    # Set the logging level from argument 6.
    if sys.argv[7] == 'l0': logging = 0
    if sys.argv[7] == 'l1': logging = 1
    if sys.argv[7] == 'l2': logging = 2
    # Set the verbosity level from argument 6.
    if sys.argv[7] == 'v0': verbosity = 0
    if sys.argv[7] == 'v1': verbosity = 1
    if sys.argv[7] == 'v2': verbosity = 2
    # Set forced overwrite from argument 6.
    if sys.argv[7] == 'f' or 'force' in sys.argv[7]: forced = True
  # Check to see if an input delimeter was supplied.
  try: sys.argv[1]
  except IndexError:
    errorCounter += 1    
    message = 'No original delimiter was specified'
    if logging > 0: writeLog(logFile, message, time, 89, errorCounter)
    if verbosity > 0: dieGracefully(message, 89, errorCounter)
    else: sys.exit()
  else:
    oldLimiter = sys.argv[1]
  # Check to see if an output delimeter was supplied.
  try: sys.argv[2]
  except IndexError:
    errorCounter += 1    
    message = 'No new delimiter was specified'
    if logging > 0: writeLog(logFile, message, time, 89, errorCounter)
    if verbosity > 0: dieGracefully(message, 89, errorCounter)
    else: sys.exit()
  else:
    newLimiter = sys.argv[2]
  # Check to see if an input file argument was supplied.
  try: sys.argv[3]
  except IndexError:
    # Display an error and stop execution if the input argument is missing.
    # "ERROR-<#>!!! Re-Limiter89, No input file was specified on <time>."
    errorCounter += 1    
    message = 'No input file was specified'
    if logging > 0: writeLog(logFile, message, time, 89, errorCounter)
    if verbosity > 0: dieGracefully(message, 89, errorCounter)
    else: sys.exit()
  else:
    inputFile = sys.argv[3]
    inputPath = os.path.dirname(inputFile)
    # Display an error and stop execution if the input file does not exist.
    if not os.path.exists(inputFile):
      # "ERROR-<#>!!! Re-Limiter97, The input file specified does not exist on <time>."
      errorCounter += 1
      message = 'The input file specified does not exist'
      if logging > 0: writeLog(logFile, message, time, 97, errorCounter)
      if verbosity > 0: dieGracefully(message, 97, errorCounter)
      else: sys.exit()  
  # Check to see if an output file argument was supplied.
  try: sys.argv[4]
  except IndexError:
    # Display an error and stop execution if the output argument is missing. 
    # "ERROR-<#>!!! Re-Limiter108, No output file was specified on <time>."
    errorCounter += 1
    message = 'No output file was specified'
    if logging > 0: writeLog(logFile, message, time, 108, errorCounter)
    if verbosity > 0: dieGracefully(message, 108, errorCounter)
    else: sys.exit()
  else: 
    outputFile = sys.argv[4]
    outputPath = os.path.dirname(outputFile)
    # Check to see that a directory exists to put an output file into and display an error if not.
    if not os.path.exists(outputPath):
      # "ERROR-<#>!!! Re-Limiter109, The output file specified relies on an invalid directory on <time>."
      errorCounter += 1
      message = 'The output file specified relies on an invalid directory'
      if logging > 0: writeLog(logFile, message, time, 126, errorCounter)
      if verbosity > 0: dieGracefully(message, 126, errorCounter)
      else: sys.exit()
  # Verify that no output file exists already.
  if (os.path.isfile(outputFile) and forced == False):
    errorCounter += 1
    message = 'The output file already exist at '+str(outputFile)
    if logging > 0: writeLog(logFile, message, time, 280, errorCounter)
    if verbosity > 0: dieGracefully(message, 280, errorCounter)
    else: sys.exit()
    print oldLimiter
  return forced, logging, verbosity, inputFile, inputPath, outputFile, outputPath, oldLimiter, newLimiter
# --------------------------------------------------

# --------------------------------------------------
# Perform the actual replacement of data in the selected file.
def relimit(oldLimiter, newLimiter, inputFile, outputFile):
  counter = 0
  with open(inputFile) as inFile:
    for line in inFile:
      line = line.replace(oldLimiter, newLimiter)
      if (os.path.isfile(outputFile) and counter == 0) or not os.path.isfile(outputFile):
        outFile = open(outputFile, "w+")
        outFile.write(line)
        outFile.close()
      if os.path.isfile(outputFile) and counter > 0:
        outFile = open(outputFile, "a")
        outFile.write(line)
        outFile.close()
      counter += 1
    inFile.close()
    if os.path.isfile(outputFile):
      return 0
    else:
      return 1
# --------------------------------------------------

# --------------------------------------------------
# Display some text to kick things off.
# Known as the welcome message.
def printWelcome(logging, verbosity):
  print ('\n')
  message = 'Starting '+str(progName)+' on '+str(time)
  if logging > 1: writeLog(logFile, message, time, 0, 0)
  if verbosity > 1: printGracefully(logPrefix, message)
  return 1
# --------------------------------------------------

# --------------------------------------------------
# Display some text to round things out.
# Known as the goodbye message.
def printGoodbye(logging, verbosity):
  message = 'Operation complete'
  if logging > 1: writeLog(logFile, message, time, 0, 0)
  if verbosity > 1:
    printGracefully('', message)
    print("\n")
    return 1
# --------------------------------------------------

# --------------------------------------------------
# The main portion of the program which makes use of the functions above.
forced, logging, verbosity, inputFile, inputPath, outputFile, outputPath, oldLimiter, newLimiter = parseArgs(logging, verbosity, sys.argv[1:], errorCounter) 
printWelcome(logging, verbosity)
relimit(oldLimiter, newLimiter, inputFile, outputFile)
printGoodbye(logging, verbosity)
# --------------------------------------------------





