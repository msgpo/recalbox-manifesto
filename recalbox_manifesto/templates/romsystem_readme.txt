## RECALBOX - SYSTEM {{ name }} ##

Put your {{ name }} roms in this directory.

{% if extensions|length > 1 %}Rom files must have one of following file extensions: {{ extensions|join(', ') }}.{% else %}Rom files must have the file extension '{{ extensions[0] }}'.{% endif %}
{% if download_links %}
You can download roms from the following url(s) :
{% for url in download_links %}* {{ url }}
{% endfor %}{% endif %}{% if bios and bios|length > 0 %}
This system requires a bios file to work correctly, see '{{ BIOS_README_FILEPATH }}' for a list of supported Bios.{% endif %}{% if extra_comments and extra_comments|length > 0 %}
{% for comment in extra_comments %}{{ comment }}

{% endfor %}{% endif %}