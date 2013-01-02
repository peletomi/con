# con

## Description

This tool hands out configuration data over a REST API. The configuration values
are stored in files in YAML format. The key idea here is that these files are
in some kind of version control so each change is tracked and access rigths are
enforced.

## REST structure

http://BASE/get/DIRECTORY/FILE/KEY/[CONTEXT_KEY/CONTEXT_VALUE]

* DIRECTORY - from which the configuration files are read. This can be used
              for example to distinguish between live and test environments.
* FILE      - the name of the configuration file. This can be used to distinguish
              components in a complex system.
* KEY       - key of the property

Contexts can be used to constraint the configuration property to context. For example the
key: mail.encoding has to have the value UTF-8 for hungarian language, but for all other
locales it should be ISO-8859. In this case the context key could be 'locale' the value
'hu_HU'. If there is no value for the given context key and value pair the service tries
fallback to a more general one.

## Dependencies

* YAML
* cherrypy
* nosetests

## Examples

From the 'src' directory start service with:

    python2.7 ./web.py -r ..

Then try:

    http://127.0.0.1:8080/get/examples/example_config/foo.bar/country/de/version/4
