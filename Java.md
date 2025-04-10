# 1. Java基础

## 1.1 为什么Java代码可以实现一次编写、到处运行？
**参考答案**

JVM（Java虚拟机）是Java跨平台的关键。

- 在程序运行前，Java源代码（`.java`）需要经过编译器编译成字节码（`.class`）。
- 在程序运行时，JVM负责将字节码翻译成特定平台下的机器码并运行。
- 只要在不同的平台上安装对应的JVM，就可以运行字节码文件。

**注意事项**

- 编译的结果是生成字节码，而不是机器码，字节码不能直接运行，必须通过JVM翻译成机器码才能运行。
- 跨平台的是Java程序，而不是JVM。JVM是用C/C++开发的软件，不同平台下需要安装不同版本的JVM。

---

## 1.2 一个Java文件里可以有多个类吗（不含内部类）？
**参考答案**

- 一个Java文件里可以有多个类，但最多只能有一个被`public`修饰的类。
- 如果Java文件中包含`public`修饰的类，则这个类的名称必须和Java文件名一致。

---

## 1.3 说一说你对Java访问权限的了解
**参考答案**

Java语言提供了三种访问修饰符：`private`、`protected`、`public`，以及默认访问权限`default`。这些修饰符可以形成四种访问权限：

- **private**：仅允许类内部访问。
- **default**：允许同一包下的其他类访问。
- **protected**：允许同一包下的其他类以及子类访问。
- **public**：允许任意包下的任意类访问。

### 类的访问权限
- **default**：类可以被同一包下的其他类访问。
- **public**：类可以被任意包下的任意类访问。

---

## 1.4 介绍一下Java的数据类型
**参考答案**

Java数据类型包括：

- **基本数据类型**（8种）
  - 整数类型：`byte`、`short`、`int`、`long`
  - 浮点类型：`float`、`double`
  - 字符类型：`char`
  - 布尔类型：`boolean`
- **引用数据类型**：包括数组、类、接口类型。

### 扩展阅读
基本数据类型的内存占用：

- `byte`：1字节（8位），-2^7 ~ 2^7-1
- `short`：2字节（16位），-2^15 ~ 2^15-1
- `int`：4字节（32位），-2^31 ~ 2^31-1
- `long`：8字节（64位），-2^63 ~ 2^63-1
- `float`：4字节（32位），约 -3.4 × 10^38 ~ 3.4 × 10^38
- `double`：8字节（64位），约 -1.8 × 10^308 ~ 1.8 × 10^308
- `char`：2字节（16位），\u0000 ~ \uffff
- `boolean`：内存大小由JVM实现决定

---

## 1.5 int类型的数据范围是多少？
**参考答案**

- `int`类型占4字节（32位），数据范围是`-2^31` ~ `2^31 - 1`。

---

## 1.6 请介绍全局变量和局部变量的区别
**参考答案**

Java中变量分为**成员变量**和**局部变量**：

### 成员变量
- 定义在类的范围内。
- 有默认初始值。
- **实例变量**：未被`static`修饰，存储于堆内存中，生命周期与对象相同。
- **类变量**：被`static`修饰，存储于方法区中，生命周期与类相同。

### 局部变量
- 定义在方法或代码块中。
- 没有默认初始值。
- 存储于栈内存，生命周期结束后自动释放。

**注意事项**

Java中没有真正的全局变量，面试官的“全局变量”通常是指成员变量。

---

## 1.7 请介绍一下实例变量的默认值
**参考答案**

- **引用数据类型**：默认值为`null`。
- **基本数据类型**默认值：

| 数据类型  | 默认值   |
|--------|--------|
| `byte` | 0      |
| `short`| 0      |
| `int`  | 0      |
| `long` | 0L     |
| `float`| 0.0F   |
| `double`| 0.0   |
| `char` | '\u0000' |
| `boolean` | false |

---

## 1.8 为啥要有包装类？
**参考答案**

Java是面向对象的语言，但8种基本数据类型不具备对象的特性。Java为每个基本数据类型都定义了一个对应的引用类型，这就是**包装类**。

### 扩展阅读
- 包装类的存在使基本数据类型可以作为`Object`类型进行处理，简化了代码操作，解决了基本类型和对象类型之间的转换问题。

---

## 1.9 说一说自动装箱、自动拆箱的应用场景
**参考答案**

自动装箱、自动拆箱是JDK1.5提供的功能。

- **自动装箱**：将基本类型直接赋值给对应的包装类。
- **自动拆箱**：将包装类对象直接赋值给基本类型。

### 应用场景
- 调用方法时，参数需要包装类型，可以直接传入基本类型。
- 进行集合操作时，可以将基本类型直接放入`List`、`Map`等集合。

---

## 1.10 如何对Integer和Double类型判断相等？
**参考答案**

`Integer`、`Double`不能直接进行比较，正确的比较方法：

- 不能使用`==`，因为它们是不同的数据类型。
- 不能通过字符串转换比较，因为浮点值带小数点，整数值不带。
- 不能使用`compareTo`进行比较，不同类型无法比较。

### 正确方法
- 将`Integer`、`Double`转换为相同的基本数据类型（如`double`），然后使用`==`进行比较。
```java
Integer intVal = 5;
Double doubleVal = 5.0;

if (intVal.doubleValue() == doubleVal) {
    System.out.println("相等");
}
```



## 1.11 int 和 Integer 有什么区别，二者在做 `==` 运算时会得到什么结果？
**参考答案**

- `int` 是基本数据类型，`Integer` 是 `int` 的包装类。
- 二者在做 `==` 运算时，`Integer` 会自动拆箱为 `int` 类型，然后再进行比较。
- 如果两个 `int` 值相等，则返回 `true`，否则返回 `false`。

---

## 1.12 说一说你对面向对象的理解
**参考答案**

面向对象是一种更优秀的程序设计方法，基本思想是使用 **类、对象、继承、封装、消息** 等基本概念进行程序设计。它从现实世界中客观存在的事物出发来构造软件系统，并在系统构造中尽可能运用人类的自然思维方式。

### 扩展阅读

- **结构化程序设计方法：**
  - 按功能分析系统需求，主要原则是 **自顶向下、逐步求精、模块化**。
  - 采用结构化分析方法进行需求分析，再使用结构化设计进行概要设计和详细设计，最后采用结构化编程实现系统。

- **结构化程序设计的局限性：**
  - 设计不够直观，与人类习惯思维不一致。
  - 适应性差，可扩展性不强，修改需求时需要自顶向下重新修改模块结构。

---

## 1.13 面向对象的三大特征是什么？
**参考答案**

面向对象的程序设计方法具有三个基本特征：**封装、继承、多态**。

- **封装：** 将对象的实现细节隐藏，通过一些公用方法暴露功能。
- **继承：** 子类继承父类后，子类作为一种特殊的父类，将直接获得父类的属性和方法。
- **多态：** 子类对象可以直接赋给父类变量，但运行时依然表现出子类的行为特征。

---

## 1.14 封装的目的是什么，为什么要有封装？
**参考答案**

封装是面向对象编程语言对客观世界的模拟，在客观世界里，对象的状态信息都被隐藏在对象内部，外界无法直接操作和修改。对一个类或对象实现良好的封装，可以实现以下目的：

- 隐藏类的实现细节；
- 让使用者只能通过事先预定的方法来访问数据，从而可以在该方法里加入控制逻辑，限制对成员变量的不合理访问；
- 可进行数据检查，从而有利于保证对象信息的完整性；
- 便于修改，提高代码的可维护性。

---

### 扩展阅读

为了实现良好的封装，需要从两个方面考虑：

1. 将对象的成员变量和实现细节隐藏起来，不允许外部直接访问；
2. 把方法暴露出来，让方法来控制对这些成员变量进行安全的访问和操作。

---

封装实际上有两个方面的含义：
- 把该隐藏的隐藏起来；
- 把该暴露的暴露出来。

这两个方面都需要通过使用 Java 提供的访问控制符来实现。

## 1.15 说一说你对多态的理解
**参考答案**

因为子类其实是一种特殊的父类，因此 Java 允许把一个子类对象直接赋给一个父类引用变量，无须任何类型转换，或者被称为**向上转型**，向上转型由系统自动完成。

当把一个子类对象直接赋给父类引用变量时，例如：

```java
BaseClass obj = new SubClass();
```

- `obj` 引用变量的**编译时类型**是 `BaseClass`，而**运行时类型**是 `SubClass`。
- 当运行时调用该引用变量的方法时，其方法行为总是表现出子类方法的行为特征，而不是父类方法的行为特征。
- 这种现象是：**相同类型的变量、调用同一个方法时呈现出多种不同的行为特征，这就是多态。**

---

### 扩展阅读

多态可以提高程序的**可扩展性**，在设计程序时让代码更加简洁而优雅。

---

### 示例

例如我要设计一个司机类，他可以开轿车、巴士、卡车等等，示例代码如下：

```java
class Driver {
    void drive(Car car) { ... }
    void drive(Bus bus) { ... }
    void drive(Truck truck) { ... }
}
```

