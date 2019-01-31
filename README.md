# CHS MODS XML
Resources and tools for creating valid MODS XML for CHS digital collections.

## Contents
### mods_column_headers.csv
A spreadsheet template for cataloging digital objects. Column headers correspond to the OpenRefine templating code.

### mods_column_headers_AV.csv
A spreadsheet template for cataloging AV material. Column headers correspond to the OpenRefine templating code.

### openrefine_mods_template.xml
OpenRefine templating code for exporting to MODS XML. Also includes a versions tailored for the CHS Maps and AV collections.

### mods2json.py
Python script that attempts to parse MODS XML and output to JSON, which can then be imported into OpenRefine. Could certainly use some work, but it's functional.

Before running this script, be sure to set the ```path``` to your source directory of XML files.

### mods_clean.py & cleanup.xsl
An attempt to batch clean MODS XML by running it through XSL. Not very well thought-out at this point, and the XSL is clunky, but at least the Python script is a good source of how to use Python and lxml to run XML through a stylesheet transformation.
