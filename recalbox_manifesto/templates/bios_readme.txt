Use the md5 command to get the checksum of your files.
Here is a the compatible md5 and filenames, per system.

{% for system_name,system_bios in systems %}- {{ system_name }} : 
{% for bios_hash,bios_filename in system_bios %}{{ bios_hash }}  {{ bios_filename }}
{% endfor %}

{% endfor %}