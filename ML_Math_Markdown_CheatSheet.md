# 📚 机器学习数学公式与 Jupyter 笔记排版速查手册 (LaTeX & Markdown)

这份手册专为在 Jupyter Notebook (`.ipynb`) 中编写机器学习算法、数据分析报告和数学推导而整理。包含了最全的数学符号 LaTeX 表达，以及进阶的 Markdown 排版美化技巧。

---

## 第一部分：数学公式 LaTeX 全量整理 (含机器学习高频补充)

> **💡 提示**：在 Jupyter 中，行内公式使用 `$公式$`，独立居中公式使用 `$$公式$$`。

### 1. 集合论与逻辑 (概率论与信息论基础)
在原有的交并集基础上，补充了机器学习中常用的指示函数和信息论符号。

| 描述 | LaTeX 代码 | 显示效果 | 备注/机器学习场景 |
| :--- | :--- | :--- | :--- |
| **并集 (小/大)** | `A \cup B`, `\bigcup_{i=1}^n` | $A \cup B, \bigcup_{i=1}^n$ | 联合事件 |
| **交集 (小/大)** | `A \cap B`, `\bigcap_{i=1}^n` | $A \cap B, \bigcap_{i=1}^n$ | 同时发生的事件 |
| **差集 / 补集** | `A \setminus B`, `A^c`, `\bar{A}` | $A \setminus B, A^c, \bar{A}$ | 排除某情况 |
| **属于 / 包含** | `x \in A`, `A \subset B` | $x \in A, A \subset B$ | 样本属于某集合 |
| **指示函数** | `\mathbb{I}(x=1)`, `\mathbb{1}` | $\mathbb{I}(x=1), \mathbb{1}$ | 损失函数中的分类指示 |
| **信息熵** | `H(X)` | $H(X)$ | 决策树节点分裂依据 |
| **KL 散度** | `D_{KL}(P \| Q)` | $D_{KL}(P \| Q)$ | 分布相似度度量，注意双竖线用 `\|` |
| **定义为 / 恒等** | `\triangleq`, `\equiv` | $\triangleq, \equiv$ | 损失函数的定义 |

### 2. 概率论与数理统计
补充了似然函数、独立同分布等机器学习核心推导符号。

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **概率 / 条件概率**| `P(A)`, `P(A \mid B)` | $P(A), P(A \mid B)$ | 贝叶斯定理核心 |
| **期望** | `\mathbb{E}[X]`, `E_{x \sim p}[f(x)]`| $\mathbb{E}[X], E_{x \sim p}[f(x)]$| 常用于期望风险 |
| **方差 / 协方差** | `\text{Var}(X)`, `\text{Cov}(X,Y)` | $\text{Var}(X), \text{Cov}(X,Y)$| PCA降维推导常用 |
| **服从分布** | `X \sim \mathcal{N}(\mu, \sigma^2)` | $X \sim \mathcal{N}(\mu, \sigma^2)$ | 高斯分布，使用 `\mathcal` 花体 |
| **独立同分布** | `X_i \stackrel{i.i.d.}{\sim} P` | $X_i \stackrel{i.i.d.}{\sim} P$ | 极大似然估计的基础假设 |
| **似然函数** | `\mathcal{L}(\theta)`或 `L(\theta)` | $\mathcal{L}(\theta), L(\theta)$ | 似然评估，花体 L 很常见 |
| **估计量(帽子)** | `\hat{y}`, `\hat{\theta}` | $\hat{y}, \hat{\theta}$ | 预测值或参数估计值 |

