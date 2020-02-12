# Advanced-Databases-Coursework
Coursework for Advanced Databases (SSA)

XPath navigates through a directed tree to select data.

XQuery is the SQL of XML. It selects / combines data using XPath and constructs output.

* `//x`: restricted Kleene closure, i.e. "Find any node with tag `x`".
* `*`: wildcard. Matches any element. 
* `@`: attribute node, e.g. `bib/book/@price` returns the price of the first book.

The directed tree for Part A a) was generated using [this](https://lautgesetz.com/latreex/) website with the following
text:

`
students (root element)
-student
--name
---"John Smith"
--course
---name
----"Software, Systems and Applications III"
---submodule
----"Advanced Databases"
---submodule
----"Web Technology"
--course
---"Computing Methologies III
-student
--firstname
---"Anna"
--lastname
---"Brown
--course
---name
----"Software, Systems, and Applications IV"
---submodule
----"Semantic Web"
--course
---"Computing Methodologies IV"`

### Document Type Definition (DTD)

A concrete set of rules for elements and attributes. Allows for the seamless
data exchange between documents with the same DTD.

`standalone='no'` imposes structure by a DTD.

DTDs can be generated from XML files [here](https://xml.mherman.org/). See [here](https://www.w3schools.com/xml/xml_dtd_intro.asp)
for a tutorial.

XQuery can be tested [here](http://videlibri.sourceforge.net/cgi-bin/xidelcgi), with some difficulty.

c) [here](http://videlibri.sourceforge.net/cgi-bin/xidelcgi?&data=%3C%3Fxml%20version%3D%221.0%22%20standalone%3D%22no%22%3F%3E%0A%3Cteachers%3E%0A%20%20%20%20%3Cteacher%20joiningDate%3D%222018%22%20jobRole%3D%22Professor%22%3E%0A%20%20%20%20%20%20%20%20%3Cname%3EAlexandra%20Cristea%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESoftware%2C%20Systems%20and%20Applications%20III%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3EAdvanced%20Databases%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2018-2019%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2019-2020%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%3C%2Fcourse%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESoftware%2C%20Systems%20and%20Applications%20IV%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESemantic%20Web%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2018-2019%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2019-2020%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%3C%2Fcourse%3E%0A%20%20%20%20%3C%2Fteacher%3E%0A%20%20%3Cteacher%3E%0A%20%20%20%20%3Cname%3EDom%3C%2Fname%3E%0A%20%20%3C%2Fteacher%3E%0A%3C%2Fteachers%3E&=&extract=xquery%20version%20%223.0%22%3B%0A%0Afor%20%24t%20in%20%2Fteachers%2Fteacher%0Awhere%20%24t%2Fname%3D%27Alexandra%20Cristea%27%0A%0Afor%20%24s%20in%20%24t%2Fcourse%2Fsubmodule%0Awhere%20%24s%2Fname%3D%27Advanced%20Databases%27%0A%0Areturn%20count(%24s%2Fyear)%0A%0A%0A&=return%20count(%24s%2Fyear)&input-format=xml&printed-node-format=xml&output-format=xml&compatibility=Standard%20XQuery&dot-notation=off&extract-kind=xquery3.0&print-type-annotations=true&no-extended-strings=true&no-json=true&no-json-literals=true&only-json-objects=true&strict-type-checking=true&strict-namespaces=true&case-sensitive=true)
d) [here](http://videlibri.sourceforge.net/cgi-bin/xidelcgi?&data=%3C%3Fxml%20version%3D%221.0%22%20standalone%3D%22no%22%3F%3E%0A%3Cteachers%3E%0A%20%20%20%20%3Cteacher%20joiningDate%3D%222018%22%20jobRole%3D%22Professor%22%3E%0A%20%20%20%20%20%20%20%20%3Cname%3EAlexandra%20Cristea%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESoftware%2C%20Systems%20and%20Applications%20III%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3EAdvanced%20Databases%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2018-2019%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2019-2020%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%3C%2Fcourse%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESoftware%2C%20Systems%20and%20Applications%20IV%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESemantic%20Web%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2018-2019%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cyear%3E2019-2020%3C%2Fyear%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%3C%2Fcourse%3E%0A%20%20%20%20%3C%2Fteacher%3E%0A%3C%2Fteachers%3E%0A%0A%3Cstudents%20year%3D%222019-2020%22%3E%0A%20%20%20%20%3Cstudent%20enrolmentDate%3D%222017%22%3E%0A%20%20%20%20%20%20%20%20%3Cname%3EJohn%20Smith%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESoftware%2C%20Systems%20and%20Applications%20III%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3EAdvanced%20Databases%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3EWeb%20Technology%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%3C%2Fcourse%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3EComputing%20Methodologies%20III%3C%2Fcourse%3E%0A%20%20%20%20%3C%2Fstudent%3E%0A%20%20%20%20%3Cstudent%20enrolmentDate%3D%222016%22%3E%0A%20%20%20%20%20%20%20%20%3Cfirstname%3EAnna%3C%2Ffirstname%3E%0A%20%20%20%20%20%20%20%20%3Clastname%3EBrown%3C%2Flastname%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Cname%3ESoftware%2C%20Systems%20and%20Applications%20IV%3C%2Fname%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%3Csubmodule%3ESemantic%20Web%3C%2Fsubmodule%3E%0A%20%20%20%20%20%20%20%20%3C%2Fcourse%3E%0A%20%20%20%20%20%20%20%20%3Ccourse%3EComputing%20Methodologies%20IV%3C%2Fcourse%3E%0A%20%20%20%20%3C%2Fstudent%3E%0A%3C%2Fstudents%3E&=&extract=xquery%20version%20%223.0%22%3B%0A%0Afor%20%24s%20in%20%2Fteachers%2Fteacher%5Bname%3D%27Alexandra%20Cristea%27%5D%2Fcourse%2Fsubmodule%2Fname%0A%0Afor%20%24k%20in%20%2Fstudents%2Fstudent%5B%40enrolmentDate%3D%272016%27%5D%0A%20%20%20%20%0Afor%20%24t%20in%20%24k%20%0A%09where%20%24s%3D%24k%2Fcourse%2Fsubmodule%0A%0Areturn%20%24t%0A%0A%0A%0A%0A&=&input-format=xml&printed-node-format=xml&output-format=xml&compatibility=Standard%20XQuery&dot-notation=off&extract-kind=xquery3.0&print-type-annotations=true&no-extended-strings=true&no-json=true&no-json-literals=true&only-json-objects=true&strict-type-checking=true&strict-namespaces=true&case-sensitive=true)
e) [here]()