在设计上述代码时，我已采用了**重载机制**，将方法名进行了统一。这样在进行调用时，无论要开什么交通工具，都是通过 `driver.drive(obj)` 这样的方式来调用，对调用者足够的友好。

---

### 问题

但对于程序的开发者来说，这显得繁琐，因为实际上这个司机可以驾驶更多的交通工具。当系统需要为这个司机增加车型时，开发者就需要相应的增加 `driver` 方法，类似的代码会堆积的越来越多，显得臃肿。

---

### 解决方案：使用多态

采用多态的方式来设计上述程序，就会变得简洁很多。我们可以为所有的交通工具定义一个父类 `Vehicle`，然后按照如下的方式设计 `drive` 方法。调用时，我们可以传入 `Vehicle` 类型的实例，也可以传入任意的 `Vehicle` 子类型的实例，对于调用者来说一样的方便，但对于开发者来说，代码却变得十分的简洁了。

```java
class Driver {
    void drive(Vehicle vehicle) { ... }
}
```

## 1.16 Java中的多态是怎么实现的？
**参考答案**

多态的实现离不开**继承**。在设计程序时，我们可以将参数的类型定义为父类型。在调用程序时，则可以根据实际情况，传入该父类型的某个子类型的实例，这样就实现了多态。

- **父类型**可以有三种形式：普通类、抽象类、接口。
- **子类型**需要根据自身的特征，重写父类的某些方法，或实现抽象类/接口的某些抽象方法。

---

## 1.17 Java为什么是单继承，为什么不能多继承？
**参考答案**

- Java 是**单继承**的，这意味着 Java 中一个类只能有一个直接的父类。
- Java 不支持**多继承**，即 Java 中一个类不能直接继承多个父类。

### 关键原因
- Java 在设计时借鉴了 C++ 的语法，而 C++ 是支持多继承的。
- Java 之所以摒弃了多继承的特性，是因为多继承容易产生混淆。例如：
    - 如果两个父类中包含相同的方法，子类在调用该方法或重写该方法时会产生**二义性**。

---

### 实现“多继承”的变通方法
Java 通过**接口**来实现类似于多继承的功能。
- **一个类可以实现多个接口**，从而达到某种程度上的多继承效果。
- 另外，Java 一个类只能有一个直接父类，但是却可以有任意多个间接父类，从而避免了多继承时产生的混淆。

---

## 1.18 说一说重写与重载的区别
**参考答案**

| 特性       | 重载（Overload）                  | 重写（Override）                   |
|----------|--------------------------|---------------------------|
| 发生位置    | 同一个类                  | 父类和子类                  |
| 方法签名    | 方法名相同，参数列表不同          | 方法名、参数列表相同            |
| 返回类型    | 无关                   | 子类返回类型 <= 父类返回类型 |
| 访问修饰符   | 无关                   | 子类的访问权限 >= 父类         |
| 关键字     | 不需要使用 `@Override`    | 需要使用 `@Override` 标注     |
| 目的       | 提供不同参数类型的多种实现    | 子类重写父类方法，提供不同实现   |

---

## 1.19 构造方法能不能重写？
**参考答案**

- **构造方法不能重写**。因为构造方法需要与类名保持一致，而重写的要求是子类方法与父类方法同名。
- 如果允许构造方法重写，那么子类中将会存在与类名不同的构造方法，这与构造方法的要求是矛盾的。

---

## 1.20 介绍一下Object类中的方法
**参考答案**

`Object` 类提供了以下几个常用方法：

- `Class<?> getClass()`：返回该对象的运行时类。
- `boolean equals(Object obj)`：判断指定对象与该对象是否相等。
- `int hashCode()`：返回该对象的 `hashCode` 值。默认情况下，`Object` 类的 `hashCode()` 方法根据该对象的地址计算，但很多类重写了 `hashCode()` 方法。
- `String toString()`：返回该对象的字符串表示。当程序使用 `System.out.println()` 输出一个对象时，系统会自动调用 `toString()` 方法。`Object` 类的 `toString()` 方法返回**运行时类名@十六进制 hashCode 值**格式的字符串，但很多类重写了 `toString()` 方法来返回更有意义的信息。

---

### 线程相关方法
- `void wait()`：让当前线程等待，直到被其他线程通知或超时。
- `void notify()`：唤醒一个正在等待的线程。
- `void notifyAll()`：唤醒所有正在等待的线程。

---

### `clone()` 方法
- `Object` 类提供了一个 `clone()` 方法，该方法用于创建一个对象的副本，并且副本与原对象完全隔离。
- 由于 `clone()` 方法使用了 `protected` 修饰，因此它只能被子类重写或调用。

---

### 扩展阅读
`Object` 类还提供了一个 `finalize()` 方法：

- 当系统中没有引用变量引用到该对象时，垃圾回收器调用此方法来清理该对象的资源。
- 垃圾回收器最多只会调用一个对象的 `finalize()` 方法一次。
- **注意：** `finalize()` 方法的调用时间和是否调用是不确定的，因此不要依赖 `finalize()` 方法来释放资源。从 JDK9 开始，该方法已被标记为不推荐使用。


## 1.21 说一说hashCode()和equals()的关系
**参考答案**

`hashCode()` 用于获取哈希码（散列码），`equals()` 用于比较两个对象是否相等。  
它们应遵守如下规定：  

- 如果两个对象相等，则它们必须有相同的哈希码。  
- 如果两个对象有相同的哈希码，则它们未必相等。

---

### 扩展阅读

在 Java 中，`Set` 接口代表无序的、元素不可重复的集合，`HashSet` 则是 `Set` 接口的典型实现。

- 当向 `HashSet` 中加入一个元素时，需要判断集合中是否已经包含该元素，从而避免重复存储。
- 由于这个判断非常频繁，为了提高效率，`HashSet` 通过获取对象的 `hashCode()` 和调用 `equals()` 方法来完成这个判断。  

`HashSet` 首先会调用对象的 `hashCode()` 方法获取其哈希码，并通过哈希码确定该对象在集合中的存放位置。  
- 如果该位置已经存储了一个对象，则 `HashSet` 会调用 `equals()` 对两个对象进行比较：  
  - 如果相等，则不会保存新加的对象；  
  - 如果不等，则使用链式结构在同一位置保存多个对象，将新加对象链接到原来的对象之后。

---

## 1.22 为什么要重写hashCode()和equals()？
**参考答案**

- `Object` 类提供的 `equals()` 方法默认是使用 `==` 进行比较的，也就是说只有两个对象是同一个对象时，才能返回 `true`。  
- 实际业务中，我们通常需要判断两个对象的**内容**是否相同，而不是判断它们是否为同一个对象。因此，`Object` 类中 `equals()` 方法的默认实现没有实际应用价值，需要进行重写。  

### 关键点
- 由于 `hashCode()` 与 `equals()` 具有联动关系（见 1.21），因此**重写 `equals()` 时，也需要重写 `hashCode()`**，以确保这两个方法遵循相关的约定。

---

## 1.23 ==和equals()有什么区别？
**参考答案**

### `==` 运算符
- **基本数据类型：** 比较两个数值是否相等。  
- **引用数据类型：** 比较两个对象的内存地址是否相同，即判断它们是否为同一个对象。

---

### `equals()` 方法
- **没有重写时：** `Object` 类默认实现使用 `==` 比较两个对象的内存地址。  
- **重写后：** 一般情况下，`equals()` 会根据对象的内容进行比较，如果内容相同，则返回 `true`，否则返回 `false`。

---

## 1.24 String类有哪些方法？
**参考答案**

`String` 类是 Java 最常用的 API，包含大量处理字符串的方法，常用的有：

- `char charAt(int index)`：返回指定索引处的字符。  
- `String substring(int beginIndex, int endIndex)`：从此字符串中截取出一部分子字符串。  
- `String[] split(String regex)`：按指定规则将字符串拆分成数组。  
- `String trim()`：删除字符串前后空格。  
- `int indexOf(String str)`：返回子串在此字符串首次出现的索引。  
- `int lastIndexOf(String str)`：返回子串在此字符串最后出现的索引。  
- `boolean startsWith(String prefix)`：判断字符串是否以指定前缀开头。  
- `boolean endsWith(String suffix)`：判断字符串是否以指定后缀结尾。  
- `String toUpperCase()`：将字符串转换为大写。  
- `String toLowerCase()`：将字符串转换为小写。  
- `String replaceFirst(String regex, String replacement)`：用指定字符串替换第一个匹配的子串。  
- `String replaceAll(String regex, String replacement)`：用指定字符串替换所有匹配的子串。

---

### 注意事项
- `String` 类的方法非常多，面试时不需要全部记住，只需说出常用的方法即可。  
- 建议挑选几个方法深入阅读源码，面试时可以重点讲解这些方法的实现。

---

## 1.25 String可以被继承吗？
**参考答案**

`String` 类由 `final` 修饰，所以不能被继承。

---

### 扩展阅读

在 Java 中，`String` 类被设计为**不可变类**，主要体现在它保存字符串的成员变量是 `final` 的。

