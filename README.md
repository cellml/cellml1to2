# cellml1to2
Attempt at using XSLT to translate CellML 1.0 and 1.1 documents into the proposed CellML 2.0 format.

Note that it needs an XSLT 2 processor to handle namespace nodes nicely. Tested using the Saxon engine within oXygen XML and Saxon on the command line, e.g., `saxon -s:test-models/cellml1.0.xml -xsl:cellml1to2.xsl`.

This is primarily an effort to enable the production of a suite of test CellML 2.0 models for use in testing the functionality of [libCellML](http://libcellml.readthedocs.io/).
