import xml.etree.ElementTree as ET
import sys

name = ''
new_version = ''
new_link = ''
new_sha = ""

if len(sys.argv) < 5:
    print('''
Missing Parameters
          Usage : python update-modlinks.py <mod name> <new version> <new download link> <asset sha256>
''') 
    exit(1)
else:
    name = sys.argv[1]
    new_version = sys.argv[2]
    new_link = sys.argv[3]
    new_sha = sys.argv[4]

tag_name = "{https://github.com/HollowKnight-Modding/HollowKnight.ModLinks/HollowKnight.ModManager}Name"
tag_version = "{https://github.com/HollowKnight-Modding/HollowKnight.ModLinks/HollowKnight.ModManager}Version"
tag_link = "{https://github.com/HollowKnight-Modding/HollowKnight.ModLinks/HollowKnight.ModManager}Link"

old_modlinks_data = {'name':'','version':'','link':'' , 'sha': ''}

tree = ET.parse('ModLinks.xml')
root = tree.getroot()
for child in root:
    if child.find(tag_name).text == "Custom Knight" :
        old_modlinks_data['name'] = child.find(tag_name).text.strip()
        old_modlinks_data['version'] = child.find(tag_version).text.strip()
        old_modlinks_data['link'] = child.find(tag_link).text.strip()
        old_modlinks_data['sha']  = child.find(tag_link).get('SHA256').strip()
        break

print(old_modlinks_data)

modlink_str = open('ModLinks.xml','r').read()

modlink_str = modlink_str.replace(old_modlinks_data['version'],new_version)
modlink_str = modlink_str.replace(old_modlinks_data['link'],new_link)
modlink_str = modlink_str.replace(old_modlinks_data['sha'],new_sha)

with open("ModLinks.xml", "w") as f:
    f.write(modlink_str)