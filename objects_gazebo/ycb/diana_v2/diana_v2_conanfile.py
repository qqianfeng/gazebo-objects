from conans import ConanFile
import os

class ConanPackage(ConanFile):
    name = "diana_v2-urdf"
    version = "2.0.0"
    license = "Proprietary"
    author = 'Various'
    description = "Urdf and meshes for diana_v2"
    url = 'http://git.ar.int/autonomy-and-teleoperation/robot_models.git'
    
    scm = {
        "type": "git",
        "url" : "auto",
        "revision": "auto"
    }
    settings = None
    options = {}
    default_options = ''
    default_user = 'ar'
    default_channel = 'stable'
    no_copy_source = True

    def build(self):
        pass

    def package(self):
        self.copy("diana_v2.urdf", src="agile_robots/diana_v2", keep_path=True)
        self.copy("diana_v2_meta_data.yaml", src="agile_robots/diana_v2", keep_path=True)
        self.copy("*", src="agile_robots/diana_v2/meshes/visual/obj", dst="meshes/visual/obj", keep_path=True)
        self.copy("*", src="agile_robots/diana_v2/meshes/collision/obj", dst="meshes/collision/obj", keep_path=True)

    def package_info(self):
        self.env_info.DIANA_V2_URDF_ARPM_BASE = self.package_folder
        self.env_info.DIANA_V2_URDF_MODEL = os.path.join(self.package_folder, "diana_v2.urdf")
        self.env_info.DIANA_V2_URDF_METADATA = os.path.join(self.package_folder, "diana_v2_meta_data.yaml")

