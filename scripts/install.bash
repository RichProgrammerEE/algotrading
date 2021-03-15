#!/bin/bash

export DISABLE_BCOLZ_AVX2=true
export TA_LIBRARY_PATH=/opt/ta-lib/lib
export TA_INCLUDE_PATH=/opt/ta-lib/include

pip install zipline
pip install --upgrade --upgrade-strategy only-if-needed --no-cache-dir pyfolio
pip install ta-lib
pip install ipykernel