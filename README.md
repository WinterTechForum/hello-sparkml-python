Hello Spark ML Python
=====================

Run Locally
-----------

On Mac:

    1. [Install pyenv](https://github.com/pyenv/pyenv#installation)

    2. Install Python: `pyenv install 2.7.13`

    3. Use Python 2.7.13: `pyenv local 2.7.13`

    4. Install pyenv-virtualenv: `brew install pyenv-virtualenv`

    5. Add these to your `~/.profile`:

      eval "$(pyenv init -)"
      eval "$(pyenv virtualenv-init -)"

    6. Restart your shell

    7. Setup virtualenv: `pyenv virtualenv 2.7.13 my-virtual-env-2.7.13`

    8. Activate the virtualenv: `pyenv activate my-virtual-env-2.7.13`

    9. Install the deps: `pip install -r requirements.txt`

    10. [Download Spark](http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz)

    11. Extract Spark: `tar -zxvf spark-2.1.0-bin-hadoop2.7.tgz`

    12. Run `test-pyspark.py`:

        ~/YOUR_SPARK_HOME/bin/spark-submit test-pyspark.py
