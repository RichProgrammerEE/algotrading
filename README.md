# algotrading

* Create and activate virtual environment (highly recommended):

  ```bash
  virtualenv -p /opt/python-3.6.12/bin/python3.6 ./venv
  source venv/bin/activate
  ```

* DO NOT UPGRADE PIP- This seems to break the --upgrade-strategy only-if-needed option
* Upgrade pip (not sure if this is required or not but it seemed to prevent warnings):

  ```bash
  pip install --upgrade pip
  ```

* Follow the steps in docs/Installing-Zipline.md
* Follow the steps in docs/Installing-TaLib.md
* Run the install script:
    ```bash
    bash scripts/install.bash
    ```