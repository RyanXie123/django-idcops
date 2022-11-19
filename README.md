# idcops 简介

idcops 是一个基于 Django 开发，倾向于数据中心运营商使用的，拥有数据中心、客户、机柜、设备、跳线、物品、测试、文档等一系列模块的资源管理平台，解决各类资源集中管理与数据可视化的问题。
idcops 通过“数据中心”来分类管理每个数据中心下面的资源，每个数据中心均是单独的。

软件许可协议

django-idcops 遵循 Apache License 2.0。

官方文档：[https://demo.idcops.cn/static/docs/](https://demo.idcops.cn/static/docs/)

GitHub: [https://github.com/Wenvki/django-idcops](https://github.com/Wenvki/django-idcops)

## 交流讨论

[作者博客](https://www.idcops.cn)

QQ群：185964462
[数据中心运维管理idcops](https://jq.qq.com/?_wv=1027&k=5SVIbPP)

---

## 项目截图

[演示地址](http://demo.idcops.cn/)

关注公众号回复数字 **7** 获取体验账号

![weixin_qrcode](https://gitee.com/wenvki/django-idcops/raw/master/screenshots/qrcode_for_weixin.jpg)

![仪表盘](https://gitee.com/wenvki/django-idcops/raw/master/screenshots/2018-12-25_173535.jpg)

---

## 快速开始

### 一、安装

#### **1. 极速安装，支持WSL部署（推荐）**

需要联网，脚本一键自动安装

```bash
cd /opt
curl -sL https://gitee.com/wenvki/django-idcops/raw/master/auto_install.sh | sh

或
cd /opt
wget -q https://gitee.com/wenvki/django-idcops/raw/master/auto_install.sh
sh auto_install.sh

# 安装目录： /opt/django-idcops/ 
# 默认端口号： 18113 (gunicorn)，参数：SrvPort
# 默认idcops版本：develop，参数：VERSION develop[master]
# nginx 反向代理 18113 端口即可
```

[快速部署参考链接](https://mp.weixin.qq.com/s/fOcdTfr6274_Erh3fOftQw)

#### **2. 手动部署线上生产环境**

一步一步手动安装，可以进一步理解Django运行部署

[部署线上生产环境](https://www.idcops.cn/archive/2390/)

#### 二、配置settings.py

`/opt/django-idcops/idcops_proj/settings.py`

```python
# django options

STATIC_URL = '{}static/'.format(SITE_PREFIX)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '{}media/'.format(SITE_PREFIX)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '{}accounts/login/'.format(SITE_PREFIX)

LOGIN_REDIRECT_URL = '{}accounts/profile/'.format(SITE_PREFIX)

# idcops options
# 默认为： '/'
# 可配置为以 '/' 开始的字符串
# 例如： '/idcops/', 则 nginx 反向代理为： http://127.0.0.1:18113/idcops/
SITE_PREFIX = '/'

if SITE_PREFIX:
    SITE_PREFIX = SITE_PREFIX.rstrip('/') + '/'

# SOFT_DELETE 设置为 `True`, 则执行删除的时候不会直接从数据库删除
SOFT_DELETE = True

# COLOR_TAGS 设置为 `True`, 相关标签会根据设置的颜色进行显示
COLOR_TAGS = True

# COLOR_FK_FIELD 设置为 `True`, 相关机房选项会根据设置的颜色进行显示
COLOR_FK_FIELD = False


HIDDEN_COMMENT_NAVBAR = False

# TEST_ENV = True

# `Device` 过保提前提醒天数
REMIND_ADVANCE_DAYS = 30
```

---

## Thanks

![JetBrains Community Support](https://gitee.com/wenvki/django-idcops/raw/master/screenshots/jetbrains.svg)

---

## 捐赠该项目

开源不易，可以用支付宝扫下面二维码以赏金的模式打赏支持。您的支持是我不断创作的动力

![Bounty](https://gitee.com/wenvki/django-idcops/raw/master/screenshots/bounty_for_zfb.png)