- **Java 9 之前：** 字符串使用 `char[]` 数组来存储字符，即：  
```java
private final char[] value;
```

- **Java 9 之后：** 字符串改用 `byte[]` 数组来存储字符，即：  
```java
private final byte[] value;
```

---

### 设计String类为不可变类的原因
`String` 类之所以被设计为不可变类，主要是出于**安全性和性能**的考虑，可归纳为以下 4 点：

---

#### 1. 安全性
- `String` 被广泛应用于 Java 系统中，例如账号、密码、网络路径、文件路径等场景。  
- 如果字符串是可变的，就容易被篡改，这将导致安全隐患，比如 SQL 注入或访问危险文件等操作。

---

#### 2. 线程安全性
- 在多线程环境中，只有**不可变对象**才是线程安全的，可以在多个线程中共享数据。  
- 由于 `String` 是不可变的，当一个线程“修改”字符串的值时，会创建一个新的 `String` 对象，不会对其他线程的访问产生副作用，因此不需要任何同步操作。

---

#### 3. 散列集合的高效使用
- `String` 作为基础的数据结构，被大量应用在一些散列集合中，如 `HashMap` 和 `HashSet`。  
- 在散列集合中，元素的位置由 `hashCode()` 方法决定。  
- 由于 `String` 的 `hashCode` 属性不会改变，保证了元素的唯一性，使 `HashMap` 和 `HashSet` 等容器能够实现高效的缓存功能。  
- 因为 `String` 不可变，所以可以避免重复计算 `hashCode`，直接使用缓存的 `hashCode`，从而提高性能。

---

#### 4. 字符串常量池的意义
- 当字符串不可变时，**字符串常量池**才有意义。  
- 字符串常量池的存在可以减少创建相同字面量字符串的次数，让不同的引用指向池中的同一个字符串，从而节省运行时的堆内存。  
- 如果字符串是可变的，则字符串常量池将失去意义，同时 `String.intern()` 方法也会失效，每次创建新的字符串都需要在堆中重新开辟空间，占用更多内存。

---

### 为什么String类要用final修饰？
为了保证 `String` 类的不可变性，将其定义为 `final` 是非常必要的。

- 如果 `String` 没有被 `final` 修饰，则可能存在 `String` 的子类，这些子类可以**重写** `String` 类的方法，从而改变字符串的值。  
- 这种情况违背了 `String` 设计的初衷，因此 `String` 被 `final` 修饰，确保不会被继承。


## 1.26 说一说String和StringBuffer有什么区别
**参考答案**

- **String 类：**
  - `String` 是**不可变类**，一旦创建 `String` 对象后，其中包含的字符序列是不可改变的，直到对象被销毁。  
  - 例如：
```java
String str = "Hello";
str = str + " World";  // 创建了一个新的字符串对象
```
  - 每次对 `String` 进行修改时，都会生成一个新的 `String` 对象，并将引用指向新对象，原对象则会等待垃圾回收。

---

- **StringBuffer 类：**
  - `StringBuffer` 代表一个**可变的字符串**对象，可以通过 `append()`、`insert()`、`reverse()`、`setCharAt()`、`setLength()` 等方法修改字符序列。  
  - 例如：
```java
StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");  // 修改原来的字符串对象，不会创建新的对象
```
  - 通过 `StringBuffer` 生成最终想要的字符串后，可以调用 `toString()` 方法将其转换为 `String` 对象。

---

## 1.27 说一说StringBuffer和StringBuilder有什么区别
**参考答案**

- **相同点：**
  - `StringBuffer` 和 `StringBuilder` 都是**可变字符串类**，可以修改字符串对象的内容。  
  - 它们有共同的父类 `AbstractStringBuilder`，构造方法和成员方法也基本相同。  

---

- **不同点：**
| 特性               | StringBuffer       | StringBuilder       |
|------------------|------------------|--------------------|
| **线程安全性**       | 线程安全，适用于多线程环境 | 非线程安全，适用于单线程环境 |
| **性能**           | 性能较低            | 性能较高             |
| **推荐使用场景**     | 需要线程安全时使用    | 不需要线程安全时使用  |

---

- **示例：**
```java
// 使用 StringBuffer
StringBuffer sb = new StringBuffer("Hello");
sb.append(" World");

// 使用 StringBuilder
StringBuilder sbuilder = new StringBuilder("Hello");
sbuilder.append(" World");
```
- **建议：**  
  - 在单线程环境下，优先选择 `StringBuilder`，因为性能更高。  
  - 在多线程环境下，建议使用 `StringBuffer`，以确保线程安全。

---

## 1.28 使用字符串时，new 和 "" 推荐使用哪种方式？
**参考答案**

### 区别
1. **字符串直接量：**
```java
String str1 = "hello";
```
- 当 Java 程序直接使用 `"hello"` 字符串直接量时，JVM 会使用**常量池**来管理这个字符串。  
- 如果常量池中已存在 `"hello"`，则复用该字符串，避免创建新的对象。

---

2. **new String()：**
```java
String str2 = new String("hello");
```
- `new String("hello")` 会做两步操作：  
  - 首先，在**常量池**中存储 `"hello"`（如果常量池中已存在，则不会重复存储）。  
  - 然后，在**堆内存**中创建一个新的 `String` 对象，并将其数据指向常量池中的 `"hello"`。

---

### 性能比较
- 使用 `new` 关键字会创建一个新的字符串对象，增加内存开销。  
- 直接使用字符串直接量时，JVM 会复用常量池中的对象，内存占用更少。

---

### 结论
- **推荐：**  
  - 一般建议使用**字符串直接量**的方式来创建字符串。  
  - 只有在明确需要创建一个新对象的情况下，才使用 `new String()`。


## 1.29 说一说你对字符串拼接的理解
**参考答案**

拼接字符串有很多种方式，最常用的有 4 种，下面列举了这些方式及其适用场景：

---

- **`+` 运算符：**
  - 如果拼接的都是**字符串直接量**，适合使用 `+` 运算符拼接。
```java
String str = "Hello " + "World";
```

---

