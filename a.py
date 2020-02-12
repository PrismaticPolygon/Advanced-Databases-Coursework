from lxml import etree

teachers_dtd = etree.DTD("xml/teachers.dtd")
students_dtd = etree.DTD("xml/students.dtd")

teachers = etree.parse("xml/teachers.xml")
students = etree.parse("xml/students.xml")

print("Is DTD for teachers.xml valid: ", teachers_dtd.validate(teachers))
print("Is DTD for students.xml valid: ", students_dtd.validate(students))
