------------------------
FireEye Poison Evy Report Converstion to STIX
------------------------

First of all, the STIX team would like to thank FireEye for allowing us to distribute this content
as well as for the high-level comments they gave us on the result. Please note that the STIX content is the responsibility of MITRE and FireEye makes no statement that it is correct or accurate.

------------------------
Approach and Caveats
------------------------
As with the APT1 conversion, the intent of this conversion was not to create a complete 1:1 parity mapping to the original report, rather it was to provide an illustrative example of what a comprehensive report such as the FireEye PIVY report might look like in STIX.  Therefore, not everything that appears in the original report is represented in the STIX content that MITRE developed.  One particularly noteworthy feature of this content is that, again much like the APT1 content, it makes substantial use of the higher-level constructs in STIX, including TTPs, Threat Actors and Campaigns. Thus, we hope that you find the report useful in understanding how these constructs work and how they can be related to lower-level technical intelligence.

The conversion resulted in 4 STIX documents, explained below. The source documents are all available from FireEye's website: http://www.fireeye.com/blog/technical/targeted-attack/2013/08/pivy-assessing-damage-and-extracting-intel.html

fireeye-pivy-report.xml
------------------------
This document is the result of a manual conversion of the structured portions of the prose report itself (fireeye-poison-ivy-report.pdf) into a representative portion of that report in STIX 1.1.1. The process was to read through the report and manually create STIX 1.1.1 XML content to match the contents of the report, with the primary focus on TTPs, Threat Actors, and Campaigns. The intent was not to convert the whole report but to provide illustrative examples of the higher-level content that the PIVY report describes. As such, not all material in the original report is in the conversion and some of the material that was converted over may have small bugs or be incomplete. Please treat it as an example and not as a finished intelligence product.

fireeye-pivy-observables.xml
------------------------
This document is the result of an automated conversion of the Maltego graph analysis that was included in the report into STIX/CybOX observables. The intent of this file is to demonstrate the representation of analysis results in STIX/CybOX.

Note that no indicators were created in this file. It simply contains static, instance observables for the data in the analysis.

fireeye-pivy-indicators.xml
------------------------
This document is also the result of an automated conversion of the Maltego graph analysis, however rather than containing instance observables this file contains STIX indicators with patterns. The intent of this file was to demonstrate actionable indicators that can be derived from an analysis and how those indicators can be related to higher-level context. The indicators in this file contain relationships into constructs defined in the prose report (fireeye-pivy-report.xml).

fireeye-pivy-report-with-indicators.xml
------------------------
This document is simply a union of the content in fireeye-pivy-report.xml and fireeye-pivy-indicators.xml. It is included simply for ease of use: many tools, including stix_to_html, are not capable of operating across multiple STIX files and therefore many of the relationships in the indicators file would have been broken.

------------------------
HTML Versions
------------------------

For each of the XML files above, the stix_to_html utility was used to create HTML versions of the STIX source. The files are named identically to the XML files but with an HTML extension. Please note that the stix_to_html utility is experimental and still under development and therefore might omit or incorrectly represent some information. In particular, some of the relationships in higher-level components like TTPs, Threat Actors, and Campaigns are not yet supported.

------------------------
Detailed Conversion Information
------------------------

This section describes in detail how the data was converted. Feel free to skip it if that's not interesting to you.

    ------------------------
    Conversion of Appendix into STIX Observables File
    ------------------------

    The conversion of the appendix was accomplished by walking the Maltego graph file using an automated script. For each relevant node in the graph, the script would create a CybOX observable with an object describing that node. For each edge in the graph, the script would create a Related_Object in the source to the destination (assuming both the source and the destination had CybOX representations).

    The mapping of nodes in the graph to types of CybOX objects is:

                  IPv4Address
                  -------------------
                  AddressObject
                    @category = "ipv4-addr"
                    Address_Value = the address

                  Mutex
                  -------------------
                  MutexObject
                    Name = the mutex

                  ID*
                  -------------------
                  FileObject
                    Custom_Properties/Property
                      @name = "ID"
                      value = the id

                  Password*
                  -------------------
                  FileObject
                    Custom_Properties/Property
                      @name = "PIVY Password"
                      value = the password

                  Hash (Sample)
                  -------------------
                  FileObject
                    Hash
                      @type = "MD5"
                      Simple_Hash_Value = the hash

                  Domain
                  -------------------
                  DomainNameObject
                    @type = "FQDN"
                    value = the domain

                  EmailAddress
                  -------------------
                  WhoisObject
                    Registrants/Email_Address
                      @category = "e-mail"
                      Address_Value = the email

                  Launcher
                  -------------------
                  CodeObject
                    Custom_Properties/Property
                      @name = "MFC Class Name"
                      value = the launcher value

                  ThreatActor
                  -------------------
                  N/A (the threat actor node was used in creating the report)

    ------------------------
    Conversion of Appendix into STIX Indicators File
    ------------------------

    The conversion into the indicators file was much the same. The tree was again walked an observables were generated as above. Instead of creating instance observables, however,
    this conversion created pattern observables and indicators. So, each object above has an independent atomic indicator. The CybOX match type for all indicators was set to "Equals".

    From there, the script takes a "sample-centric" approach and creates a composite indicator for each sample. That composite indicator includes all indicators downstream from the Sample in the graph.

    Each indicator also includes relationships into the reports file as described below.

    ------------------------
    Conversion of Report and Appendix into STIX Report
    ------------------------

    The STIX report file contains both content that was manually generated from the prose report as well as content that was automatically generated by parsing the graph file.

    Starting with the manually converted content, the report contains:

    * A TTP describing the Poison Ivy malware variant
    * TTPs describing high-level attack patterns that were referenced from the report
      * One for Spear Phishing
      * One for Strategic Web Compromise
    * A TTP for each threat actor's attack pattern as described in the report
      * These attack pattern TTPs referenced the appropriate generic attack pattern TTP
    * A TTP for the victim targeting for each threat actor as described in the report
    * A single course of action describing using the Calamine toolset

    With that base of manually converted content, the automatic conversion creates the following items:

    * For each threat actor node in the graph it creates both a Campaign and a Threat Actor in STIX, because the report refers to both.
      * These threat actors and campaigns are related to each other and to the above TTPs as appropriate.
    * Treating each Hash in the graph as a sample, it creates a TTP. That TTP is linked to the generic PIVY TTP as a Variant, to the corresponding composite indicator in the indicators file, and to the campaign and threat actors as indicated in the graph.

    Going back to the indicators file, each indicator contains the following relationships:
    * An Indicated_TTP to the appropriate Sample TTP or TTPs (since some nodes were used by many samples)
    * A Suggested_COA to the single COA

------------------------
Summary
------------------------

The result of this conversion is a holistic bundle of content that includes:

* High level intelligence in the STIX file for the report
* Raw observables in the STIX file with observables
* Indicators (including context referencing the high-level intelligence) in the indicators file

Finally, as noted elsewhere for ease of use the report and indicators file were combined to create the combined bundle.