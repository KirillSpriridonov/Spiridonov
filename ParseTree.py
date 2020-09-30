from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

file_path = "MyTree.ged"

file_record=open("fact.pl",'w',encoding='utf-8')

gedcom_parser = Parser()

gedcom_parser.parse_file(file_path, False)

root_child_elements = gedcom_parser.get_root_child_elements()

for element in root_child_elements:
    if isinstance(element, IndividualElement):
        if len(gedcom_parser.get_parents(element)) != 0:
            name_of_child=element.get_name()[0]
            sur_of_child = element.get_name()[1]
            mother = gedcom_parser.get_parents(element)[1].get_name()
            father = gedcom_parser.get_parents(element)[0].get_name()
            file_record.write('parents(\'{} {}\', \'{} {}\', \'{} {}\').\n'.format(name_of_child,sur_of_child,father[0],father[1],
                              mother[0],mother[1]))
