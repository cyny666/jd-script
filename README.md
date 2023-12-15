# jd-scripts
a script used to grab JD products

一个比较简陋的京东商品抢购的脚本，主要是为了帮同学抢购商品

步骤如下

1.先克隆项目

```shell
git clone https://github.com/cyny666/jd-script.git
```

2.安装所需要的环境（可以用虚拟环境）

```shell
pip install selenium
```

3.更改python代码

要求先把商品加进自己的购物车然后查看商品的id（可以用F12大法确定商品的ID）

这里更改时间为抢购时间

```python
    if (datetime_str == "2023-12-19 10:00:00"):
        print("开始抢购")
```

这里更改商品ID为你需抢购的ID

```python
target = driver.find_element(By.ID,"100077030325")
```

4.运行main.py即可开始抢商品



