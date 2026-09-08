# 📚 机器学习数学公式与 Jupyter 笔记排版速查手册 (LaTeX & Markdown)

这份手册专为在 Jupyter Notebook (`.ipynb`) 中编写机器学习算法、数据分析报告和数学推导而整理。包含了最全的数学符号 LaTeX 表达，以及进阶的 Markdown 排版美化技巧。

---

## 第一部分：数学公式 LaTeX 全量整理

> **💡 提示**：在 Jupyter 中，行内公式使用 `$公式$`，独立居中公式使用 `$$公式$$`。

### 0. 基础数学符号、运算与箭头 (🆕 新增基础补全)
这里补充了最基础的四则运算、关系判断、省略号及常用箭头。

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **基础运算** | `\times, \div, \pm, \mp` | $\times, \div, \pm, \mp$ | 乘，除，加减，减加 |
| **分数与根号** | `\frac{a}{b}, \sqrt{x}, \sqrt[n]{x}` | $\frac{a}{b}, \sqrt{x}, \sqrt[n]{x}$ | |
| **关系符(等与不等)** | `\neq, \approx, \sim, \equiv` | $\neq, \approx, \sim, \equiv$ | 不等，约等，相似，恒等 |
| **关系符(大小)** | `\le, \ge, \ll, \gg` | $\le, \ge, \ll, \gg$ | 小于等于，大于等于，远小于，远大于 |
| **正比于** | `\propto` | $\propto$ | 物理和概率论中常用 |
| **省略号(底/中/竖/斜)**| `\dots, \cdots, \vdots, \ddots` | $\dots, \cdots, \vdots, \ddots$ | 矩阵或无穷级数中常用 |
| **绝对值 / 范数** | `|x|, \|x\|` | $|x|, \|x\|$ | |
| **常用单箭头** | `\rightarrow, \leftarrow` | $\rightarrow, \leftarrow$ | 可简写为 `\to`, `\gets` |
| **推导双箭头** | `\Rightarrow, \Leftarrow, \Leftrightarrow` | $\Rightarrow, \Leftarrow, \Leftrightarrow$ | 逻辑推导等价 |
| **映射** | `\mapsto` | $\mapsto$ | 函数映射，如 $x \mapsto x^2$ |

### 1. 方程组与多行公式排版 (🆕 新增核心排版)

在机器学习推导中，经常需要列出方程组或长公式对齐：

**方程组 (Cases 环境) 与矩阵**：用于联立方程或分段函数。
```latex
\begin{cases} 
3x + 4y = 10 \\ 
x - y = 1 
\end{cases}
```
显示效果：
$$
\begin{cases} 
3x + 4y = 10 \\ 
x - y = 1 
\end{cases}
$$

**多行公式对齐 (Aligned 环境)**：使用 `&` 指定对齐位置，通常对齐等号。
```latex
\begin{aligned}
f(x) &= (x+1)^2 \\
     &= x^2 + 2x + 1
\end{aligned}
```
显示效果：
$$
\begin{aligned}
f(x) &= (x+1)^2 \\
     &= x^2 + 2x + 1
\end{aligned}
$$
**矩阵**：
vmatrix,Vmatrix,bmatrix
```latex
\begin{vmatrix}a&b\\c&d\end{vmatrix}
```
显示效果：
$$
\begin{vmatrix}a&b\\c&d\end{vmatrix}
$$



### 2. 集合论与逻辑 (概率论与信息论基础)

| 描述 | LaTeX 代码 | 显示效果 | 备注/机器学习场景 |
| :--- | :--- | :--- | :--- |
| **并集 (小/大)** | `A \cup B`, `\bigcup_{i=1}^n` | $A \cup B, \bigcup_{i=1}^n$ | 联合事件 |
| **交集 (小/大)** | `A \cap B`, `\bigcap_{i=1}^n` | $A \cap B, \bigcap_{i=1}^n$ | 同时发生的事件 |
| **差集 / 补集** | `A \setminus B`, `A^c`, `\bar{A}` | $A \setminus B, A^c, \bar{A}$ | 排除某情况 |
| **属于 / 包含** | `x \in A`, `A \subset B` | $x \in A, A \subset B$ | 样本属于某集合 |
| **指示函数** | `\mathbb{I}(x=1)`, `\mathbb{1}` | $\mathbb{I}(x=1), \mathbb{1}$ | 损失函数中的分类指示 |
| **信息熵** | `H(X)` | $H(X)$ | 决策树节点分裂依据 |
| **KL 散度** | `D_{KL}(P \| Q)` | $D_{KL}(P \| Q)$ | 分布相似度度量，双竖线用 `\|` |

### 3. 概率论与数理统计

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **概率 / 条件概率**| `P(A)`, `P(A \mid B)` | $P(A), P(A \mid B)$ | 贝叶斯定理核心 |
| **期望** | `\mathbb{E}[X]`, `E_{x \sim p}[f(x)]`| $\mathbb{E}[X], E_{x \sim p}[f(x)]$| 常用于期望风险 |
| **方差 / 协方差** | `\text{Var}(X)`, `\text{Cov}(X,Y)` | $\text{Var}(X), \text{Cov}(X,Y)$| PCA降维推导常用 |
| **服从分布** | `X \sim \mathcal{N}(\mu, \sigma^2)` | $X \sim \mathcal{N}(\mu, \sigma^2)$ | 高斯分布，使用 `\mathcal` |
| **独立同分布** | `X_i \stackrel{i.i.d.}{\sim} P` | $X_i \stackrel{i.i.d.}{\sim} P$ | 极大似然估计基础假设 |
| **似然函数** | `\mathcal{L}(\theta)`或 `L(\theta)` | $\mathcal{L}(\theta), L(\theta)$ | 似然评估，花体 L 很常见 |
| **估计量(帽子)** | `\hat{y}`, `\hat{\theta}` | $\hat{y}, \hat{\theta}$ | 预测值或参数估计值 |

