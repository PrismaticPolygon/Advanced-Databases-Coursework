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
