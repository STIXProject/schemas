# Impetus 

Structured Threat Information eXpression (STIX) is a collaborative community-driven effort to define and develop a standardized language to represent structured cyber threat information. The STIX Language intends to convey the full range of potential cyber threat information and strives to be fully expressive, flexible, extensible, automatable, and as human-readable as possible. 

Interested parties are welcome to participate in evolving STIX as part of its open community.

Contact us at <stix@mitre.org>

Please visit the [Official STIX Web Site](http://stix.mitre.org) for more information about the STIX Language.

[Usage docs](stixproject.github.io)

The STIX Language operates under the [STIX Terms of Use](http://stix.mitre.org/about/termsofuse.html).

## Dependencies

STIX depends on CybOX, which are installed using [git submodules](http://git-scm.com/book/en/Git-Tools-Submodules) 

Run these commands to get a working setup
    git clone
    git submodule init
    git submodule update

or simply:
`git clone --recursive` 

Whenever the CybOX schema is updated, run `git submodule update` again.
