# Steps to install Ta-lib on Ubuntu 20.04:
* Download source file tar from https://ta-lib.org/
* Compile library:
    ```bash
    tar -xf ta-lib-0.4.0-src.tar.gz
    cd ta-lib
    ./configure --prefix=/opt/ta-lib
    make
    sudo make install
    ```
* Ta-Lib python bindings https://github.com/huanghyw/ta-lib
* Point the python bindings to the library installation directory:
    ```bash
    export TA_LIBRARY_PATH=/opt/ta-lib/lib
    export TA_INCLUDE_PATH=/opt/ta-lib/include
    ```
