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