### 3. 微积分与凸优化 (Calculus & Optimization)
补充了机器学习最优化算法（梯度下降、拉格朗日乘子）必须的符号。

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **极限 / 无穷** | `\lim_{n \to \infty}`, `\infty` | $\lim_{n \to \infty}, \infty$ | |
| **偏导数** | `\frac{\partial L}{\partial w}` | $\frac{\partial L}{\partial w}$ | 梯度下降推导 |
| **梯度 / 雅可比** | `\nabla_w L`, `J(f)` | $\nabla_w L, J(f)$ | 多维函数求导 |
| **拉普拉斯/海森** | `\Delta f`, `\nabla^2 f`, `H` | $\Delta f, \nabla^2 f, H$ | 牛顿法中的海森矩阵 |
| **定积分 / 连加** | `\int_{a}^{b}`, `\sum_{i=1}^{N} x_i` | $\int_{a}^{b}, \sum_{i=1}^{N} x_i$ | |
| **最大化/最小化** | `\max_{\theta} L(\theta)`, `\min` | $\max_{\theta} L(\theta), \min$ | 目标函数 |
| **求极值点** | `\arg\max_{x} f(x)`, `\arg\min` | $\arg\max_{x} f(x)$ | 返回使得函数最大/小的 $x$ |
| **拉格朗日函数** | `\mathcal{L}(x, \lambda, \nu)` | $\mathcal{L}(x, \lambda, \nu)$ | SVM等带约束优化常用 |

### 4. 线性代数 (Linear Algebra)
补充了张量、特殊矩阵乘法符号。

| 描述 | LaTeX 代码 | 显示效果 | 备注 |
| :--- | :--- | :--- | :--- |
| **向量(粗体)** | `\mathbf{w}, \boldsymbol{\beta}` | $\mathbf{w}, \boldsymbol{\beta}$ | 权重向量，希腊字母用 boldsymbol |
| **矩阵环境** | `\begin{bmatrix} a & b \\ c & d \end{bmatrix}`| 方括号矩阵形式 | 线性回归数据矩阵表示 |
| **转置 / 逆** | `X^T`, `X^\top`, `X^{-1}` | $X^T, X^\top, X^{-1}$ | 解析解推导常用 |
| **范数(L1/L2)** | `\|w\|_1`, `\|w\|_2^2` | $\|w\|_1, \|w\|_2^2$ | 正则化项常用 |
| **内积 / 点积** | `a^T b`, `\langle x, y \rangle` | $a^T b, \langle x, y \rangle$ | |
| **哈达玛积** | `A \odot B` | $A \odot B$ | 矩阵按元素相乘 (逐元素操作) |
| **克罗内克积** | `A \otimes B` | $A \otimes B$ | 张量积 |
| **迹 (Trace)** | `\text{tr}(A)` | $\text{tr}(A)$ | 矩阵的迹，PCA推导常用 |

---

## 第二部分：Jupyter Notebook (Markdown) 常用语法与美化指南

在编写机器学习算法笔记时，纯文本往往显得单调。以下是一些能大幅提升 `.ipynb` 颜值的排版技巧，这些都是直接兼容 Jupyter 的 HTML/Markdown 语法。

### 1. 基础但高质量的 Markdown
* **分级标题**：使用 `#`, `##`, `###` 保持层级清晰。
* **无序列表**：使用 `-` 或 `*`。
* **有序列表**：使用 `1. `, `2. `。
* **强调与代码**：`**加粗**`，`*斜体*`，`` `行内代码` ``，`~~删除线~~`。
* **代码块高亮**：
  ```python
  import pandas as pd
  import numpy as np
  from sklearn.linear_model import LogisticRegression
  ```

### 2. Jupyter 特色美化：彩色提示框 (Alert Boxes)
这是数据分析笔记中最常用的技巧，用于醒目地标记公式结论、警告或提示。在 Markdown 单元格中直接输入 HTML：

**信息提示 (Info - 蓝色)**
```html
<div class="alert alert-info" style="border-radius: 5px;">
  <b>📘 核心结论：</b> 逻辑回归虽然名字里有“回归”，但实际上是一个<b>分类</b>算法。其核心是使用了 Sigmoid 函数将线性回归的输出映射到 $(0, 1)$ 区间。
</div>
```

