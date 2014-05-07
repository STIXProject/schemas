------------------------
APT1 Report Converstion to STIX
------------------------

First of all, the STIX team would like to thank Mandiant for allowing us to distribute this content
as well as for the high-level comments they gave us on the result. Please note that the STIX content
was the responsibility of MITRE and Mandiant makes no statement that it is correct or accurate. The
following disclaimer applies to all of the conversion results, including both the raw STIX files that
MITRE converted and the HTML representations of that content:

APT1: Exposing One of China's Cyber Espionage Units (the "APT1 Report")
is copyright 2013 by Mandiant Corporation and can be downloaded at 
intelreport.mandiant.com.  This XML file using the STIX standard was created
by The MITRE Corporation using the content of the APT1 Report with Mandiant's
permission.  Mandiant is not responsible for the content of this file.

------------------------
Approach and Caveats
------------------------
Please note that the intent of this conversion was not to create a complete 1:1 parity mapping to the
original report, rather it was to provide an illustrative example of what a comprehensive report such
as APT1 might look like in STIX.  Therefore, not everything that appears in the original APT1 report is
represented in the STIX content that MITRE developed.  One particularly noteworthy feature of this content
is that it makes substantial use of the higher-level constructs in STIX, including TTPs, Threat Actors
and Campaigns. Thus, we hope that you find the report useful in understanding how these constructs work
and how they can be related to lower-level technical intelligence.

The conversion resulted in 7 STIX documents, explained below. The source documents are all available from
Mandiant's website at: http://intelreport.mandiant.com.

Mandiant_APT1_Report.xml
------------------------
This document is the result of a manual conversion of the APT1 report itself (Mandiant_APT1_Report.pdf)
into a representative portion of that report in STIX 1.1.1. The process was to read through the report
and manually create STIX 1.1.1 XML content to match the contents of the report, with the primary focus
on TTPs, Threat Actors, and Campaigns. The intent was not to convert the whole report but to provide
illustrative examples of the higher-level content that the APT1 report describes. As such, not all material
in the original report is in the conversion and some of the material that was converted over may have small
bugs or be incomplete. Please treat it as an example and not as a finished intelligence product.

Appendix_D_FQDNs.xml
------------------------
This document is the result of an automated conversion of Appendix D (Digital) - FQDNs.txt into CybOX
observables wrapped in a STIX package. The conversion was performed using a custom script that took advantage
of the Python bindings and APIs. The logic was to create an individual DomainNameObj Observable for each line
in the source file with a type of "FQDN" and a value of the domain.

Note that no indicators were created: because the appendix was not called an IOC and the domains were not
all explicitely said to be malicious we intentionally limited the conversion to creating raw observables.

Appendix_E_MD5s.xml
------------------------
This document is the result of an automated conversion of Appendix E (Digital) - MD5s.txt into CybOX observables
wrapped in a STIX package. The conversion was performed using a custom script that took advantage of the Python
bindings and APIs. The logic was to create an individual FileObject Observable for each line in the source file
with a Simple_Hash_Value of the hash.

Again, no indicators were created because the appendix was not called an IOC and the MD5s were not explicitly
said to be malicious.

Appendix_F_SSLCertificates.xml
------------------------
This document is the result of an automated conversion of Appendix F (Digital) - SSLCertificates.pdf into CybOX
observables wrapped in a STIX package. The conversion was performed using a custom script that took advantage of
the Python bindings and APIs. The logic was to create an individual X509CertificateObject Observable for each
certificate in the PDF.

Once again, no indicators were created because the appendix was not called an IOC and the certificates were not
explicitly said to be malicious.

Appendix_G_IOCs_Full.xml, Appendix_G_IOCs_No_Observables.xml, Appendix_G_IOCs_No_OpenIOC.xml
------------------------
These three documents are the result of an automated conversion of the IOCs in the Appendix G (Digital) - IOCs
folder into STIX indicators. The conversion was performed using a custom script that took advantage of the Python
bindings and APIs. Each document was the result of a conversion using slightly different logic:

* Appendix_G_IOCs_No_Observables.xml was created by creating a STIX indicator for each IOC and embedding the original
	OpenIOC content in that using the OpenIOC extension to the indicator's TestMechanism. This file does not contain any
	CybOX observables.
* Appendix_G_IOCs_No_OpenIOC.xml was creating in the same way as above except instead of including the original OpenIOC
	content that content was converted to CybOX using the OpenIOC_to_CybOX library. The resulting observables
	(including a top-level composite) are then referenced by the indicator as the pattern for that indicator. The
	original OpenIOC content is not included.
* Appendix_G_IOCs_Full.xml was created as a combination of the two approaches above. It includes both the original
	OpenIOC as a TestMechanism and the converted CybOX as the indicator's CybOX pattern. 

------------------------
HTML Versions
------------------------

For each of the XML files above, the stix_to_html utility was used to create HTML versions of the STIX source. The files are
named identically to the XML files but with an HTML extension. Please note that because the stix_to_html tool is still
experimental and still under development the HTML views are incomplete representations of the XML. In particular, some of
the higher-level constructs like Campaign and Threat Actor are still under development in the tool so the HTML views of
those components will be missing content that’s present in the XML.