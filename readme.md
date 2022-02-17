# hjxh express cmd

## download as source

```shell
git clone  https://github.com/hjxh-opendata/hjxh-express-match-cmd.git
cd hjxh-express-match-cmd
```

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

![picture 1](https://mark-vue-oss.oss-cn-hangzhou.aliyuncs.com/readme-1645033395420-a7382643440ca5a096c1f3b0e9d12f3949bff9120ca0f9d80c2521e5b2452276.png)  
