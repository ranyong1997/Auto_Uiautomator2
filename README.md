# UIAutoTest
## 概述
本工程是在开源 [uiautomator2](https://github.com/openatx/uiautomator2) 和 [facebook-wda](https://github.com/openatx/facebook-wda) 项目的基础之上，进行了统一的封装，消除两个项目所提供的接口的差异性，同时也将分散的接口功能进行了聚合，降低接入门槛，简化使用操作，同时也最大化保留了原项目的诸多优点，并可以进行更加深度的定制化拓展。  
工程采用业内主流的pytest+allure作为用例运行的基本脚手架和测试报告生成框架，脚本用例采用经典PO模式+业务流程封装+数据分离的思想进行组织和编写。  
本工程编写的初衷是为了尽可能的降低UI自动化脚本的编写和使用门槛，着重在元素定位、异常和断言处理上进行了更进一步的策略优化和封装，使得测试人员可以聚焦在元素基本操作的编写和业务流程的逻辑组织上，而无需刻意关注随机的弹窗遮挡或点击按钮无法跳转下一页面的异常toast报错处理等操作，减少流程中过多的自定义断言处理，提高脚本稳定性和复用性(多平台复用、流程复用)，降低维护成本，加快脚本编写速度。

## 环境要求
- [Pycharm](https://www.jetbrains.com/pycharm/download)
- [Python](https://www.python.org/getit/) <=3.7 
- adb 1.0.32+
- [git](https://git-scm.com/downloads) 
- [allure2](https://github.com/allure-framework/allure2/releases) 2.13+

## 初始化安装
#### Windows
1. 安装最新的[Pycharm](https://www.jetbrains.com/pycharm/download) 社区版  
2. 安装[Python](https://www.python.org/getit/) ，版本3.7  
3. 安装adb，并配置好环境变量  
4. 安装[allure2](https://github.com/allure-framework/allure2/releases) ，点击链接内的Links---Download，解压到任意目录，并配置好环境变量
5. 安装[git](https://git-scm.com/downloads) ，完成后鼠标右键打开git bash，输入：
6. 找一个目录，打开git bash，输入：  
`git clone https://gitee.com/ran_yong/auto_uiautomator2.git`
7. 打开Pycharm，打开上一步拉取下来的UIAutoTest文件夹，导入工程，点击settings---Project---Project Interpretor---add...---New environment---Location中在当前工程名后确认是否有/venv，没有的话手动输入，基本编译器选择python3的安装路径，确认即可
8. Pycharm需要先配置pip的repositories，推荐https://pypi.tuna.tsinghua.edu.cn/simple/ ，Pycharm的Terminal中，输入：  
`pip3 install -r requirements.txt`  
`pip3 install ./install/whl/mtn_perf-0.1.0-py3-none-any.whl ./install/whl/mtn_speed-0.1.0-py3-none-any.whl ./install/whl/facebook_wda-1.3.2.dev31-py3-none-any.whl`  
等待安装完成后，环境就配置完成了，后续执行测试只要执行下面的第9步即可  
9. 手机进入开发者模式，插入usb，确保adb devices可以返回设备号，直接运行对应应用目录下的run.py即可(需要在手机端确认安装一些必须的软件)
#### MacOS
1. 安装最新的Pycharm社区版  
2. 安装python，版本3.7  
3. 安装[Homebrew](https://brew.sh/index_zh-cn)  
4. 安装libimobiledevice工具包   
`brew uninstall --ignore-dependencies libimobiledevice`  
`brew uninstall --ignore-dependencies usbmuxd`  
`brew install --HEAD usbmuxd`  
`brew unlink usbmuxd`  
`brew link usbmuxd`  
`brew install --HEAD libimobiledevice`  
`brew install ideviceinstaller`  
`brew link --overwrite ideviceinstaller`  
5. 安装git、allure、carthage、android-platform-tools  
`brew install git`  
`brew install allure`  
`brew install carthage`  
`brew install android-platform-tools`  
6. 找一个目录，打开git bash，输入：  
`git clone http://alm.adc.com/ittools/CompTest/_git/UIAutoTest`
7. 打开Pycharm，打开上一步拉取下来的UIAutoTest文件夹，导入工程，点击settings---Project---Project Interpretor---add...---New environment---Location中在当前工程UIAutoTest名输入/venv，基本编译器选择python3的安装路径，确认即可
8. Pycharm需要先配置pip的repositories，推荐https://pypi.tuna.tsinghua.edu.cn/simple/ ，Pycharm的Terminal中，输入：  
`pip3 install -r requirements.txt`  
`pip3 install ./install/whl/mtn_perf-0.1.0-py3-none-any.whl ./install/whl/mtn_speed-0.1.0-py3-none-any.whl ./install/whl/facebook_wda-1.3.2.dev31-py3-none-any.whl`   
9. 初始化WebDriverAgent  
`git clone https://github.com/appium/WebDriverAgent Appium-WebDriverAgent`  
`cd Appium-WebDriverAgent && ./Scripts/bootstrap.sh`  
`open WebDriverAgent.xcodeproj`   
然后找台手机接到苹果电脑上。
按照这个文档<https://testerhome.com/topics/7220> 对WebDriverAgent项目进行下设置。
有条件的话还是弄一个苹果的开发者证书比较方便。个人可以用免费的证书(需要修改BundleID)，另外隔几天证书就会过期。
每台设备都需要先用xcode，注册下，能跑起来WDA test
10. 运行run.py即可  
## 快速了解工程框架
### 分层结构
```
Fixtures辅助层(driver、data、业务相关的前后置操作)
     |
   用例层
     |
业务流程逻辑层
     |
PageObject层(继承BasePage)
     |
   元素层(元素数据、元素集切换)
```
### 目录结构
```
WalletUiTest/
  - common/ 存放公共文件
    - base_page.py: 提供基本页面元素操作
    - config_parser.py: 提供配置文件解析方法
    - image.py: 提供图像识别方法
    - logger.py: 提供日志全局配置方法
    - yaml_parser.py: 提供yaml文件解析方法
    - utils.py: 提供工具类方法
  - install/: 存放修改后的源码或依赖库
  - demo/: 文件夹名称表示对应的应用别称(功能域)，demo只是示例名称
    - vXXX/: 以vXXX表示应用版本号以区分版本用例，每个版本一个文件夹(包含文件夹内的文件结构)
      - case/: 存放用例
      - data/: 存放测试数据(yaml文件)
      - element/: 存放定位元素(yaml文件)
        - element_router.py: 元素选择路由，需按照实际补充相关逻辑
      - flow/: 存放业务流程逻辑
      - image/: 存放需要图像识别的元素图像文件
      - page/:  存放PageObject文件
      - conftest.py: 放置与应用强关联的Fixtures操作
      - debug.py: 做步骤调试
      - run.py: 用例统一执行和生成报告
    - config.ini: 应用相关配置
  - report/: 存放与报告相关的文件
    - log: 存放本工程的log日志
    - logcat: 存放抓取的系统和应用日志
    - screenrecord: 存放用例执行过程的录屏
    - screenshot: 存放截图
    - raw_data: 存放allure原始数据
    - html_report_xxxx: allure生成的html报告，以时间分割保存
  - config.ini: 全局相关配置
  - conftest.py: 放置通用的Fixtures和Hooks方法
  - pytest.ini: pytest运行配置
  - README.md: 使用说明文档
```
### 数据结构
- 无结构
    - txt: 分行，无结构的文本数据
- 表格型
    - csv: 表格型，适合大量同一类型的数据
    - excel: 表格型，构造数据方便，文件较大，解析较慢
- 树形
    - json: 可以存储多层数据，格式严格，不支持备注
    - yaml: 兼容json，灵活，可以存储多层数据
    - xml: 可以存储多层，文件格式教繁琐
- 配置型 
    - .ini/.properties/.conf: 只能存储1-2层数据，适合配置文件

由于用例数据常常需要多层级的数据结构，这里选择yaml文件作为本工程的数据文件，示例格式如下：
```
#用例中数据，以以下方式书写，并存放到data/data.yaml中
test_case_0001: 
    param1: aaa
    param2: bbb

#page中的对应的element定位元素，以以下方式书写，并存放到element/中，文件名以 xxx_zz_element.yaml命名，xxx区分page，zz区分语言区域
element_name1: {text: "这是text文案", resourceId: "com.yyy.wallet:id/xxxx"}
element_name2: {resourceId: "com.yyy.wallet:id/zzzz"}
```
数据第一层以用例名标识某条用例所使用的数据，这里约定要和用例中的方法名称完全一致，方便后面使用Fixture方法向用例分配数据；  
元素数据第一层以元素的英文名称标识，后面元素定位的键值对写在一行中，并用大括号{}括起  
想进一步了解yaml语法，参考这篇文章[yaml语言教程](http://www.ruanyifeng.com/blog/2016/07/yaml.html)  
## 快速了解pytest在工程中的应用方式
可以点击[pytest权威教程](https://www.cnblogs.com/superhin/p/11677240.html) 进行深入的学习
### 编写规则
编写pytest测试样例非常简单，只需要按照下面的规则：
- 测试文件以test_开头（以_test结尾也可以）
- 测试类以Test开头，并且不能带有 init 方法
- 测试函数以test_开头
- 断言使用基本的assert即可
### 使用@pytest.fixtures()做初始化
#### 根目录下的conftest.py
在工程根目录下的conftest.py中，提供了driver(scope=session)和start_stop_app(scope=function)两个fixtures方法。driver需要在用例中手动导入，start_stop_app视场景导入用例，表示在用例执行前会启动被测应用，测试结束后关闭应用
#### 应用目录下的conftest.py
在应用每个版本的目录下的conftest.py中，提供了data(scope=function)fixtures方法，用于测试用例的数据驱动，除此以外，与应用相关的自定义的fixtures方法应全部放在该conftest.py文件中，比如一些特定的前置后置操作等等
```
#driver和data传入参数
def test_unionpay_0001(self, driver, start_stop_app, data):
    union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.bind_debit_card_nfc(**data["test_unionpay_0001"])
```
### 使用@pytest.mark.parametrize做参数化
```
@pytest.mark.parametrize(('kewords'), [(u"小明"), (u"小红"), (u"小白")])
def test_kewords(self,kewords):
    print(kewords)

# 多个参数    
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```
### 使用@pytest.mark.dependency()做用例依赖
```
class TestExample(object):

    @pytest.mark.dependency()
    def test_a(self):
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        assert False

    @pytest.mark.dependency(depends=["TestExample::test_a"])
    def test_c(self):
        # TestExample::test_a 没通过则不执行该条用例
        # 可以跨 Class 筛选
        print("Hello I am in test_c")

    @pytest.mark.dependency(depends=["TestExample::test_a","TestExample::test_b"])
    def test_d(self):
        print("Hello I am in test_d")
```
### 使用@pytest.mark.xxx做自定义标记，执行用例筛选作用
建议使用release代表生产环境用例，test代表测试环境用例，smoke代表冒烟级别用例
```
@pytest.mark.release
def test_0001():
    pass

#仅执行标记release的用例
pytest -v -m release
#不执行标记release的用例
pytest -v -m "not release"
```
### 使用@pytest.mark.run(order=N)做用例执行优先级
```
@pytest.mark.run(order=1)
class TestExample:
    def test_a(self):
        pass
```
### 用例失败重试
```
#使用第三方插件
pip install pytest-rerunfailures #使用插件
pytest --reruns 2 # 失败case重试两次

#run.py args传入下值
def run():
    args = ["--reruns", "2", "--reruns-delay", "5"]
    pytest.main(args)
```
## 快速了解allure在工程中的应用方式
- [官方教程](https://docs.qameta.io/allure/)
- 使用@allure.epic标记用例一级模块，建议标记在case层类上
- 使用@allure.feature标记用例二级模块，建议标记在case层方法上
- 使用@allure.story描述用例逻辑功能点，建议标记在flow层方法上
- 使用@allure.title标记用例标题，建议标记在case层方法上
- 使用@allure.step标记用例具体步骤，建议标记在PO层方法上
## 代码编写规范
### 命名
Rule 1. 【强制】类、异常名使用驼峰方式命名，缩写不做强制，但推荐驼峰  
Rule 2. 【强制】常量使用大写字母，并用下划线分隔单词  
Rule 3. 【强制】其余情况一致使用小写字母，并用下划线分隔单词  
Rule 4. 【强制】protected成员使用单下划线前缀，private成员使用双下划线前缀  
Rule 5. 【强制】禁止使用双下划线开头，双下划线结尾的名字(类似__init__)  
正例：  
```
ClassName, ExceptionName  
GLOBAL_CONSTANT_NAME, CLASS_CONSTANT_NAME  
module_name, package_name, method_name, function_name, global_var_name, instance_var_name, function_parameter_name, local_var_name  
_InternalClassName, _INTERNAL_CONSTANT_NAME, _internal_function_name, _protected_member_name, __private_member_name  
```
### 缩进
Rule 1. 【强制】使用4个空格缩进，禁止使用tab缩进  
### 空行
Rule 1. 【强制】文件级定义(类或全局函数)之间隔两个空行，类方法之间隔一个空行  
### 空格
Rule 1. 【强制】圆括号、花括号、方括号内侧都不加空格  
Rule 2. 【强制】不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾)  
Rule 3. 【强制】参数列表, 索引或切片的左括号前不应加空格  
Rule 4. 【强制】所有二元运算符前后各加一个空格  
Rule 5. 【强制】关键字参数或参数默认值里的等号前后不加空格  
Rule 6. 【强制】不要用空格来垂直对齐多行间的标记, 因为这会成为维护的负担(适用于:, #, =等)  
正例：
```
spam(ham[1], {eggs: 2}, [])
if x == 4:
print x, y
x, y = y, x

spam(1)
dict[‘key’] = list[index]

x == 1

def complex(real, imag=0.0): return magic(r=real, i=imag)

foo = 1000 # comment
long_name = 2 # comment that should not be aligned

dictionary = {
“foo”: 1,
“long_name”: 2,
}
```
反例：
```
spam( ham[ 1 ], { eggs: 2 }, [ ] )

if x == 4 :
print x , y
x , y = y , x

spam (1)
dict [‘key’] = list [index]

x<1

def complex(real, imag = 0.0): return magic(r = real, i = imag)

foo = 1000 # comment
long_name = 2 # comment that should not be aligned

dictionary = {
“foo” : 1,
“long_name”: 2,
}
```
### 组装文件路径
使用os.path.join组装文件路径，本工程使用相对路径，相对于run.py所在的路径  
`os.path.join('.', 'data', 'data.yaml')`
## 核心API介绍
### 配置解析操作：config_parser.py
读取根目录和应用目录下的config.ini的字段
```
# 获取平台（Android iOS）
ReadConfig().get_platform
# 获取隐式等待时间
ReadConfig().get_implicitly_wait
# 获取检查错误toast开关状态
ReadConfig().get_check_error_toast
# 获取包名
ReadConfig().get_package_name
# 获取弹窗元素列表
ReadConfig().get_popup_elements
# 获取环境
ReadConfig().get_env
# 获取区域
ReadConfig().get_region
# 获取项目根路径
ReadConfig().get_root_dir
```
### 基本PO操作(二次封装)：base_page.py
```
# 查找元素基本方法，聚合了ios、android元素基本定位方法和图像识别方法，若没有识别到会重试retry_times次数
find_element(retry_times=_MAX_RETRY_TIMES, **locator)

# 查找到元素后进行点击操作，默认会在点击操作结束后检查是否弹出异常toast，若不需要检查输入check_toast=False，若需要忽略正常toast输入ignore_toast,
# config.ini中的check_error_toast进行全局控制
find_element_and_click(check_toast=True, ignore_toast=None, **locator)

# 查找到元素后进行长按操作，默认长按1.0s
find_element_and_long_click(duration: float = 1.0, **locator)

# 查找到元素后进行输入操作，plaintext传入输入的文本，通常输入框无需额外进行点击，识别到即可输入文本
find_element_and_input(plaintext=None, **locator)

# 查找到元素后滑动元素，支持"left", "right", "up", "down"，steps只用于android，从元素中间开始，1步表示滑动5ms，200步表示滑动1s；
# scale用于android的xpath定位时表示从一边滑至另一边的比例(0, 1.0)，scale用于ios时表示滑动元素的宽/高乘以scale的长度
find_element_and_swipe(direction, steps: int = 10, scale: float = 0.8, **locator)

# 查找到元素后拖动元素，与滑动元素不同，这里只支持android，并且需要指定目标点的坐标
find_element_and_drag(*coordinate, **locator)

# 断言元素是否存在，不存在即报错
assert_element_exist(**locator)

# 检查元素存在性，返回bool值
check_element_existence(**locator)

# 断言文字是否存在，不存在即报错
assert_text_exist(plaintext)

# 检查文字存在性，返回bool值
check_text_existence(plaintext)

# 查找到指定的元素后等待元素消失，若超过默认5min时间还没有消失，会断言失败，可依据实际情况修改超时时间，一般用于进度等待
wait_until_element_gone(timeout=300, **locator)

# 滑动屏幕，支持"left", "right", "up", "bottom"，android可以设置滑动的比例，滑动距离是屏幕的宽(高)*scale；ios滑动距离固定，
# 上下滑动是从屏幕中间滑到上下边界，左右滑动是从屏幕最左(右)滑到最右(左)
swipe_screen(direction, scale: float = 0.7)

# 向上滚动屏幕直到指定的元素出现
scroll_until_element_appear(retry_times=_MAX_RETRY_TIMES, **locator)

# 滚动屏幕直到达到应用边界(顶部或底部)
scroll_to_boundary(boundary: str = "end", speed: str = "fast")

# 按键操作，Android支持home, back, left, right, up, down, center, menu, search, enter,delete(or del), recent(recent apps), 
# volume_up, volume_down,volume_mute, camera, power  iOS支持home, volumeUp, volumeDown
press_key(key)

# 打开通知栏
open_notification()

# 打开快速设置栏
open_quick_settings()

# 获取toast
get_toast()

# 屏幕截图
take_screenshot(name="截图")

# 等待，秒
sleep(seconds)
```
### 基本PO操作(原始)：u2和wda提供的原始API
若base_page提供的方法依旧无法满足需求，优先找毕夏提需求，临时可以直接使用u2/wda提供的原始api，引入Fixtures中的driver后可直接调用，相关api使用文档如下：  

[uiautomator2 ](install/uiautomator2/README.md) 使用说明文档  
[facebook-wda](install/facebook-wda/README.md) 使用说明文档

## XPath规则
> 注意此规则只适用于android定位  

为了写起脚本来更快，u2自定义了一些简化的xpath规则

**规则1**  
`//` 开头代表原生xpath

**规则2**  
`@` 开头代表resourceId定位  
`@smartisanos:id/right_container` 相当于`//*[@resource-id="smartisanos:id/right_container"]`

**规则3**  
`^`开头代表正则表达式  
`^.*道了` 相当于 `//*[re:match(text(), '^.*道了')]`

**规则4**   
> 灵感来自SQL like

`知道%` 匹配`知道`开始的文本， 相当于 `//*[starts-with(text(), '知道')]`  
`%知道` 匹配`知道`结束的文本，相当于 `//*[ends-with(text(), '知道')]`  
`%知道%` 匹配包含`知道`的文本，相当于 `//*[contains(text(), '知道')]`  

**规则5**  
默认会匹配text 和 description字段  
如 `搜索` 相当于 XPath `//*[@text="搜索" or @content-desc="搜索" or @resource-id="搜索"]`

**特殊说明**
- 有时className中包含有`$`字符，这个字符在XML中是不合法的，所以全部替换成了`-`
## 开始编写用例
>**基本流程**： element(image)-->page-->flow-->case-->data
### 编写示范
- Terminal中输入 `python -m weditor`
- 使用weditor定位元素(右键点击界面刷新分层结构)，定位元素写到element对应yaml文件中(新增page需要先在element_router.py配置文件路由)
>注意：不同平台提供的定位关键字不同  
>**Android:**  
>- text, textContains, textMatches, textStartsWith  
>- className, classNameMatches  
>- description, descriptionContains, descriptionMatches, descriptionStartsWith  
>- checkable, checked, clickable, longClickable  
>- scrollable, enabled,focusable, focused, selected  
>- packageName, packageNameMatches  
>- resourceId, resourceIdMatches  
>- index, instance  
>
>以上参数都可以单独或组合使用，以下的只能单独使用  
>- child
>- xpath  
>- image  
>
>**iOS:**  
>- className  
>- name, nameContains, nameMatches  
>- label, labelContains  
>- value, valueContains  
>- visible, enabled  
>- index (index 必须与label，value等结合使用) 
> 
>以上参数都可以单独(index除外)或组合使用，以下的只能单独使用  
>- id  
>- child
>- xpath  
>- predicate  
>- classChain  
>- image  
```
# element_router.py
# page和element文件的映射，page的类名作为键，文件名作为值
mapping = {
    "CommonPage": "common_cn_element.yaml",
    "HomePage": "home_cn_element.yaml",
    ...
}
```  
```
# xxx_zz_element.yaml
# resourceId支持简写，消除包名差异，比如com.finshell.wallet:id/tv_order_record，可以简写成tv_order_record
abc: {resourceId: "com.finshell.wallet:id/tv_order_record"}
# 或者(推荐)
abc: {resourceId: "tv_order_record"}

# 组合写法
bcd: {text: "fff", resourceId: "dddeeefff"}

# child写法，传入child关键字，值为字典组成的列表，字典的写法与上面的一致，支持单个和组合，列表长度没有限制
efg: {child: [{className: "android.widget.LinearLayout"},{text: "京津冀互联互通卡"}]}

# right,left,up,down写法，传入right/left/up/down关键字，值为字典组成的列表，字典的写法与上面的一致，支持单个和组合，列表长度限制为2个元素
hij: {right: [{textContains: "身份证", resourceId: "tvName"}, {resourceId: "cetInf"}]}
...
```  
>注意：  
>建议多使用像textContains, textMatches等模糊和正则的写法；resourceId推荐简写的形式，难以定位的元素(只有xpath或者元素重叠)建议用child定位
- page层编写元素的操作，一个元素操作对应一个function，function命名开头需体现操作类型(比如：click_, input_, swipe_, drag_, long_click_,
 double_click, press_x_button, pinch_, check_等等)并使用@allure.step标注步骤，不要多种元素的操作集中到一个function中，应该在flow层中进行组合，增加复用性。
 另外注意，一个page class代表一类独立的功能，它会由若干子页面组成，元素操作的编写要按照模块或者子页面用分割线备注分开，并且方法的顺序按照页面操作顺序合理放置，便于查找
```
# xxx_page.py
class XXXPage(BasePage):

    def __init__(self, driver):
        super(XXXPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- XXX模块/子页面 -------------------
    @allure.step("点击abc")
    def click_abc(self):
        self.find_element_and_click(**self.element["abc"])

    # ----------------- YYY模块/子页面 -------------------
    @allure.step("输入bcd")
    def input_bcd1(self, bcd1):
        self.find_element_and_input(bcd1, **self.element["bcd1"])

    @allure.step("输入bcd")
    def input_bcd2(self, bcd2):
        self.find_element_and_input(bcd2, **self.element["bcd2"])
    ...
```
>调试某一个步骤
```
# debug.py
def step(d):
    page = XXXPage(d)
    page.click_abc()
```
- flow层组合操作逻辑
```
# xxx_flow.py
class XXXFlow(object):

    def __init__(self, driver):
        self.xxx_page = XXXPage(driver)

    @allure.story('描述是干什么的流程，比如登录账户')
    def flow_logic_description(self, **kwargs):
        self.xxx_page.click_abc()
        self.xxx_page.input_bcd(kwargs["bcd"])
        ...
```
- case层组合流程
```
# test_xxx.py
@allure.epic("用例一级模块")
class TestXXX:

    @allure.feature("用例二级模块")
    @allure.title("用例标题")
    @pytest.mark.release
    def test_xxx_0001(self, driver, start_stop_app, data): # 注意这里传入的fixtures参数，driver必传，data需要的时候再传
        xxx_flow = XXXFlow(driver)
        xxx_flow.flow_logic_description(**data["test_xxx_0001"])
```
>若需要传递测试数据，data添加数据，传入case层
```
# data.yaml
test_xxx_0001:
  bcd: "abcdefg"
  ...
```
- 运行run.py，执行测试用例，并会自动弹出测试报告
>**注意：**  
>用例执行时默认会自动启动app，执行结束后关闭app(相关的方法可在根目录下的conftest.py中查看)，若用例需要额外的前后置操作(比如还原执行前的状态)，
>请在应用目录下的conftest.py中增加fixtures方法并在对应用例参数中导入
## 增加日志打印
导入logging模块即可(通常用例中不需要再额外打印日志)
```
import logging

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()
logging.exception()
```
## 查看测试报告
运行run.py完成测试后会自动处理报告并使用默认浏览器打开报告，若关闭后想再次打开，请在pycharm中找到对应报告的目录下的index.html，右击--Open in Browser
