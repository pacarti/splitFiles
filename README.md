# splitFiles
Splits file into smaller chunks. Especially useful for .zip archives. Slightly modificated from: https://stackoverflow.com/questions/20955556/zip-a-folder-into-parts solution

## Usage
<code>./splitFiles [input file] [chunk size]</code><br>
<br>By default, size is in bytes, but you can add a letter to increase it:
* <b>k</b> to input size in kilobytes
* <b>m</b> to input size in megabytes
* <b>g</b> to input size in gigabytes

<br>Example:
<br><code>./splitFiles inputFile.zip 1g</code><br><br>
This will split a 'inputFile.zip' into 1GB chunks

<br><br>Do not forget to add execution rights to the script.

<br><br>Alternatively:<br>
<code>python3 splitFiles.py [input file] [chunk size]</code>