import os, re, codecs, json

source = 'C:\\mods\\'
ids = {}

for file in os.listdir(source):
	if '.xml' in file:
		isl_id = file
		with open(file, 'r') as f:
			mods = f.read()
			m = re.search('<identifier type="local">(.*)</identifier>', mods)
			local_id = m.group(1)

		ids[local_id] = isl_id

# write out to json
with codecs.open(source+'data.json', 'w', encoding='UTF-8') as json_out:

    # write the list of dictionaries to json
    dump = json.dumps(ids, sort_keys=True, indent=4)
    json_out.write(dump)

# close the file
json_out.close

print "All done! Your JSON file is ready."