**警告提示 (Warning - 黄色)**
```html
<div class="alert alert-warning" style="border-radius: 5px;">
  <b>⚠️ 注意：</b> 在使用 SVM 之前，必须对数据进行标准化 (StandardScaler)，因为 SVM 依赖于距离度量！
</div>
```

**成功提示 (Success - 绿色)**
```html
<div class="alert alert-success" style="border-radius: 5px;">
  <b>✅ 优化完成：</b> 模型收敛，当前损失值 $L(\theta)$ 已达到全局极小值点。
</div>
```

**危险/报错提示 (Danger - 红色)**
```html
<div class="alert alert-danger" style="border-radius: 5px;">
  <b>🛑 常见错误：</b> 忘记添加偏置项 (Bias) 会导致模型穿过原点，严重降低拟合能力。
</div>
```

### 3. 文字颜色与高亮
如果你只想让某几个字变色，可以使用 `<span>` 或 `<font>` 标签：
```html
<font color="red">这段文字是红色的</font>
<span style="color: blue; font-weight: bold;">这段文字是蓝色且加粗的</span>
<mark>这段文字有黄色荧光笔背景</mark>
```

### 4. 折叠面板 (Collapsible Details)
推导过程太长？不想占用太多屏幕空间？可以使用折叠面板把复杂的数学推导藏起来。

```html
<details>
  <summary><b>👉 点击展开：逻辑回归损失函数的极大似然推导过程</b></summary>
  
  这里写推导过程，支持 LaTeX：
  $$ \mathcal{L}(\theta) = \prod_{i=1}^{n} h_\theta(x_i)^{y_i} (1 - h_\theta(x_i))^{1-y_i} $$
  两边取对数得到对数似然：
  $$ \ell(\theta) = \sum_{i=1}^{n} y_i \log h_\theta(x_i) + (1-y_i) \log (1 - h_\theta(x_i)) $$
  
</details>
```

### 5. 图像排版 (居中与缩放)
默认的 `![alt](url)` 图片是靠左且无法调节大小的。在笔记中插入算法原理图时，使用 HTML `<img>` 更好：

```html
<p align="center">
  <img src="your_image_path_or_url.png" width="400" alt="梯度下降图示">
  <br>
  <i>图 1：梯度下降算法的等高线图</i>
</p>
```

### 6. 页内跳转定位 (锚点)
如果笔记很长，可以制作一个目录并实现页内跳转。
**步骤 1：在你想要跳到的地方（比如某个大标题下）定义一个 ID：**
```html
<a id="math-derivation"></a>
### 算法推导细节
```
**步骤 2：在目录处创建一个链接指向它：**
```markdown
[点击这里跳转到算法推导细节](#math-derivation)
```

### 7. 公式推导排版实战模板 (复制即用)
最后提供一个你在写 ML 算法笔记时可以直接复用的标准推导格式：

```markdown
### 目标函数与梯度

我们定义带 $L_2$ 正则化的目标函数为：

$$
J(\mathbf{w}) = \frac{1}{N} \sum_{i=1}^{N} L(y_i, f(\mathbf{x}_i)) + \frac{\lambda}{2} \|\mathbf{w}\|_2^2
$$

其中，使用均方误差 (MSE) 作为损失函数 $L$ 时：

$$
\begin{aligned}
J(\mathbf{w}) &= \frac{1}{N} \sum_{i=1}^{N} (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \frac{\lambda}{2} \mathbf{w}^T \mathbf{w} \\
&= \frac{1}{N} \|\mathbf{y} - X\mathbf{w}\|_2^2 + \frac{\lambda}{2} \|\mathbf{w}\|_2^2
\end{aligned}
$$

对目标函数求梯度：

$$
\nabla_{\mathbf{w}} J(\mathbf{w}) = - \frac{2}{N} X^T (\mathbf{y} - X\mathbf{w}) + \lambda \mathbf{w}
$$

令梯度等于 0，即可得到闭式解 (Closed-form Solution)：

$$
\mathbf{w}^* = (X^T X + \frac{\lambda N}{2} I)^{-1} X^T \mathbf{y}
$$
```
