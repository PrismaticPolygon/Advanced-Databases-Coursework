from lxml import etree

students = etree.parse("xml/students.xml")
teachers = etree.parse("xml/teachers.xml")

print("Find all students who study Advanced Databases this year.\n")

path = "/students/descendant::submodule[text()='Advanced Databases']/ancestor::student"
result = students.xpath(path)

for r in result:

    print(etree.tostring(r, pretty_print=True))

print("\nFind all teachers who teach Advanced Databases this year.\n")

path = "/teachers/descendant::submodule[name='Advanced Databases' and year='2019-2020']/ancestor::teacher"
result = teachers.xpath(path)

for r in result:

    print(etree.tostring(r, pretty_print=True))

print("\nc) How many years has Professor Cristea been teaching ‘Advanced Databases’ (at Durham)?\n")

path = "count(/teachers/teacher[name='Alexandra Cristea']/course/submodule[name='Advanced Databases']/year)"
result = teachers.xpath(path)

print(result)


