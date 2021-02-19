import os
from shutil import copyfile

objects_raw_folder = '/home/vm/object_datasets/objects_raw/bigbird'
objects_gazebo_folder = '/home/vm/object_datasets/objects_gazebo/bigbird'
gazebo_objects_folder = '/home/vm/gazebo-objects/objects_gazebo/bigbird'

folder_names = sorted(os.listdir(objects_raw_folder))

for model_name in folder_names:
    source = os.path.join(objects_raw_folder, model_name, model_name, 'meshes',
                          model_name + '_250_collision.obj')
    dest1 = os.path.join(objects_gazebo_folder, model_name, model_name + '_250_collision.obj')
    dest2 = os.path.join(gazebo_objects_folder, model_name, model_name + '_250_collision.obj')

    copyfile(source, dest1)
    copyfile(source, dest2)
