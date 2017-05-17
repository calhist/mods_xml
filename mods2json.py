# MODS XML to CSV

import os, lxml.etree as ET, csv, codecs, json

# set the source directory for MODS.xml files
path = 'C:\\mods\\wagner\\'

# set up dict
files = {}

# open each file in directory
for filename in os.listdir(path):

    if '.xml' in filename:

        # set up empty sub-dict
        mods = {}

        # parse source.xml with lxml
        parser = ET.XMLParser(recover=True)
        tree = ET.parse(path+filename, parser)

        # start cleanup
        # remove any element tails
        for element in tree.iter():
            element.tail = None

        # remove any line breaks or tabs in element text
            if element.text:
                if '\n' in element.text:
                    element.text = element.text.replace('\n', '') 
                if '\t' in element.text:
                    element.text = element.text.replace('\t', '')

        # remove any remaining whitespace
        parser = ET.XMLParser(remove_blank_text=True)
        treestring = ET.tostring(tree)
        clean = ET.XML(treestring, parser)

        # remove empty nodes
        for element in tree.xpath(".//*[not(node())]"):
            element.getparent().remove(element)

        # remove nodes with text "null"
        for element in tree.xpath(".//*[text()='null']"):
            element.getparent().remove(element)

        # remove nodes with attribute "null"
        for element in tree.xpath(".//*[@*='null']"):
            element.getparent().remove(element)

        # finished cleanup


        # start looping through each XML element
        for element in clean.iter():

            parent_tag = ''
            grandparent_tag = ''

            if element.getparent() is not None:
                parent = element.getparent()
                parent_tag = parent.tag.replace('{http://www.loc.gov/mods/v3}', '')+'-'
                if parent_tag == 'mods-' or parent_tag == 'modsCollection-':
                    parent_tag = ''
                if parent.getparent() is not None:
                    grandparent = parent.getparent()
                    grandparent_tag = grandparent.tag.replace('{http://www.loc.gov/mods/v3}', '')+'-'
                    if grandparent_tag == 'mods-' or grandparent_tag == 'modsCollection-':
                        grandparent_tag = ''

            # clean up the tag
            tag = grandparent_tag+parent_tag+element.tag.replace('{http://www.loc.gov/mods/v3}', '')

            # if there are attributes, parse them out and add their values to the tag
            if element.attrib:
                for attrib in element.attrib:
                    tag = tag+'-'+attrib+':'+element.attrib[attrib]

            # exclude top-level tags
            if tag != 'mods' or tag != 'modsCollection':

                # if the tag actually has text
                if element.text:

                    # dict can't have duplicate keys, so make it a list and add to it
                    if tag not in mods:
                        text = element.text
                    elif tag in mods and mods[tag] != element.text:
                        text = element.text+'; '+mods[tag]

                    else:
                        pass

                    # write to sub-dict
                    mods[tag] = text.encode('utf-8')
                    mods['PID'] = filename.replace('_MODS.xml','')
                    
        # write sub-dict to dict
        files[filename.replace('.xml','')] = mods


# get a list of dictionary keys, then normalize all subdicts and add them to a list

all_keys = []
normalized_list = []

for a_file in files:
	for tag in files[a_file]:
		if tag not in all_keys:
			all_keys.append(tag)

for a_file in files:
	mods = {}
	for a_key in all_keys:
		for tag in files[a_file]:
			if a_key in files[a_file]:
				mods[tag] = files[a_file][tag]
			else:
				mods[a_key] = ''

	normalized_list.append(mods)

# write out to json
with codecs.open(path+'data.json', 'w', encoding='utf-8') as json_out:

    #write the dictionary to json
    dump = json.dumps(normalized_list, sort_keys=True, indent=4)
    json_out.write(dump)

# close the file
json_out.close

print "All done! Your JSON file is ready."