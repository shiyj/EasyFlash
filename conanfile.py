from mc_conan import MCConanFile


class Lib(MCConanFile):
    name = "EasyFlash"
    version = "0.1"
    # exports_sources = "*","!tmp","!demos"
    exports_sources = "EasyFlash/src/*", "EasyFlash/inc/*", "CMakeLists.txt"
    description = "CmBacktrace mc定制版本"

    def mc_package_src(self):
        # 把所有的头文件放到同一个位置
        self.copy("*.h", dst="include", src="EasyFlash/inc",
                  keep_path=True, excludes=["ef_cfg.h"])
        self.copy("CMakeLists.txt", dst="mc_source", src=".")
        file_ext = ['.h', '.c', '.cpp', '.txt']
        for one in file_ext:
            self.copy("easyflash/*" + one, dst="mc_source",
                      src=".", keep_path=True, excludes=["*ef_cfg.h"])
