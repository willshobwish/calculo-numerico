## Review

### Resolução de equações algébricas $f(x)=0$

### Método da bissecção

### Iteração linear $x=\psi(x)$

### Método de Newton

Necessita de cálculo de derivada

### Métodos das secantes

Cálculo do coeficiente angular das retas secantes

### Método de Regula Falsi

Método que junta o método da bissecção e método das secantes 

$f(x,y)=0$

$g(x,y)=0$

Sistema de equações não lineares, reescrevemos desta forma:

$$
\begin{cases}
x=F(x,y) \Rightarrow x_{k+1}=F(x,y)\\
y=G(x,y) \Rightarrow y_{k+1}=G(x,y)
\end{cases}
$$


## Hoje:

### Método de Newton

Método de Newton para sistema de equações não lineares.
$$
f(x)=?\\
T(x)=f(p)+f'(p)(x-p)\\
E(x)=f(x)-T(x)\\
E(x)=f(x)-f(p)+f'(p)(x-p)\\
f(p+x-p)=f(x)=f(p)+f'(p)(x-p)+E(x)\\
E(x)=\frac{f''(e)(x-p)^{2}}{2!}
$$

Qual que é o nosso problema?

$$
\begin{cases}
f(x,y)=0\\
g(x,y)=0
\end{cases}
$$

Supondo que $(x_0,y_0)$ seja uma aproximação $(\bar x, \bar y)$ (solução exata). Queremos determinar $(x,y)$ tal que esta seja uma aproximação de $(\bar x, \bar y)$ com um erro menor.

$$
f(x,y)=f(x_0+(x-x_0),y_0+(y-y_0))=\\
f(x_0,y_0)+\frac{\partial f}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial f}{\partial y}(x_0,y_0)(y-y_0)+...+=0
$$

$$
g(x,y)=g(x_0,y_0)+\frac{\partial g}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial g}{\partial y}(x_0,y_0)(y-y_0)+...+=0
$$

$$
\begin{cases}
f(x_0,y_0)+\frac{\partial f}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial f}{\partial y}(x_0,y_0)(y-y_0)=0\\
g(x_0,y_0)+\frac{\partial g}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial g}{\partial y}(x_0,y_0)(y-y_0)=0
\end{cases}
$$

$$
\begin{cases}
\frac{\partial f}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial f}{\partial y}(x_0,y_0)(y-y_0)=-f(x_0,y_0)\\
\frac{\partial g}{\partial x}(x_0,y_0)(x-x_0)+\frac{\partial g}{\partial y}(x_0,y_0)(y-y_0)=-g(x_0,y_0)
\end{cases}
$$

A equação acima é um sistema linear.

$$
\begin{bmatrix}
    \frac{\partial f}{\partial x}&\frac{\partial f}{\partial y}\\
    \frac{\partial g}{\partial x}&\frac{\partial g}{\partial y}
\end{bmatrix}
\begin{bmatrix}
    X\\Y
\end{bmatrix}
=
\begin{bmatrix}
    -f\\-g
\end{bmatrix}
$$

onde $X=x-x_0$ e $Y=y-y_0$.


$det(A)=\frac{\partial f}{\partial x}\cdot\frac{\partial g}{\partial y}-\frac{\partial f}{\partial y}\cdot\frac{\partial g}{\partial x}$

$$  
det(A)=X=\begin{bmatrix}
    -f&\frac{\partial f}{\partial y}\\
    -g&\frac{\partial g}{\partial y}    
\end{bmatrix},
det(A)=Y=\begin{bmatrix}
    \frac{\partial f}{\partial x}&-f\\
    \frac{\partial g}{\partial x}&-g
\end{bmatrix}
$$
$$
x_1=x_0+\frac{(-f\cdot\frac{\partial g}{\partial y}+g\cdot\frac{\partial f}{\partial y})}{det(A)}\\
y_1=y_0+\frac{(-g\cdot\frac{\partial f}{\partial x}+f\cdot\frac{\partial g}{\partial x})}{det(A)}
$$
#### Passos para resolução:

- Escolher o chute inicial
- Definir a tolerância $\epsilon$
- $$x_{k+1}=x_{k}+\frac{(-f\cdot\frac{\partial g}{\partial y}+g\cdot\frac{\partial f}{\partial y})}{det(A)}\\y_{k+1}=y_{k}+\frac{(-g\cdot\frac{\partial f}{\partial x}+f\cdot\frac{\partial g}{\partial x})}{det(A)}$$
### Sistemas lineares

- Trabalho
    - Grupo 1
      - Método do Jacob-Richardson
    - Grupo 2
      - Método de Gauss-Seidel
    - Grupo 3
      - Método dos gradientes
    - Grupo 4
      - Métodos dos gradientes conjugados
    - O que entregar
      - Entregar o relatório (um relatório por grupo)
      - Apresentar a construção do método
      - Implementação do algoritmo
      - Resolução de um exemplo

### Decomposição de L.U.
