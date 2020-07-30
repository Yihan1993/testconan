from conans import ConanFile, CMake


class AddConan(ConanFile):
    name = "add"
    version = "0.2"
    author = "Y.Cheng chengyihan1993@gmail.com"
    description = "test for conan create process"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "src/*"
    # scm = {
    #     "type": "git",
    #     "subfolder": "add",
    #     "url": "https://github.com/Yihan1993/add.git",
    #     "revision": "master",
    #     "password": "405761278ckh"
    # }

#     def source(self):
#         self.run("git clone https://github.com/Yihan1993/add.git")
#         # This small hack might be useful to guarantee proper /MT /MD linkage
#         # in MSVC if the packaged project doesn't have variables to set it
#         # properly
#         tools.replace_in_file("add/CMakeLists.txt", "PROJECT(TestAdd)",
#                               '''PROJECT(add)
# include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
# conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["add"]