- **`StringBuilder`：**
  - 如果拼接的字符串中包含**变量**，且不要求线程安全，则适合使用 `StringBuilder`。
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");
```

---

- **`StringBuffer`：**
  - 如果拼接的字符串中包含**变量**，并且需要**线程安全**，则适合使用 `StringBuffer`。
```java
StringBuffer sbf = new StringBuffer("Hello");
sbf.append(" World");
```

---

- **`String` 的 `concat()` 方法：**
  - 如果只是对**两个字符串**进行拼接，并且包含变量，则适合使用 `concat()` 方法。
```java
String str1 = "Hello";
String str2 = str1.concat(" World");
```

---

### 扩展阅读

---

### 采用 `+` 运算符拼接字符串时：
- **字符串直接量拼接：**  
  - 如果拼接的都是字符串直接量，在**编译时**，编译器会将其直接优化为一个完整的字符串，这种情况下效率非常高。  
```java
String str = "Hello " + "World";  // 编译时优化为 "Hello World"
```
- **包含变量的字符串拼接：**  
  - 如果拼接的字符串中包含变量，编译器会使用 `StringBuilder` 进行优化，即自动创建 `StringBuilder` 实例并调用 `append()` 方法进行拼接。  
  - **注意：** 如果拼接操作在循环中进行，每次循环都会创建一个 `StringBuilder` 实例，这种情况下效率较低。  

---

### 采用 `StringBuilder`/`StringBuffer` 拼接字符串时：
- `StringBuilder` 和 `StringBuffer` 都有**字符串缓冲区**，在创建对象时分配默认容量为 16。  
- 当拼接的字符串长度超过缓冲区容量时，会触发**扩容机制**，即缓冲区加倍，影响拼接效率。  
- **优化建议：**  
  - 如果能够预估最终字符串的长度，可以在创建 `StringBuilder` 或 `StringBuffer` 时指定初始容量，避免频繁扩容。

---

### 采用 `String` 的 `concat()` 方法拼接字符串时：
- `concat()` 方法的拼接逻辑是：  
  - 创建一个足以容纳两个字符串的新字节数组。  
  - 将两个字符串的内容拷贝到该数组中。  
  - 最后，将数组转换为新的 `String` 对象。  
- **性能对比：**
  - `concat()` 的性能低于 `StringBuilder`，但在拼接**两个字符串**时，`concat()` 的效率高于 `StringBuilder`，且代码更简洁。

---

## 1.30 两个字符串相加的底层是如何实现的？
**参考答案**

- **拼接字符串直接量：**  
  - 如果拼接的都是**字符串直接量**，在**编译时**，编译器会直接优化为一个完整的字符串，与直接写一个完整字符串效果一样。  
```java
String str = "Hello " + "World";  // 编译时优化为 "Hello World"
```

- **拼接包含变量的字符串：**  
  - 如果拼接的字符串中**包含变量**，编译器会使用 `StringBuilder` 进行优化。  
  - `StringBuilder` 会创建一个新的对象，并调用 `append()` 方法将这些字符串拼接在一起。  
```java
String str1 = "Hello";
String str2 = "World";
String str = str1 + str2;  // 等价于 new StringBuilder(str1).append(str2).toString();
```

---

## 1.31 String a = "abc"; 说一下这个过程会创建什么，放在哪里？
**参考答案**

JVM 会使用**常量池**来管理字符串直接量。  
在执行 `String a = "abc";` 这句话时：  

1. JVM 会先检查**常量池**中是否已经存有 `"abc"`：  
   - 如果不存在，则将 `"abc"` 存入常量池中；  
   - 如果存在，则直接复用常量池中的字符串。  
2. 然后，将 `a` 引用指向常量池中的 `"abc"`。

---

## 1.32 new String("abc") 是去了哪里，仅仅是在堆里面吗？
**参考答案**

在执行 `new String("abc")` 时：  

1. JVM 会先检查**常量池**中是否已存储 `"abc"`，如果没有，则将 `"abc"` 存入常量池；  
2. 然后，在**堆内存**中创建一个新的 `String` 对象，并将其数据指向常量池中的 `"abc"`。  

---

## 1.33 接口和抽象类有什么区别？
**参考答案**

### 1. 设计目的的区别
- **接口：**  
  - 体现的是一种**规范**，规定实现者必须向外提供哪些服务。  
  - 接口规定了调用者可以调用哪些服务，以及如何调用这些服务。  

- **抽象类：**  
  - 体现的是一种**模板式设计**，作为多个子类的抽象父类，定义系统的部分功能，但仍需要子类来进一步完善。  

---

### 2. 使用方式的区别
| 特性               | 接口                        | 抽象类                     |
|------------------|-------------------------|--------------------------|
| **包含内容**       | 只能包含抽象方法、静态方法、默认方法、私有方法 | 可以包含普通方法和抽象方法 |
| **成员变量**       | 只能定义静态常量             | 可以定义普通成员变量和静态常量 |
| **构造器**         | 不能包含构造器               | 可以包含构造器              |
| **初始化块**       | 不包含初始化块               | 可以包含初始化块            |
| **继承方式**       | 一个类可以实现多个接口         | 一个类只能继承一个抽象类      |

---

### 3. 继承机制的区别
- **接口：**  
  - 一个类可以实现多个接口。  
  - 通过实现多个接口，可以弥补 Java 单继承的不足。  

- **抽象类：**  
  - 一个类最多只能有一个直接父类，包括抽象类。  

---

### 扩展阅读
- **接口和抽象类的共同点：**
  - 都不能被实例化，位于继承树的顶端，用于被其他类实现或继承。  
  - 都可以包含抽象方法，实现接口或继承抽象类的子类必须实现这些抽象方法。  

---

## 1.34 接口中可以有构造函数吗？
**参考答案**

由于接口定义的是一种**规范**，因此接口**不能包含构造器**和**初始化块**。  
- **接口中可以包含：**  
  - 成员变量（只能是静态常量）；  
  - 方法（抽象方法、类方法、默认方法或私有方法）；  
  - 内部类（包括内部接口、枚举）。  

---

## 1.35 谈谈你对面向接口编程的理解
**参考答案**

**面向接口编程（Interface-Oriented Programming, IOP）** 体现了一种**规范与实现分离**的设计哲学：  
- 通过使用接口，可以降低程序各模块之间的耦合，提高系统的可扩展性和可维护性。  

---

### 关键点：
- **降低耦合度：**  
  - 通过接口定义规范，使模块之间依赖于抽象接口，而不是具体实现类，从而降低耦合度。  

- **提高系统灵活性：**  
  - 通过面向接口编程，可以随时更换实现类，而不需要修改调用方的代码，从而提高系统的灵活性。  

- **增强可维护性：**  
  - 当系统发生变化时，只需要修改具体的实现类，无需修改接口或调用方，提高系统的维护性。  

---

## 1.36 遇到过异常吗，如何处理？
**参考答案**

在 Java 中，可以按照如下三个步骤处理异常：

---

### 1. 捕获异常
- 将业务代码包裹在 `try` 块内部，当业务代码发生异常时，系统会创建一个异常对象。  
- JVM 会在 `try` 块之后寻找可以处理该异常的 `catch` 块，并将异常对象交给这个 `catch` 块处理。
```java
try {
    // 业务代码
} catch (Exception e) {
    // 处理异常
}
```

---

### 2. 处理异常
- 在 `catch` 块中处理异常时，应**记录日志**，便于以后追溯异常。  
- 根据异常类型，结合当前的业务情况进行相应的处理，例如：  
  - 赋予变量默认值；  
  - 返回空值；  
  - 抛出新的业务异常交给调用者处理等。

---

### 3. 回收资源
- 如果业务代码打开了某个资源（如数据库连接、网络连接、磁盘文件等），需要在业务代码执行完毕后关闭该资源。  
- **无论是否发生异常**，都要尝试关闭资源，可将关闭资源的代码写在 `finally` 块中。
```java
finally {
    // 关闭资源
}
```

---

## 1.37 说一说Java的异常机制
**参考答案**

---

### 1. 异常处理
- 在 Java 中，处理异常的语句由 `try`、`catch`、`finally` 组成。  
- **`try` 块：** 用于包裹业务代码；  
- **`catch` 块：** 捕获并处理特定类型的异常；  
- **`finally` 块：** 用于回收资源，无论是否发生异常，`finally` 块都会执行。  
```java
try {
    // 业务代码
} catch (Exception e) {
    // 处理异常
} finally {
    // 回收资源
}
```

---

### 2. 抛出异常
- **系统自动抛出异常：**  
  - 当程序出现错误时，系统会自动抛出异常。  

- **手动抛出异常：**  
  - 使用 `throw` 关键字主动抛出异常：  
```java
if (someErrorCondition) {
    throw new IllegalArgumentException("参数不合法");
}
```

- **声明抛出异常：**  
  - 如果方法无法处理异常，可以在方法签名上使用 `throws` 关键字声明抛出异常：  
```java
public void someMethod() throws IOException {
    // 可能抛出 IOException
}
```

---

### 3. 异常跟踪栈
- **异常传播机制：**  
  - 异常发生后，会在**方法调用栈**中逆向传播。  
  - 异常从发生异常的方法向外传播，依次传给调用者，直到 `main()` 方法。  
  - 如果 `main()` 方法中没有捕获该异常，JVM 会终止程序并打印异常跟踪栈信息。

---

## 1.38 请介绍Java的异常接口
**参考答案**

---

### 1. 异常的顶层父类
- `Throwable` 是异常的顶层父类，代表所有的非正常情况。  
- 它有两个直接子类：
  - **`Error`：** 表示严重的系统级错误，例如 JVM 崩溃、内存溢出等，通常无法恢复；  
  - **`Exception`：** 表示程序本身可以捕获和处理的异常。

---

### 2. `Error` 类
- `Error` 代表系统级错误，通常应用程序无法处理这些错误。  
- **特点：**
  - 例如：`OutOfMemoryError`、`StackOverflowError` 等；  
  - 无需在 `throws` 子句中声明，不建议捕获 `Error` 对象。

---

### 3. `Exception` 类
- `Exception` 代表可以处理的异常，分为**两大类：**
  - **Checked 异常：** 继承自 `Exception`，必须显式声明或捕获；  
  - **Runtime 异常：** 继承自 `RuntimeException`，不需要显式声明，系统自动抛出。

---

### 4. Checked 异常和 Runtime 异常的区别
| 特性            | Checked 异常       | Runtime 异常        |
|---------------|-----------------|------------------|
| **父类**        | `Exception`       | `RuntimeException` |
| **是否必须处理** | 必须显式声明或捕获  | 不需要显式声明       |
| **典型示例**     | `IOException`      | `NullPointerException` |

---

## 1.39 finally是无条件执行的吗？
**参考答案**

---

### 1. `finally` 语句块的特点
- **`finally` 块：**  
  - 无论 `try` 块是否抛出异常，`finally` 块的代码都会执行。  
  - 即使在 `try` 块或 `catch` 块中执行了 `return` 语句，`finally` 块也会执行。

---

### 2. 特殊情况
- **注意：**  
  - 如果在 `try` 或 `catch` 块中使用 `System.exit(1);` 终止 JVM，则 `finally` 块不会执行。  
  - 但这种情况在实际开发中极少发生，因此 `finally` 块通常被视为**无条件执行**。

---

```java
try {
    System.out.println("try block");
    return;
} catch (Exception e) {
    System.out.println("catch block");
} finally {
    System.out.println("finally block");  // 仍然执行
}
```

---

## 1.40 在finally中return会发生什么？
**参考答案**

---

### 1. `finally` 中的 `return` 的特殊性
- **通常情况下：**  
  - 在 `try` 或 `catch` 块中遇到 `return` 或 `throw` 语句时，方法会立即结束。  
  - 但在 `return` 或 `throw` 语句执行之前，系统会先检查是否存在 `finally` 块，并执行 `finally` 块的内容。  

---

### 2. `finally` 中的 `return` 会覆盖之前的 `return`
- 如果在 `finally` 块中使用了 `return` 或 `throw` 语句，那么 `finally` 块的返回值会覆盖 `try` 和 `catch` 块中的返回值。
```java
public int test() {
    try {
        return 1;
    } catch (Exception e) {
        return 2;
    } finally {
        return 3;  // 覆盖了之前的返回值
    }
}
```
- **输出结果：**
```
3
```

---

### 3. **建议：** 
- 通常不建议在 `finally` 块中使用 `return` 或 `throw` 语句，以免影响 `try` 和 `catch` 块的正常返回。


## 1.41 说一说你对static关键字的理解
**参考答案**

---

在 Java 类里只能包含以下 5 种成员：  

- 成员变量  
- 方法  
- 构造器  
- 初始化块  
- 内部类（包括接口、枚举）

---

### 1. static 关键字的作用
- `static` 可以修饰成员变量、方法、初始化块、内部类（包括接口、枚举）。  
- **static 修饰的成员是类成员，属于整个类，而不属于单个对象。**  

---

### 2. static 的重要规则
- 类成员（包括变量、方法、初始化块、内部类、枚举）**不能访问实例成员**。
- 因为类成员属于类，其作用域比实例成员更大，实例成员尚未初始化时，类成员已初始化，因此访问会引起错误。  

---

## 1.42 static修饰的类能不能被继承？
**参考答案**

---

- `static` 修饰的类**可以被继承**。

---

### 扩展阅读

---

#### 1. 静态内部类
- `static` 修饰内部类时，该类属于**外部类本身**，而不属于外部类的某个对象。  
- 静态内部类也称为**类内部类**或**静态嵌套类**。  

---

#### 2. 静态内部类的规则
- 静态内部类可以包含**静态成员**和**非静态成员**。  
- 静态内部类**不能访问**外部类的实例成员，只能访问外部类的静态成员。  
- 外部类的所有方法、初始化块都可以访问静态内部类。  
- 外部类的外部也可以实例化静态内部类，语法如下：
```java
外部类.内部类 变量名 = new 外部类.内部类();
```

---

## 1.43 static和final有什么区别？
**参考答案**

---

### 1. static 的特征
- `static` 关键字可以修饰：**成员变量、成员方法、初始化块、内部类。**  

---

#### 2. static 的特征表现
- **类变量：**  
  - 被 `static` 修饰的成员变量叫**类变量（静态变量）**。  
  - 类变量属于类，存储在方法区，不随对象存储在堆中，可通过类名或对象名访问，建议使用类名访问。
- **类方法：**  
  - 被 `static` 修饰的方法叫**类方法（静态方法）**。  
  - 类方法属于类，可以通过类名或对象名访问，建议通过类名访问。
- **静态块：**  
  - 被 `static` 修饰的初始化块叫**静态初始化块**。  
  - 静态块在类加载时被调用一次，不会被多次调用。
- **静态内部类：**  
  - 被 `static` 修饰的内部类叫**静态内部类**。  
  - 静态内部类可以包含静态和非静态成员，但不能访问外部类的实例成员，只能访问外部类的静态成员。

---

### 3. final 的特征
- `final` 关键字可以修饰：**类、方法、变量。**  

---

#### 4. final 的特征表现
- **final 类：**  
  - `final` 修饰的类**不可以被继承**。  
- **final 方法：**  
  - `final` 修饰的方法**不可以被重写**。  
- **final 变量：**  
  - `final` 修饰的变量，在获得初始值后，**不可再修改**。  

---

## 1.44 说一说你对泛型的理解
**参考答案**

---

### 1. Java 集合的缺陷
- Java 集合将对象放入集合后，集合会**忘记**对象的数据类型；  
- 取出对象时，集合元素的类型变成 `Object`，需要进行**强制类型转换**。  

---

### 2. 泛型的引入
- 从 Java 5 开始，引入了**参数化类型**的概念，即**泛型（Generic）**。  
- 允许在创建集合时指定集合元素的类型，例如：
```java
List<String> list = new ArrayList<>();
```
- `list` 只能保存 `String` 类型的对象，其他类型无法插入。

---

### 3. 泛型的优点
- **避免类型错误：** 防止将不正确的对象放入集合。  
- **消除强制类型转换：** 取出集合元素时，不需要强制类型转换。  

---

## 1.45 介绍一下泛型擦除
**参考答案**

---

### 1. 泛型擦除的概念
- 在严格的泛型代码中，带有泛型声明的类**必须带着类型参数**。  
- 但为了与旧的 Java 代码保持一致，也允许在使用泛型类时**不指定实际类型**。  

---

### 2. 泛型擦除的表现
- **泛型信息擦除：**  
  - 当将带泛型的对象赋给没有泛型信息的变量时，所有泛型信息都会被擦除。  
- **默认上限：**  
  - 若不指定泛型类型，泛型参数的默认上限为 `Object`。

---

### 3. 代码示例
```java
List<String> list1 = new ArrayList<>();
List list2 = list1;  // 泛型擦除，list2 的类型信息被擦除
```
- `list2` 的元素类型会变成 `Object`。

---

## 1.46 List<? super T> 和 List<? extends T> 有什么区别？
**参考答案**

---

### 1. 通配符 `?` 的概念
- `?` 表示**未知类型**。  
- **`List<?>`** 表示各种泛型 `List` 的父类。  

---

### 2. `? super T` 和 `? extends T` 的区别
| 特性                 | `List<? super T>`          | `List<? extends T>`       |
|--------------------|------------------------|------------------------|
| **含义**            | T 的父类                  | T 的子类                  |
| **添加元素**        | 只能添加 T 或 T 的子类元素 | 不允许添加任何元素         |
| **获取元素**        | 获取的元素为 `Object`       | 获取的元素类型为 `T` 或子类 |
| **使用场景**        | 用于写入集合              | 用于读取集合              |

---

## 1.47 说一说你对Java反射机制的理解
**参考答案**

---

### 1. Java 的两种类型
- **编译时类型：** 由变量声明时的类型决定。  
- **运行时类型：** 由对象的实际类型决定。  

---

### 2. 反射机制的引入
- **运行时类型判断：** 当程序在运行时接收到 `Object` 类型的对象，但需要调用它的特定方法时，可以使用**反射机制**。  

---

### 3. 反射机制的作用
- **获取类的 `Class` 对象：**
```java
Class<?> clazz = Class.forName("com.example.Person");
```
- **创建类的实例：**
```java
Object obj = clazz.newInstance();
```
- **访问类的成员变量和方法：**
```java
Field field = clazz.getDeclaredField("name");
Method method = clazz.getMethod("getName");
```

---

## 1.48 Java反射在实际项目中有哪些应用场景？
**参考答案**

---

### 1. JDBC 中加载数据库驱动
- 使用反射机制动态加载数据库驱动。
```java
Class.forName("com.mysql.cj.jdbc.Driver");
```

---

### 2. 框架中解析 XML/注解
- 解析配置文件或注解，并通过反射创建对象。  

---

### 3. AOP（面向切面编程）
- 在运行时创建目标对象的代理类，需要使用反射实现。

---

## 1.49 说一说Java的四种引用方式
**参考答案**

---

### 1. Java 的四种引用
| 引用类型   | 特点                                  | 应用场景                  |
|----------|-----------------------------------|----------------------|
| **强引用** | 普通的对象引用，不会被 GC 回收            | 常规对象使用               |
| **软引用** | 只有在内存不足时才会回收                   | 缓存、内存敏感的数据          |
| **弱引用** | 下一次 GC 时一定会被回收                  | 缓存、映射等需要快速释放的场景 |
| **虚引用** | 随时可能被 GC 回收，不会保存对象的引用         | 跟踪对象被 GC 回收的状态      |

---

### 2. 强引用
- 通过 `new` 创建的对象就是强引用，永远不会被 GC 自动回收。
```java
String str = new String("hello");
```

---

### 3. 软引用
- 使用 `SoftReference` 创建，只有在内存不足时才会回收。
```java
SoftReference<String> softRef = new SoftReference<>(new String("hello"));
```

---

### 4. 弱引用
- 使用 `WeakReference` 创建，在 GC 时会被立即回收。
```java
WeakReference<String> weakRef = new WeakReference<>(new String("hello"));
```

---

### 5. 虚引用
- 使用 `PhantomReference` 创建，仅用于追踪对象被 GC 的状态。
```java
PhantomReference<String> phantomRef = new PhantomReference<>(new String("hello"), new ReferenceQueue<>());
```


## 2. 集合类

### 2.1 Java中有哪些容器（集合类）？
**参考答案**

Java中的集合类主要由 `Collection` 和 `Map` 这两个接口派生而出，其中 `Collection` 接口又派生出三个子接口，分别是：`Set`、`List`、`Queue`。所有的 Java 集合类，都是 `Set`、`List`、`Queue`、`Map` 这四个接口的实现类。

这四个接口将集合分成了四大类，其中：

- **Set**：代表**无序的、元素不可重复**的集合；
- **List**：代表**有序的、元素可以重复**的集合；
- **Queue**：代表**先进先出（FIFO）**的队列；
- **Map**：代表**具有映射关系（key-value）**的集合。

---

这些接口拥有众多的实现类，其中最常用的实现类有：

- `HashSet`
- `TreeSet`
- `ArrayList`
- `LinkedList`
- `ArrayDeque`
- `HashMap`
- `TreeMap`

---

### 扩展阅读

#### Collection体系的继承树：
![Collection](/image/collections.jpg)

#### Map体系的继承树：
![Map](/image/map.jpg)

> 💡 注：  
> - **紫色框体**代表接口，其中**加粗**的是代表四类集合的接口；  
> - **蓝色框体**代表实现类，其中**有阴影**的是常用实现类。


## 2.2 Java中的容器，线程安全和线程不安全的分别有哪些？
**参考答案**

`java.util` 包下的集合类大部分都是**线程不安全的**，例如：

- `HashSet`
- `TreeSet`
- `ArrayList`
- `LinkedList`
- `ArrayDeque`
- `HashMap`
- `TreeMap`

这些集合类的优点是**性能好**，但不适用于多线程环境。如果需要线程安全的集合类，可以使用 `Collections` 工具类提供的 `synchronizedXxx()` 方法，将它们包装成线程安全的集合。

---

`java.util` 包下也有一些**线程安全的**集合类，例如：

- `Vector`
- `Hashtable`

这两个类虽然是线程安全的，但属于**较老的API**，**性能较差**。所以，即使需要线程安全，**不推荐直接使用**这些类，而是推荐使用包装的方式或 `java.util.concurrent` 包下的集合类。

---

### 从 Java 5 开始，Java 在 `java.util.concurrent` 包下提供了大量支持高效并发访问的集合类：

#### ① 以 `Concurrent` 开头的集合类：

- 支持**多个线程并发写入访问**
- 写操作是**线程安全的**
- 读操作**无需加锁**
- 内部使用**复杂算法**避免锁住整个集合，提高并发性能

#### ② 以 `CopyOnWrite` 开头的集合类：

- 写操作会**复制一份新的数组**
- 读操作**无需加锁**
- 写操作是线程安全的
- 适用于**读多写少**的场景

---

### 扩展阅读

> `java.util.concurrent` 包下线程安全集合类的体系结构：  
![Map](/image/concurrent.jpg)

---

## 2.3 Map接口有哪些实现类？
**参考答案**

`Map` 接口常用的实现类有：

- `HashMap`
- `LinkedHashMap`
- `TreeMap`
- `ConcurrentHashMap`

### 使用场景建议：

- **不需要排序：**
  - 首选 `HashMap`，性能最好
  - 若需线程安全：使用 `ConcurrentHashMap`
    - `ConcurrentHashMap` 性能优于 `Hashtable`，因为它使用**分段锁/CAS机制**，而 `Hashtable` 的 `put` 和 `get` 都加锁

- **需要排序：**
  - 按**插入顺序排序**：使用 `LinkedHashMap`
  - 按**自然顺序或自定义顺序排序**：使用 `TreeMap`
  - 若需线程安全：可通过 `Collections.synchronizedMap()` 包装为线程安全版本


## 2.4 描述一下Map put的过程
**参考答案**

`HashMap` 是最经典的 `Map` 实现，下面以它为例来说明 `put` 的过程：

---

### 🛠️ **1. 首次扩容：**

- 判断数组是否为空（即 table == null）；
- 如果为空，则调用 `resize()` 方法进行**第一次扩容**。

---

### 📍 **2. 计算索引：**

- 使用键的 `hashCode()`，经过扰动函数处理后计算出键的哈希值；
- 根据哈希值与数组长度计算出**该键值对应在数组中的索引**。

---

### 📥 **3. 插入数据：**

根据索引位置的情况有以下几种处理方式：

- **如果当前位置为空**：  
  直接在该位置插入节点。

- **如果当前位置不为空且 key 已存在**：  
  覆盖旧值（即更新 value）。

- **如果当前位置不为空且 key 不存在**：  
  将新节点挂到链表或红黑树的末尾。

- **如果链表长度达到 8 且数组长度 >= 64**：  
  将链表**转换为红黑树**以提高查找性能。

---

### 🚀 **4. 再次扩容：**

- 如果当前元素个数（`size`）**超过 threshold**（默认是数组长度的 0.75 倍），
  则会触发 `resize()` 方法进行**数组扩容**，容量变为原来的 2 倍。

---

### 📚 **扩展阅读**

![Map](/image/Mapput.png)


## 2.5 如何得到一个线程安全的Map？
**参考答案**

获取线程安全的 `Map` 有以下几种方式：

- 使用 `Collections` 工具类的 `synchronizedMap()` 方法，将线程不安全的 `Map` 包装成线程安全的：
  ```java
  Map<K, V> syncMap = Collections.synchronizedMap(new HashMap<>());
  ```

- 使用 `java.util.concurrent` 包下的并发类，例如：
  ```java
  Map<K, V> concurrentMap = new ConcurrentHashMap<>();
  ```

- ❗ 不建议使用 `Hashtable`，尽管它是线程安全的，但性能较差。

---

## 2.6 HashMap有什么特点？
**参考答案**

- `HashMap` 是**线程不安全**的；
- `HashMap` 允许 `null` 作为 **key** 和 **value**：
  - 最多只能有一个 `null` key；
  - 可以有多个 `null` value。

---

## 2.7 JDK7和JDK8中的HashMap有什么区别？
**参考答案**

### JDK7 中的 HashMap：

- 基于 **数组 + 链表** 实现；
- 底层使用 `Entry[]` 数组存储数据；
- 当多个键的哈希值相同（发生哈希冲突）时，将键值对以链表的形式存储；
- **缺点**：当哈希冲突严重时，链表过长会导致查找效率低，时间复杂度为 **O(N)**。

### JDK8 中的 HashMap：

- 基于 **数组 + 链表 + 红黑树** 实现；
- 底层使用 `Node[]` 数组代替 `Entry[]`；
- 当链表长度 ≥ 8 且数组长度 ≥ 64 时，链表会转换为红黑树；
- 红黑树查找效率为 **O(logN)**，显著提高了性能。

---

## 2.8 介绍一下HashMap底层的实现原理
**参考答案**

### 💾 存储过程（put）：

- 将 `K/V` 传给 `put()` 方法；
- 调用 `K.hashCode()` 计算出 hash 值；
- 根据 hash 定位到桶（bucket）的位置；
- 判断当前位置是否为空：
  - 如果为空：直接插入；
  - 如果非空：
    - 若 key 已存在：更新 value；
    - 若 key 不存在：链表或红黑树中插入新节点；
- 若 size > threshold（容量 × 加载因子），触发 **resize（扩容）**。

### 🔍 获取过程（get）：

- 将 key 传入 `get()`；
- 使用 `hashCode()` 计算 hash 定位 bucket；
- 在 bucket 中查找节点，通过 `equals()` 比较 key 是否匹配，找到则返回对应 value。

### 💥 碰撞处理：

- 使用**链表法**解决 hash 冲突；
- 在 Java 8 中，链表长度 ≥ 8 会转为红黑树，以提高查找效率；
- 转树要求数组长度 ≥ 64。

---

## 2.9 介绍一下 HashMap 的扩容机制
**参考答案**

- HashMap 的 **数组初始容量为 16**，且容量总是 **2 的幂次方**。
  - ✅ 这样设计的好处是可以使用位运算代替取模运算，从而提高性能（据说可提升 5~8 倍）。

---

### 📊 扩容的触发条件

- HashMap 是否需要扩容，是通过**负载因子（Load Factor）**判断的。
- 默认负载因子为 **0.75**，即：
  ```text
  当元素个数 ≥ 当前数组容量 × 0.75 时，触发扩容。
  ```
- 负载因子可以通过构造函数自定义：
  - **较大负载因子**（如 > 1）：减少扩容次数，节省内存但降低性能；
  - **较小负载因子**：提升性能但增加内存开销。

---

### 🧱 碰撞解决与结构转换

- HashMap 使用**单向链表**解决哈希碰撞。
- 当**链表长度 ≥ 8**，会尝试将链表转换为**红黑树**以提高查找效率；
- 当**链表长度 ≤ 6** 且结构为红黑树时，会将其转换回链表；
- ❗ 但在转换为红黑树之前，还要满足数组容量 **≥ 64** 的条件：
  - 如果数组未达到 64，则优先 **扩容** 而不是转换为红黑树。

---

### 🧠 扩容原理详解

- 假设当前数组容量为 `n`，扩容后变为 `2n`；
- 原有的哈希值不需要重新计算，只需判断新增的高位 bit 是 **0 或 1**；
  - 若是 **0**，则新的索引和旧索引一致；
  - 若是 **1**，则新的索引为 `原索引 + oldCap`。

这是一种非常巧妙的设计，带来了两大优势：

1. **避免重新计算 hash**；
2. **将碰撞节点更均匀地分散到新数组中**，提升性能。

---

### 📚 扩展阅读

- **示例**：从容量 16 扩容为 32 时的变化
![Map](/image/hashmap1.png)

因此元素在重新计算hash之后，因为n变为2倍，那么n-1的mask范围在高位多1bit(红色)，因此新的index就会发生这样的变化：

![Map](/image/hashmap2.png)

因此，我们在扩充HashMap的时候，不需要重新计算hash，只需要看看原来的hash值新增的那个bit是1还是0就好了，是0的话索引没变，是1的话索引变成“原索引+oldCap”。可以看看下图为16扩充为32的resize示意图：

![Map](/image/hashmap3.png)

这个设计确实非常的巧妙，既省去了重新计算hash值的时间，而且同时，由于新增的1bit是0还是1可以认为是随机的，因此resize的过程，均匀的把之前的冲突的节点分散到新的bucket了。


## 2.10 HashMap 中的循环链表是如何产生的？

**参考答案**

在多线程的情况下，当重新调整 HashMap 大小时，可能发生条件竞争。如果两个线程同时检测到需要 resize，就可能同时进行扩容。在扩容过程中，链表中的元素在移动时会被插入到新 bucket 的头部（而不是尾部），是为了避免尾部遍历。然而如果操作被打断并交错执行，就可能出现链表反转并自我引用，最终导致**死循环**。

---

## 2.11 HashMap 为什么用红黑树而不用 B 树？

**参考答案**

B/B+ 树更适合用于外存，如数据库索引，属于磁盘友好型数据结构。

而 HashMap 的设计基于数组 + 链表结构，为了优化链表查找效率，使用红黑树替换长链表。在内存中，**红黑树比 B 树更适合**，因为数据量较小时，B 树节点未分裂，可能导致效率退化成链表遍历。

---

## 2.12 HashMap 为什么线程不安全？

**参考答案**

在并发情况下同时执行 `put()` 操作，可能会引起链表插入顺序反转，甚至**形成循环链表**，从而引发**死循环**。

---

## 2.13 HashMap 如何实现线程安全？

**参考答案**

- ✅ 使用 `Hashtable` 类（已过时，性能差）；
- ✅ 使用 `ConcurrentHashMap`（推荐）；
- ✅ 使用 `Collections.synchronizedMap()` 对 HashMap 进行包装。

---

## 2.14 HashMap 是如何解决哈希冲突的？

**参考答案**

HashMap 采用了**链表 + 红黑树**结构：

- 默认通过链表解决冲突；
- 当链表长度超过阈值（默认 8）并且桶数组大小 ≥ 64 时，转为红黑树；
- 当树节点数少于阈值（默认 6）时，又会转换为链表。

---

## 2.15 HashMap 和 HashTable 的区别？

**参考答案**

| 特性            | HashMap                          | Hashtable                      |
|-----------------|----------------------------------|--------------------------------|
| 线程安全        | ❌ 非线程安全                    | ✅ 线程安全                     |
| null 键/值支持   | ✅ 支持 null 作为 key 或 value   | ❌ 不支持 null 作为 key 或 value |
| 性能            | 高（适用于单线程）              | 较低（使用 synchronized）       |
| 设计年代        | JDK 1.2 后的新类                | 早期类（不符合命名规范）        |

**扩展阅读**

- `Hashtable` 命名不规范（应该是 `HashTable`）；
- 避免使用 `Hashtable`，推荐使用 `ConcurrentHashMap` 或包装后的 `HashMap`。

---

## 2.16 HashMap 与 ConcurrentHashMap 有什么区别？

**参考答案**

| 特性              | HashMap                        | ConcurrentHashMap                            |
|-------------------|--------------------------------|-----------------------------------------------|
| 线程安全          | ❌ 非线程安全                  | ✅ 线程安全（高性能）                         |
| 并发风险          | 可能产生死循环，数据不一致     | 无需全局锁，避免死锁，支持高并发             |
| 同步机制          | 无或通过包装实现（synchronized） | 分段锁（JDK7）或 CAS + synchronized（JDK8） |
| 推荐使用场景      | 单线程环境                    | 多线程并发读写环境                            |

**说明**

- `HashMap` 不适用于并发；
- `ConcurrentHashMap` 设计精巧，通过降低锁粒度、分段同步、CAS 操作等机制提升性能；
- 检索操作在 `ConcurrentHashMap` 中通常是无锁的。


## 2.17 介绍一下 ConcurrentHashMap 是怎么实现的？

**参考答案**

### JDK 1.7 中的实现：

- `ConcurrentHashMap` 由 **Segment** 数据结构和 **HashEntry[]** 构成。
- 使用 **分段锁**（Segment 继承自 `ReentrantLock`）保证线程安全。
- 整体结构是：
  ```
  ConcurrentHashMap
      └─ Segment[]
            └─ HashEntry[]
  ```
- 每个 Segment 管理一部分数据，相当于多个小型的 `HashMap`，提升并发性能。

![Map](/image/concurrenthashmap1.png)

---

### JDK 1.8 中的实现：

- 弃用了 Segment，结构变为：
  ```
  Node[] + 链表 + 红黑树
  ```
- 并发控制采用：
  - `synchronized`（加锁粒度小）
  - `CAS`（无锁优化）
- 实际表现为一个 **线程安全、性能优化后的 HashMap**。

![Map](/image/concurrenthashmap2.png)
---

## 2.18 ConcurrentHashMap 是怎么分段分组的？

**参考答案**

### get 操作：

- 执行一次 hash，然后定位到某个 Segment，再 hash 找到 Node。
- 全过程基本 **无需加锁**，依赖于 `volatile` 的内存可见性。
- 如果读到 null，则会 **加锁重读**。

---

### put 操作流程：

1. 判断是否需要扩容；
2. 定位 Segment，若为 null 则通过 CAS 初始化；
3. 再次 hash 定位 Node；
4. 插入新数据时：
   - 尝试获取锁（`tryLock()`）；
   - 成功则插入；
   - 若失败，则自旋等待；
   - 超过阈值后挂起，等待唤醒。

---

## 2.19 说一说你对 LinkedHashMap 的理解

**参考答案**

- `LinkedHashMap` 是基于 `HashMap` 的子类。
- 使用 **双向链表** 维护键值对的插入顺序（按 key 顺序）。
- 优点：
  - 相比 `HashMap`，能保持遍历顺序；
  - 相比 `TreeMap`，性能更好；
- 缺点：
  - 需要维护链表，**性能略低于 HashMap**；
  - 但迭代性能更优。

---

## 2.20 请介绍 LinkedHashMap 的底层原理

**参考答案**

- `LinkedHashMap` 继承自 `HashMap`；
- 除了 HashMap 的数组 + 链表结构外，额外维护了 **一个双向链表**；
- 每个节点除了 `key`, `value`, `next`，还包含：
  - `before`（前驱节点）
  - `after`（后继节点）

**工作原理图示：**

```
head <-> node1 <-> node2 <-> node3 <-> ... <-> tail
```

- 新节点会追加在 tail 节点之后；
- 插入顺序和遍历顺序始终一致；
- 重写部分方法用于链表维护，其余功能继承自 `HashMap`。

## 2.21 请介绍 TreeMap 的底层原理

**参考答案：**

TreeMap 基于红黑树（Red-Black Tree）实现。映射根据其键的自然顺序进行排序，或者根据创建映射时提供的 Comparator 进行排序，具体取决于使用的构造方法。TreeMap 的基本操作 `containsKey`、`get`、`put`、`remove` 方法，其时间复杂度是 O(logN)。

TreeMap 包含几个重要的成员变量：`root`、`size`、`comparator`。其中 `root` 是红黑树的根节点，它是 `Entry` 类型。`Entry` 是红黑树的节点，包含了红黑树的 6 个基本组成：

- `key`
- `value`
- `left`
- `right`
- `parent`
- `color`

`Entry` 节点根据 `key` 排序，包含的内容是 `value`。`key` 的比较通过 `comparator` 实现。`size` 是红黑树的节点个数。

---

## 2.22 Map 和 Set 有什么区别？

**参考答案：**

- `Set` 代表无序的、元素不可重复的集合；
- `Map` 代表具有映射关系（key-value）的集合，其所有的 `key` 是一个 `Set` 集合，即 `key` 无序且不能重复。

---

## 2.23 List 和 Set 有什么区别？

**参考答案：**

- `Set` 代表无序的、元素不可重复的集合；
- `List` 代表有序的、元素可以重复的集合。

---

## 2.24 ArrayList 和 LinkedList 有什么区别？

**参考答案：**

- `ArrayList` 的实现是基于数组，`LinkedList` 的实现是基于双向链表；
- 对于随机访问，`ArrayList` 优于 `LinkedList`，可以以 O(1) 的时间复杂度访问元素；
- 对于插入和删除操作，`LinkedList` 优于 `ArrayList`，无需重新计算大小或更新索引；
- `LinkedList` 更占内存，因为节点除了数据，还存储两个引用（前一个和后一个元素）。

---

## 2.25 有哪些线程安全的 List？

**参考答案：**

1. **Vector**
   - 比较古老，保证线程安全，但效率低，不推荐使用。

2. **Collections.SynchronizedList**
   - `Collections` 提供的 `synchronizedList` 方法可以将非线程安全的 `List` 包装为线程安全。
   - 扩展性和兼容性比 `Vector` 更好，但所有方法加锁，性能一般。

3. **CopyOnWriteArrayList**
   - Java 1.5 引入，位于 `java.util.concurrent` 包中。
   - 写操作复制底层数组，读操作无需加锁。
   - 写操作成本高，但在读取远多于写入的场景下是性能最优方案。

---

## 2.26 介绍一下 ArrayList 的数据结构？

**参考答案：**

- `ArrayList` 底层是数组实现，第一次插入元素时默认创建长度为 10 的数组。
- 超出限制时会扩容 50%，并通过 `System.arraycopy()` 拷贝到新数组。
- 按数组下标访问元素性能高，是基本优势；
- 尾部插入性能也高；
- 中间插入/删除需移动元素，性能较差，这是基本劣势。

## 2.27 谈谈 CopyOnWriteArrayList 的原理

**参考答案：**

CopyOnWriteArrayList 是 Java 并发包中提供的并发类，是一个线程安全且**读操作无锁**的 ArrayList。

正如其名称所示，在执行写操作时，它会复制一份新的 List，在该副本上完成写操作，然后再将引用指向新的 List，从而保证了写操作的线程安全。

- **读操作：** 无需加锁，可并发访问，性能较高；
- **写操作：** 上锁、复制原容器副本，在副本上修改，然后替换原容器的引用；
- 写期间的读操作仍访问旧容器，**实现了读写分离**。

**优点：**

- 读操作性能高，无需同步；
- 适合**读多写少**的场景；
- 不会抛出 `ConcurrentModificationException` 异常，因为遍历和修改操作不作用在同一个容器。

**缺点：**

- **内存占用大**：每次写操作都会复制整个数组；
- **实时性差**：写入期间读取到的是旧数据，无法保证读写强一致性。

---

## 2.28 说一说 TreeSet 和 HashSet 的区别

**参考答案：**

- 二者元素都不可重复，且线程不安全；
- `HashSet` 的元素可以为 `null`，`TreeSet` 不允许 `null`；
- `HashSet` 不保证元素顺序，`TreeSet` 支持**自然排序**或**定制排序**；
- `HashSet` 底层使用 **哈希表**，`TreeSet` 底层使用 **红黑树**。

---

## 2.29 说一说 HashSet 的底层结构

**参考答案：**

- `HashSet` 基于 `HashMap` 实现；
- 默认构造函数创建一个容量为 16，负载因子为 0.75 的 `HashMap`；
- 内部封装了一个 `HashMap`，所有元素作为 `key` 存入；
- 所有 `value` 为同一个静态常量 `PRESENT`（一个 `Object` 类型的占位符）。

---

## 2.30 BlockingQueue 中有哪些方法，为什么这样设计？

**参考答案：**

为了应对不同业务场景，`BlockingQueue` 提供了 4 组方法用于插入、移除及检查队列元素。每组方法在操作无法立即执行时表现不同：

| 行为方式 | 插入方法               | 移除方法               | 检查方法     |
|----------|------------------------|------------------------|--------------|
| 抛异常   | `add(e)`               | `remove()`             | `element()`  |
| 特定值   | `offer(e)`             | `poll()`               | `peek()`     |
| 阻塞     | `put(e)`               | `take()`               | -            |
| 超时     | `offer(e, time, unit)` | `poll(time, unit)`     | -            |

**说明：**

- **抛异常**：操作失败时抛出异常；
- **返回特定值**：操作失败时返回 `false` 或 `null`；
- **阻塞**：操作失败时阻塞直到成功；
- **超时**：在限定时间内等待操作完成，否则返回失败。

这样的设计使得 `BlockingQueue` 可灵活用于不同的并发场景，比如线程池、生产者消费者模型等。

## 2.31 BlockingQueue 是怎么实现的？

**参考答案：**

`BlockingQueue` 是一个接口，常见实现类包括：

- `ArrayBlockingQueue`
- `LinkedBlockingQueue`
- `DelayQueue`
- `PriorityBlockingQueue`
- `SynchronousQueue`

它们主要区别在于存储结构和操作方式。但 `put` 和 `take` 方法的实现原理是类似的。

以下以 `ArrayBlockingQueue` 为例说明：

### 关键组件

构造函数初始化了 `ReentrantLock` 和 `Condition`，用于同步控制：

```java
public ArrayBlockingQueue(int capacity, boolean fair) {
    if (capacity <= 0)
        throw new IllegalArgumentException();
    this.items = new Object[capacity];
    lock = new ReentrantLock(fair);
    notEmpty = lock.newCondition();
    notFull = lock.newCondition();
}
```

## 2.32 Stream（不是IOStream）有哪些方法？

**参考答案**

Stream 提供了大量的方法进行聚集操作，这些方法既可以是“中间的”，也可以是“末端的”。

**中间方法**：中间操作允许流保持打开状态，并允许直接调用后续方法。上面程序中的 `map()` 方法就是中间方法。中间方法的返回值是另外一个流。

**末端方法**：末端方法是对流的最终操作。当对某个 Stream 执行末端方法后，该流将会被“消耗”且不再可用。上面程序中的 `sum()`、`count()`、`average()` 等方法都是末端方法。

除此之外，关于流的方法还有如下两个特征：

- **有状态的方法**：这种方法会给流增加一些新的属性，比如元素的唯一性、元素的最大数量、保证元素以排序的方式被处理等。有状态的方法往往需要更大的性能开销。
- **短路方法**：短路方法可以尽早结束对流的操作，不必检查所有的元素。

### Stream 常用的中间方法：

- `filter(Predicate predicate)`：过滤 Stream 中所有不符合 predicate 的元素。
- `mapToXxx(ToXxxFunction mapper)`：使用 ToXxxFunction 对流中的元素执行一对一的转换，该方法返回的新流中包含了 ToXxxFunction 转换生成的所有元素。
- `peek(Consumer action)`：依次对每个元素执行一些操作，该方法返回的流与原有流包含相同的元素。该方法主要用于调试。
- `distinct()`：该方法用于排序流中所有重复的元素（判断元素重复的标准是使用 equals() 比较返回 true）。这是一个有状态的方法。
- `sorted()`：该方法用于保证流中的元素在后续的访问中处于有序状态。这是一个有状态的方法。
- `limit(long maxSize)`：该方法用于保证对该流的后续访问中最大允许访问的元素个数。这是一个有状态的、短路方法。

### Stream 常用的末端方法：

- `forEach(Consumer action)`：遍历流中所有元素，对每个元素执行 action。
- `toArray()`：将流中所有元素转换为一个数组。
- `reduce()`：该方法有三个重载的版本，都用于通过某种操作来合并流中的元素。
- `min()`：返回流中所有元素的最小值。
- `max()`：返回流中所有元素的最大值。
- `count()`：返回流中所有元素的数量。
- `anyMatch(Predicate predicate)`：判断流中是否至少包含一个元素符合 Predicate 条件。
- `noneMatch(Predicate predicate)`：判断流中是否所有元素都不符合 Predicate 条件。
- `findFirst()`：返回流中的第一个元素。
- `findAny()`：返回流中的任意一个元素。

除此之外，Java 8 允许使用流式 API 来操作集合，`Collection` 接口提供了一个 `stream()` 默认方法，该方法可返回该集合对应的流，接下来即可通过流式 API 来操作集合元素。由于 Stream 可以对集合元素进行整体的聚集操作，因此 Stream 极大地丰富了集合的功能。

---

### 扩展阅读

Java 8 新增了 `Stream`、`IntStream`、`LongStream`、`DoubleStream` 等流式 API，这些 API 代表多个支持串行和并行聚集操作的元素。上面 4 个接口中，`Stream` 是一个通用的流接口，而 `IntStream`、`LongStream`、`DoubleStream` 则代表元素类型为 int、long、double 的流。

Java 8 还为上面每个流式 API 提供了对应的 `Builder`，例如：

- `Stream.Builder`
- `IntStream.Builder`
- `LongStream.Builder`
- `DoubleStream.Builder`

开发者可以通过这些 Builder 来创建对应的流。

### 独立使用 Stream 的步骤如下：

1. 使用 `Stream` 或 `XxxStream` 的 `builder()` 类方法创建该 Stream 对应的 Builder。
2. 重复调用 Builder 的 `add()` 方法向该流中添加多个元素。
3. 调用 Builder 的 `build()` 方法获取对应的 Stream。
4. 调用 Stream 的聚集方法。

在上面 4 个步骤中，第 4 步可以根据具体需求来调用不同的方法，Stream 提供了大量的聚集方法供用户调用，具体可参考 `Stream` 或 `XxxStream` 的 API 文档。对于大部分聚集方法而言，每个 Stream 只能执行一次。

