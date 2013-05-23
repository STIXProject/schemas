This set of MAEC/CybOX/STIX files provides an example of the flow between these three standards, highlighting their respective use cases and strengths; this was done using a real Zeus 1.x sample, but the generalized description is as follows:

1) A malware sample is analyzed with Anubis, the output of which is translated into MAEC (and CybOX, accordingly). (maec_anubis_output)

2) Some analyst prunes the noisy data from the MAEC output and constructs a CybOX Observable-based pattern for some of the artifacts resulting from a few actions, corresponding to an instantiation and persistence behavior that he recognizes. (cybox_observable_pattern)

3) The MAEC Package and CybOX Observable are encapsulated as a STIX Indicator in a STIX Package, and the actual malware binary is base64 encoded in and captured in a CybOX Artifact Object in the STIX Package, so that both the context and the Indicator itself are captured in one place. This STIX Package is then shared amongst the cyber-security community; the Indicator is parsed out and used for host-based detection, while the sample Artifact and MAEC data is forwarded to malware analysts for further analysis. (stix_indicator_combined)
