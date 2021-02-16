# Installing new version of Python:

* Download new sources to download folder:
  
  * https://www.python.org/downloads/source/
  
* Install system dependencies:

  ```bash
  sudo apt install lzma lzma-dev liblzma-dev libreadline-dev libsqlite3-dev libgdbm-dev libdb5.3-dev 
  ```

* Unzip the file in the current directory (shouldn't required `sudo` in Downloads folder):

	```bash
	tar -xf Python-<version>.tgz
	```
	
* Configure the python installation:

  ```bash
  cd Python-<version>.tgz
  sudo ./configure --enable-optimizations --prefix=/opt/python-<version>
  ```

* Compile the python installation:

  ```bash
  make -j<NCORES>
  ```

  * If the build stage reports that some of the modules couldn't be found, it's likely because something is missing from the system dependencies above. If all else fails and you know where the missing module/development files (.h) are, you can point the python `setup.py` script to their location with (change the directory to whatever you need):
    ```bash
    export LDFLAGS="-L/opt/local/lib"
    export CFLAGS="-I/opt/local/include"
    ```

* Install the python installation:

  ```bash
  sudo make install
  ```
  
* Now delete the files in your downloads directory (optional)

* Related links:

  * https://solarianprogrammer.com/2017/06/30/building-python-ubuntu-wsl-debian/

# How to use new Python Version:

* Can always be used by specifying the full path. This is usually easiest if you are using a virtual environment because the full path will only be used once (i.e. to setup the virtual environment).
* Setup `update-alternatives` to easily use the new install python versions:

# Notes:

* Python3.6 & Python3.5 would not compile with gcc-10, had to end up using gcc-9.

