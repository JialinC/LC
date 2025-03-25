# 静态库与动态库的制作与使用

---

## 1. 静态库（Static Library）

### ✅ 命名规则  
- **Linux**: `libxxx.a`  
  - `lib`: 固定前缀  
  - `xxx`: 库名称（自定义）  
  - `.a`: 后缀  
- **Windows**: `libxxx.lib`

### ✅ 制作流程  
1. **编译源文件为目标文件（.o）**  
   ```bash
   gcc -c a.c b.c
   ```

2. **使用 ar 工具打包为静态库**  
   ```bash
   ar rcs libxxx.a a.o b.o
   ```

### ✅ 使用方法  
编译主程序时链接静态库：  
```bash
gcc main.c -L. -lxxx -o main
```
说明：  
- `-L.` 指定库所在路径  
- `-lxxx` 链接名为 `libxxx.a` 的库  

---

## 2. 动态库（Dynamic Library）

### ✅ 命名规则  
- **Linux**: `libxxx.so`  
  - `lib`: 固定前缀  
  - `xxx`: 自定义名  
  - `.so`: 动态库后缀  
- **Windows**: `libxxx.dll`

### ✅ 制作流程  
1. **编译为位置无关代码（fPIC）**  
   ```bash
   gcc -fPIC -c a.c b.c
   ```

2. **生成共享库（.so）**  
   ```bash
   gcc -shared a.o b.o -o libxxx.so
   ```

### ✅ 使用方法  
编译主程序：  
```bash
gcc main.c -L. -lxxx -o main
```
运行程序前设置动态库路径：  
```bash
export LD_LIBRARY_PATH=.
```

---

## 3. 静态库 vs 动态库

| 特性 | 静态库 `.a` | 动态库 `.so` |
|------|-------------|---------------|
| 链接方式 | 编译时链接 | 运行时链接 |
| 是否打包进程序 | 是 | 否 |
| 发布是否需额外库 | 否 | 是 |
| 内存占用 | 高（每个程序各自加载） | 低（共享加载） |
| 更新方式 | 需重新编译程序 | 可直接替换库 |
| 优点 | 移植方便，无依赖 | 更新方便，节省空间 |
| 缺点 | 更新麻烦，程序体积大 | 运行环境需有库文件 |

---

## 🎯 得分点总结
- ✅ 命名规范清楚
- ✅ 制作命令齐全：`gcc -c`, `ar`, `-fPIC`, `-shared`
- ✅ 使用方式包含 `-L`, `-l`，和 `LD_LIBRARY_PATH`
- ✅ 对比有条理，涵盖运行机制、部署、内存等方面

# GDB 常见调试命令简述

---

## ✅ 启动与退出
- 启动调试：
  ```bash
  gdb 可执行程序名
  ```
- 退出：
  ```gdb
  quit 或 q
  ```

---

## ✅ 设置程序参数
- 设置参数：
  ```gdb
  set args 10 20
  ```
- 查看参数：
  ```gdb
  show args
  ```

---

## ✅ GDB 帮助
- 获取帮助：
  ```gdb
  help
  ```

---

## ✅ 查看代码
- 当前文件：
  ```gdb
  list 或 l             # 默认位置开始
  list 行号             # 从指定行开始
  list 函数名           # 从指定函数开始
  ```
- 其他文件：
  ```gdb
  list 文件名:行号
  list 文件名:函数名
  ```

- 设置显示行数：
  ```gdb
  show listsize
  set listsize 行数
  ```

---

## ✅ 设置断点
- 普通断点：
  ```gdb
  break 行号
  break 函数名
  break 文件名:行号
  break 文件名:函数名
  ```
- 条件断点（常用于循环）：
  ```gdb
  break 10 if i == 5
  ```

---

## ✅ 管理断点
- 查看断点：
  ```gdb
  info break 或 i b
  ```
- 删除断点：
  ```gdb
  delete 编号 或 d 编号
  ```
- 禁用断点：
  ```gdb
  disable 编号
  ```
- 启用断点：
  ```gdb
  enable 编号
  ```

---

## ✅ 程序运行控制
- 启动并停在第一行：
  ```gdb
  start
  ```
- 正常运行（遇断点才停）：
  ```gdb
  run
  ```
- 继续运行到下一个断点：
  ```gdb
  continue 或 c
  ```
- 单步执行（不进入函数）：
  ```gdb
  next 或 n
  ```
- 单步执行（进入函数）：
  ```gdb
  step 或 s
  ```
- 跳出当前函数：
  ```gdb
  finish
  ```
- 跳出当前循环：
  ```gdb
  until
  ```

---

## ✅ 变量操作
- 打印变量值：
  ```gdb
  print 变量名 或 p 变量名
  ```
- 打印变量类型：
  ```gdb
  ptype 变量名
  ```
- 自动显示变量值：
  ```gdb
  display 变量名
  info display
  undisplay 编号
  ```
- 设置变量值：
  ```gdb
  set var 变量名=值
  ```

---

## ✅ 多进程调试相关
- 查看 `follow-fork-mode` 选项值：
  ```gdb
  show follow-fork-mode
  ```
- 设置 `follow-fork-mode`：
  ```gdb
  set follow-fork-mode parent | child
  ```
- 查看 `detach-on-fork` 选项值：
  ```gdb
  show detach-on-fork
  ```
- 设置 `detach-on-fork`：
  ```gdb
  set detach-on-fork on | off
  ```
- 查看当前调试中的进程数：
  ```gdb
  info inferiors
  ```
- 切换调试某个进程：
  ```gdb
  inferior 进程ID
  ```

---

## ✅ 总结 - 得分点
- 启动、退出命令
- 设置与查看参数
- 查看代码技巧（当前/非当前文件）
- 各类断点设置与管理（含条件断点）
- 运行控制（start、run、next、step、finish、until）
- 变量操作（print、ptype、display、set var）
- 多进程调试（fork 相关设置、inferiors）
- 其他命令简洁实用

