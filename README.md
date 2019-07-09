# Re-Limiter
Automated manipulator of character delimited datasets.

# What is it?
Re-Limiter is a command line tool for modifying files containing character delimited datasets. It's primary purpose is converting data which is separated by arbitrary characters into data separated by different arbitrary characters. Perfect for turning a comma-separated list (.csv) into a tab-separated list (.tsv) while preserving the integrity of the data values themselves. Re-Limiter can replace any delimiter (or squence of characters) into any other delimiter. Maybe you want your data values separated by the string "POTATOES." Re-Limiter can make that happen!

Currently Re-Limiter only supports files (not folders). File path arguments require absolute paths.

# How does it work?
Re-Limiter reads input files line-by-line (to conserve memory) and searches its contents for the sequence of characters specified in "old delimiter." When a substring containing this character sequence is located, Re-Limiter will replace the sequence with whatever sequence of characters is specified in "new delimiter." The resultant file will contain the original data values in original order separated by the desired sequence of new characters as the delimiter.  

Re-Limiter will log warnings and display all messages when logging/verbosity arguments are not supplied.

# Why should I try it?

It sure beats CTRL+F & copypasta for dinner!

# Where should I start?

There's some example commands in Example_Commands.txt, but here's a quick rundown...

## Usage

Display help text.
  Re-Limiter.py h

Replace "," with " " from c:\TestFolder\test.csv and save it to c:\TestFolder\output.txt.
 > Re-Limiter.py , " " c:\TestFolder\test.csv c:\TestFolder\output.txt

Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt.
 > Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f

Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt with full logging.
 > Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f l2

Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt with full verbosity.
 > Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f v2

Replace " " with "," from c:\TestFolder\test.csv and overwrite c:\TestFolder\output.txt with no logs or verbosity.
 > Re-Limiter.py "  " , c:\TestFolder\test.test c:\TestFolder\output.txt f v0 l0

# Anything else?

Please check out the code and help me make it better! 

Re-Limiter.py is an [HonestRepair](https://www.HonestRepair.net/) project by Justin Grimes (@zelon88).

<3 Open-Source

# Screenshot!!!

![Re-Limiter](https://github.com/zelon88/Re-Limiter/blob/master/Screenshot.png)	
