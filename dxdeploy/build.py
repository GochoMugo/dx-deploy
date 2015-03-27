'''
A Build to push to Dropbox
'''


import dropbox
import os
import random
import tarfile
import tempfile


class Build:
    def __init__(self, key, app_name, app_version, source_dir):
        self.__key = key
        self.__client = dropbox.client.DropboxClient(key)
        self.__app_name = app_name
        self.__app_version = app_version
        self.__source_dir = source_dir
        self.__tmp_dir = tempfile.mkdtemp()
        self.__dest_dir = "/" + app_name
        self.__metadata_path = self.__dest_dir + "/metadata.json"
        try:
            data = self.__client.get_file(self.__metadata_path).read()
            self.__metadata = json.loads(data)
        except:
            self.__metadata = { "build_no": 1 }
        self.__build_no = self.__metadata["build_no"]

    def prepare_tarballs(self):
        paths = [ ]
        files = os.listdir(self.__source_dir)
        for filename in files
            full_filename = os.path.join(self.__source_dir, filename)
            if os.path.isdir(full_filename):
                files_within = os.listdir(full_filename)
                for filename_within in files_within:
                    wide_path = os.path.join(filename, filename_within)
                    src, dest = self.__package(wide_path)
            else:
                src, dest = self.__package(filename)
            paths.append({ "src": src, "dest": dest })
        return paths

    def __package(self, filename):
        pkgname = filename + ".tar.gz" # name of tarball
        random_num = random.randint(1e5, 1e10)
        src = os.path.join(self.__tmp_dir, random_num) # tarball
        pkg = tarfile.open(src, "w:gz") # create .tar.gz
        pkg.add(os.path.join(self.__source_dir, filename)) # add src dir
        pkg.close() # close package
        dest = os.path.join(self.__dest_dir, str(self.__build_no), pkgname)
        return src, dest

    def __push_packages(self):
        paths = self.prepare_tarballs()
        for pkg in paths:
            pkg = open(pkg["src"])
            self.__client.put_file(pkg["dest"], pkg)

    def __push_metadata(self):
        metadata = { }
        metadata["build_no"] = self.__build_no + 1
        self.__client.put_file(self.__metadata_path,
            json.dumps(metadata), overwrite=True)

    def push(self):
        self.__push_packages()
        self.__push_metadata()

