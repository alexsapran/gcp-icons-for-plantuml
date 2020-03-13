#!/usr/bin/env python
import os
import shutil
import pathlib

import subprocess


PUML_SPIT_GENERATOR_CMD="java -jar ./plantuml.jar -encodesprite 16z {}"
sprite_template ="""
{sprite}

GCPEntityColoring({entity})
!define {entity}(e_alias, e_label, e_techn) GCPEntity(e_alias, e_label, e_techn, GCP_COLOR, {entity}, {entity})
!define {entity}(e_alias, e_label, e_techn, e_descr) GCPEntity(e_alias, e_label, e_techn, e_descr, GCP_COLOR, {entity}, {entity})

"""


def create_sprites():
    for root, dirs, files in os.walk("./Products_and_services"):
        for dir in dirs:
            print("Directory: {}".format(dir))
            folder = "{}/{}".format(root,dir)
            if " " in folder:
                os.rename(folder, folder.replace(' ', '_'))
                folder = folder.replace(' ', '_')

            for _, _, files in os.walk(folder):
                for file in files:
                    full_path="{}/{}".format(folder, file)
                    if " " in file:
                        os.rename(full_path, full_path.replace(' ', '_'))
                        file=file.replace(' ', '_')
                        full_path = "{}/{}".format(folder, file)
                    if "png" in file:
                        sprite = create_sprite(full_path, file)
                        if sprite is not None:
                            move_to_dist(sprite)


def create_sprite(input_file, ent):
    statinfo = os.stat(input_file)
    if statinfo.st_size >= 100000:
        print("Image {} is too big".format(input_file))
        return None

    sprite_filename=input_file.replace(".png", ".puml")
    print("Creating sprite: {}".format(sprite_filename))

    cmd = PUML_SPIT_GENERATOR_CMD.format(input_file).split(" ")
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(timeout=90)

    if stderr is not None:
        print("Error running command : {} \n {}".format(PUML_SPIT_GENERATOR_CMD.format(input_file), stderr))
        return

    sprite_content = sprite_template.format(sprite=str(stdout), entity=ent.replace(".png", ""))
    with open(sprite_filename, 'w') as out_file:
        out_file.write(sprite_content)

    return sprite_filename


def move_to_dist(filename):
    path = pathlib.PurePath(filename)
    dest_path = filename.replace("./{}".format(path.parent.parent.name), "../dist")

    dest_folder = pathlib.PurePath(dest_path)
    if os.path.exists(dest_folder.parent) is False:
        os.mkdir(dest_folder.parent)

    shutil.move(filename, dest_path)


if __name__ == '__main__':
    create_sprites()
