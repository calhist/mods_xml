# run MODS xml through cleanup.xsl

import os, glob, lxml.etree as ET

source_path = 'C:\\mods\\'
out_path = 'C:\\mods\\clean\\'

xml_files = {}
xsl_filename = 'cleanup.xsl'

for root, dirs, files in os.walk(source_path):
	for dir in dirs:
		collection = os.path.join(root, dir)

		# write a list of XMLs to the xml_files dict
		xml_files[dir] = glob.glob1(collection,'*.xml')

# print xml_files

# be sure to change collection name here 
collection = 'test'

for xml in xml_files[collection]:
	xml_filename = source_path+collection+'\\'+xml

	parser = ET.XMLParser(recover=True)
	dom = ET.parse(xml_filename, parser)

	# remove empty nodes
	for element in dom.xpath(".//*[not(node())]"):
		element.getparent().remove(element)

	# remove nodes with text "null"
	for element in dom.xpath(".//*[text()='null']"):
		element.getparent().remove(element)

	# remove nodes with attribute "null"
	for element in dom.xpath(".//*[@*='null']"):
		element.getparent().remove(element)

	xslt = ET.parse(xsl_filename)
	transform = ET.XSLT(xslt)
	newdom = transform(dom)

	out = out_path+xml

    # write out to new file
	with open(out, 'wb') as f:
		f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
		f.write(ET.tostring(newdom, pretty_print = True))
	print "Writing", out
print "All done!"