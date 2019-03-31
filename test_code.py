import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path,"data\\events.xml")

tree = et.parse(xml_file)

root = tree.getroot()

#fetch information from xml file
# for r in root:
#     for element in r:
#         print(element.tag)

#add information to xml file
#
# new_department = et.SubElement(root,"department",attrib={"name":"CIVIL"})
# new_event = et.SubElement(new_department,"event",attrib={"id":"2"})
# new_name = et.SubElement(new_event,"name")
# new_date = et.SubElement(new_event,"date")
# new_time = et.SubElement(new_event,"time")
# new_venue = et.SubElement(new_event,"venue")
# new_description = et.SubElement(new_event,"discription")
# new_rules = et.SubElement(new_event,"rules")
#
# new_name.text = "Hunter League";
# new_date.text = "15 Sept,2019";
# new_time.text = "10:30am to 11:15am and 1:00pm to 4:30pm";
# new_venue.text = "New Building PG Section";
# new_description.text = "It is a treasure hunt type of competition, but the twist lies in the clues. The clues will be given in the form of code. Each team will have to crack the code leading them to another clue. Here the basic knowledge of C programming languages will be put to test. "
# new_rules.text = "";
#
# tree.write(xml_file)

# for r in root:
#     for element in r:
#         if element.attrib['id'] == '2':
#             for event in element:
#                 if event.tag == 'name':
#                     event.text = 'Hunter League'
#                     tree.write(xml_file )
#                     print(event.text)