### 4. 微积分与凸优化 (Calculus & Optimization)

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **极限 / 无穷** | `\lim_{n \to \infty}`, `\infty` | $\lim_{n \to \infty}, \infty$ | |
| **偏导数** | `\frac{\partial L}{\partial w}` | $\frac{\partial L}{\partial w}$ | 梯度下降推导 |
| **梯度 / 雅可比** | `\nabla_w L`, `J(f)` | $\nabla_w L, J(f)$ | 多维函数求导 |
| **拉普拉斯/海森** | `\Delta f`, `\nabla^2 f`, `H` | $\Delta f, \nabla^2 f, H$ | 牛顿法中的海森矩阵 |
| **定积分 / 连加** | `\int_{a}^{b}`, `\sum_{i=1}^{N} x_i` | $\int_{a}^{b}, \sum_{i=1}^{N} x_i$ | |
| **最大化/最小化** | `\max_{\theta} L(\theta)`, `\min` | $\max_{\theta} L(\theta), \min$ | 目标函数 |
| **求极值点** | `\arg\max_{x} f(x)`, `\arg\min` | $\arg\max_{x} f(x)$ | 返回使得函数最值的 $x$ |
| **拉格朗日函数** | `\mathcal{L}(x, \lambda, \nu)` | $\mathcal{L}(x, \lambda, \nu)$ | SVM等带约束优化常用 |

### 5. 线性代数 (Linear Algebra)

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **向量(粗体)** | `\mathbf{w}, \boldsymbol{\beta}` | $\mathbf{w}, \boldsymbol{\beta}$ | 希腊字母粗体用 boldsymbol |
| **矩阵环境** | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}`| 方括号矩阵形式 | 线性回归数据矩阵表示 |
| **转置 / 逆** | `X^T`, `X^\top`, `X^{-1}` | $X^T, X^\top, X^{-1}$ | 解析解推导常用 |
| **范数(L1/L2)** | `\|w\|_1`, `\|w\|_2^2` | $\|w\|_1, \|w\|_2^2$ | 正则化项常用 |
| **内积 / 点积** | `a^T b`, `\langle x, y \rangle` | $a^T b, \langle x, y \rangle$ | |
| **哈达玛积** | `A \odot B` | $A \odot B$ | 矩阵按元素相乘 |
| **克罗内克积** | `A \otimes B` | $A \otimes B$ | 张量积 |
| **迹 (Trace)** | `\text{tr}(A)` | $\text{tr}(A)$ | 矩阵的迹，PCA推导常用 |

---

## 第二部分：Jupyter Notebook (Markdown) 常用语法与美化指南

### 1. 基础 Markdown
* **分级标题**：使用 `#`, `##`, `###` 保持层级清晰。
* **无序列表**：使用 `-` 或 `*`。
* **有序列表**：使用 `1. `, `2. `。
* **强调与代码**：`**加粗**`，`*斜体*`，`` `行内代码` ``，`~~删除线~~`。

### 2. Jupyter 特色美化：彩色提示框 (Alert Boxes)
在 Markdown 单元格中直接输入 HTML 构建提示框：

**信息提示 (Info - 蓝色)**
```html
<div class="alert alert-info" style="border-radius: 5px;">
  <b>📘 核心结论：</b> 逻辑回归实际上是一个<b>分类</b>算法。其核心是使用了 Sigmoid 函数映射。
</div>
```

**警告提示 (Warning - 黄色)**
```html
<div class="alert alert-warning" style="border-radius: 5px;">
  <b>⚠️ 注意：</b> 使用 SVM 前必须对数据进行标准化 (StandardScaler)！
</div>
```

**成功提示 (Success - 绿色)**
```html
<div class="alert alert-success" style="border-radius: 5px;">
  <b>✅ 优化完成：</b> 模型收敛，当前损失值达到全局极小值点。
</div>
```

**危险/报错提示 (Danger - 红色)**
```html
<div class="alert alert-danger" style="border-radius: 5px;">
  <b>🛑 常见错误：</b> 忘记添加偏置项 (Bias) 会导致模型穿过原点。
</div>
```

### 3. 文字颜色与高亮
```html
<font color="red">这段文字是红色的</font>
<span style="color: blue; font-weight: bold;">这段文字是蓝色且加粗的</span>
<mark>这段文字有黄色荧光笔背景</mark>
```

### 4. 折叠面板 (Collapsible Details)
推导过程太长？可以使用折叠面板把复杂的数学推导藏起来。
```html
<details>
  <summary><b>👉 点击展开：逻辑回归推导过程</b></summary>
  
  这里写推导过程，支持 LaTeX：
  $$ \ell(\theta) = \sum_{i=1}^{n} y_i \log h_\theta(x_i) + (1-y_i) \log (1 - h_\theta(x_i)) $$
  
</details>
```

### 5. 图像排版 (居中与缩放)
```html
<p align="center">
  <img src="your_image_path.png" width="400" alt="梯度下降图示">
  <br>
  <i>图 1：梯度下降算法的等高线图</i>
</p>
```
