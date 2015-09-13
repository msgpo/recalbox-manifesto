"""
Command line script
"""
import os

import click

from jinja2 import Environment as Jinja2Environment
from jinja2 import Template
from jinja2 import FileSystemLoader

from .parser import ManifestParser

# Readme file names
ROMSYSTEM_README_FILENAME = BIOS_README_FILENAME = "readme.txt"

# Directory to search for templates
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# Template name for readme files
ROMSYSTEM_README_TEMPLATE = "romsystem_readme.txt"
BIOS_README_TEMPLATE = "bios_readme.txt"

# Bios directory path (this is the 'real' path on the Recalbox not the target 
# for readme building)
BIOS_DIST_PATH = "/recalbox/share/bios"


@click.command()
@click.option('-m', '--manifest', type=click.File('rb'), required=True)
@click.option('--run-dry', is_flag=True, help="Process all command but never create any directories nor files.")
@click.option('--roms', type=click.Path(exists=True), help="Build rom systems readme files and structure into the given path.")
@click.option('--bios', type=click.Path(exists=True), help="Build bios readme file into the given path.")
#@click.option('--verbosity', default='info', type=click.Choice(['debug','info','warning','error','critical']), help="The minimal verbosity level to limit logs output")
def main(manifest, roms, bios, run_dry):
    """
    Parse a manifest XML file and build readme files for rom systems and bios
    
    "lutro": {
        "download_links": [
            "https://github.com/libretro/lutro-platformer", 
            "https://github.com/libretro/lutro-game-of-life", 
            "https://github.com/libretro/lutro-snake", 
            "https://github.com/libretro/lutro-tetris", 
            "https://github.com/libretro/lutro-iyfct", 
            "https://github.com/libretro/lutro-pong"
        ], 
        "extensions": [
            "lua"
        ], 
        "extra_comments": [
            "Hello World!",
            "Lorem ipsum salace"
        ], 
        "name": "LUA games", 
        "bios": []
    }
    "fds": {
        "download_links": [
            "http://www.planetemu.net/roms/nintendo-famicom-disk-system"
        ], 
        "extensions": [
            "fds"
        ], 
        "name": "Nintendo Family Computer Disk System", 
        "bios": [
            [
                "ca30b50f880eb660a320674ed365ef7a", 
                "disksys.rom"
            ]
        ]
    },
    
    """
    if run_dry:
        click.echo('* Run dry enabled, no file/directory will be created')
    
    click.echo('* Parse manifest from: {}'.format(manifest.name))
    Manifest = ManifestParser(manifest).read()
    
    click.echo('* Jinja init with template dir on: {}'.format(TEMPLATES_DIR))
    template_env = Jinja2Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    
    
    # Build roms readme files
    if roms:
        BIOS_DIST_FILEPATH = os.path.join(BIOS_DIST_PATH, ROMSYSTEM_README_FILENAME)
        romsystem_template = template_env.get_template(ROMSYSTEM_README_TEMPLATE)
    
        click.echo('* Start building rom systems readme files to: {}'.format(roms))
        for system_key, system_datas in Manifest.items():
            click.echo('  - System : {}'.format(system_key))
            system_path = os.path.join(roms, system_key)
            readme_path = os.path.join(system_path, ROMSYSTEM_README_FILENAME)
            
            # Fill template context with system datas
            context = {
                'key': system_key,
                'BIOS_README_FILEPATH': BIOS_DIST_FILEPATH,
            }
            context.update(system_datas)
            
            # Rendering template using context
            content = romsystem_template.render(**context)
            
            # Create target path if does not allready exists
            if not os.path.exists(system_path):
                click.echo('    > Path does not exist, create it : {}'.format(system_path))
                if not run_dry:
                    os.makedirs(system_path)
            
            # Create file with rendered template
            if not run_dry:
                with open(readme_path, 'w') as outfile:
                    outfile.write(content.encode('UTF-8'))
            
            #print readme_path
    
    
    # Build bios readme file
    if bios:
        click.echo('* Start building bios readme files to: {}'.format(bios))
        
        bios_systems_list = []
        readme_path = os.path.join(bios, BIOS_README_FILENAME)
        bios_template = template_env.get_template(BIOS_README_TEMPLATE)
        
        for system_key, system_datas in Manifest.items():
            bios_list = system_datas.get('bios', [])
            if len(bios_list)>0:
                click.echo('  - System : {}'.format(system_key))
                bios_systems_list.append( (system_datas.get('name', system_key), bios_list) )
                
        # Fill template context with system datas
        context = {
            'systems': bios_systems_list,
        }
        context.update(system_datas)
        
        # Rendering template using context
        content = bios_template.render(**context)
        
        # Create file with rendered template
        if not run_dry:
            with open(readme_path, 'w') as outfile:
                outfile.write(content.encode('UTF-8'))

#if __name__ == '__main__':
    #main()