# STIX 

Structured Threat Information eXpression (STIX) is a collaborative community-driven effort to define and develop a standardized language to represent structured cyber threat information. The STIX Language intends to convey the full range of potential cyber threat information and strives to be fully expressive, flexible, extensible, automatable, and as human-readable as possible. All interested parties are welcome to participate in evolving STIX as part of its open, collaborative community.

Please visit the [STIX Web Site](http://stix.mitre.org) for more information about the STIX Language.

The STIX Language operates under the [STIX Terms of Use](http://stix.mitre.org/about/termsofuse.html).

## Cloning the repository

This STIX schemas repository uses [git submodules](http://git-scm.com/book/en/Git-Tools-Submodules) in order to include the CybOX schemas (which are a dependency of the STIX schemas).

A straight `git clone` command will not retrieve these automatically, you'll end up with an empty cybox directory rather than the schemas. To fix this you need to initialize and then update the submodules by running:

    git submodule init
    git submodule update

Alternatively, using the `--recursive` flag when cloning the repository will automatically initialize and update the submodules.

Finally, any time you see that the cybox directory has been modified (when merging or pulling updates) you will need to run `git submodule update` again to actually update the schemas themselves.