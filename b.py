from lxml import etree

students = etree.parse("xml/students.xml")
teachers = etree.parse("xml/teachers.xml")

print("Find all students who study Advanced Databases this year.\n")

path = "/students[@year='2019-2020'][//student//courses//submodule = | ]"
result = students.xpath(path)

for r in result:

    print(etree.tostring(r, pretty_print=True))

print("\nFind all teachers who teach Advanced Databases this year.\n")

path = "/teachers/teacher[course[submodule[name='Advanced Databases' and year='2019-2020']]]"
result = teachers.xpath(path)

for r in result:

    print(etree.tostring(r, pretty_print=True))

# c) How many years has Professor Cristea been teaching ‘Advanced Databases’ (at Durham)?

query = """
    for $x in doc("xml/teachers.xml")/teachers/teacher
    where $x/name=='Alexandra Cristea'
    return 2020 - $x/joiningDate
"""

# d) Find all students n year 3 currently taught by Alexandra.

# e) How many teachers and how many students are kept in the databases where the last name is not known?