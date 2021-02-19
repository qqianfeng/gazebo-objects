# Gazebo Objects

This repo contains 350 household 3D objects from the YCB, KIT and BigBird datasets. Each object consists off:
- visual mesh: from the original dataset
- collision mesh: simplified version of the visual mesh (250 faces)
- convex mesh: convex hull of visual mesh, used to compute inertia through trimesh
- config: to import sdf into Gazebo
- sdf: specifying everything needed to spawn objects including inertia.
- texture file: image of the object surface
- material file: to apply texture in Gazebo

## Disclaimer
The bigbird collision meshes had to be manually cleaned up. This process is daunting and, therefore, has only been done for the bigbird objects currently in use. A list of the bigbird objects with clean collision meshes can be found under `scripts/bigbird_list_fixed_meshes.py`. The remaining bigbird objects use a convex hull of the visual mesh as their collision mesh. Therefore, for these objects (especially when having more complex shapes) the collision meshes can differ significantly from the visual meshes.

For the KIT and YCB objects all collision meshes are in great shape.

## Using the models in Gazebo
The models under objects_gazebo can be directly accessed in Gazebo. For this simply execute
```
source gazebo.env
```

## Scripts

Different scripts can be found under the sripts folder. The scripts `create_*_meshes_pymeshlab.py` are used to create simplified collision and convex meshes via pymeshlab. NOTE: pymeshlab is only available through Python 3.7+, the rest of the code runs on Python 2.7 . I handled this via conda, however, minor changes to the `prepare_objects_gazebo.py` file should also make this work with Python 3.

Executing `prepare_objects_gazebo.py` is only possible currently if a folder objects_raw with the raw data from all three mentioned datasets is also present, since it copies the necessary files from there. Further it assumes that the simplified meshes are created through the  `create_*_meshes_pymeshlab.py` scripts and stored next to the raw meshes. `prepare_objects_gazebo.py` will only copy what is necessary from the raw data, read in the template files, compute mass and inertia, assume a density of 1/10th of the water density, and saves everything under objects_gazebo/$DATASET/$MODEL_NAME.


