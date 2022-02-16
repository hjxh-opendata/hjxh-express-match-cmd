# hjxh express cmd


## config

```shell
pip install virtualenv

virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

## start

```shell
# test
python main.py

# check file (auto generate `data/history.json` and `logs/*.log`)
python main.py -c data/ERP12月常州韵达1.csv
```