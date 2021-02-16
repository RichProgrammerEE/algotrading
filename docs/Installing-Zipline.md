# Steps to install Zipline on Ubuntu 20.04:

* zipline only supports up to python3.6 so you must install this first. Follow the steps in `Python-Install.md` for this step.

* Create and activate virtual environment (highly recommended):

  ```bash
  virtualenv -p /opt/python-3.6.12/bin/python3.6 ./venv
  source venv/bin/activate
  ```

* Upgrade pip (not sure if this is required or not but it seemed to prevent warnings):

  ```bash
  pip install --upgrade pip
  ```

* Export environment variable allowing `bcolz` python module to compile (without AVX2 support):

  ```bash
  export DISABLE_BCOLZ_AVX2=true
  ```

  * Reference to this issue:
  * https://github.com/Blosc/bcolz/issues/398
  * https://github.com/shlomikushchi/zipline-trader/issues/159

* Install zipline:

  ```bash
  pip install zipline
  ```

  

