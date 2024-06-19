- Conceitos básicos
- Solução de equações algébricas
- Solução de sistemas lineares
  - Decomposição L.U.
  - Eliminação de *Gauss*

## Classificação de um sistema linear:


### Sistema possível ou Consistente

- Determinado 
- Indeterminado

### Sistema impossível ou inconsistente


## Exemplo
 
$$
\begin{cases}
    x+y=6\\
    x-y=2
\end{cases}
;
\begin{cases}
    x+y=1\\
    2x+2y=2
\end{cases}
$$

## Possui-se dois métodos

- Métodos exatos
- Métodos iterativos

## Sistemas lineares equivalentes

Dois sistemas lineares são equivalentes quando admitem a mesma solução

Utiliza-se o método da *retrosubstituição*

### Sistema triangular superior

$$
\begin{equation}
X_{k}=\frac{bx-\sum_{j=k+1}^{n}a_{kj}\cdot x_{j}}{a_{kk}}   
\end{equation}
$$

## Decomposição L.U. (*lower and upper*)

$$
\begin{bmatrix}
    a_{11} & a_{12} & a_{13} & \cdots & a_{1n}\\
    a_{21} & a_{22} & a_{23} & \cdots & a_{2n}\\
    a_{31} & a_{32} & a_{33} & \cdots & a_{3n}\\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    a_{11} & a_{12} & a_{13} & \cdots & a_{1n}
\end{bmatrix}
$$

### Hipoteses

$det(a_{k})\neq,k=1,\cdots,n-1$

$A=LU \Rightarrow det(A)=det(LU)=det(L)\cdot det(U)=1\cdot u_{11}\cdots u_{nn}$

### Esquema para construção de matrizes L e U:

- Primeira linha de U

  - $$\begin{matrix}
      a_{11} = u_{11}\\
      a_{12} = u_{12}\\
      \vdots\\
      a_{1n}=u_{1n}
    \end{matrix}\Rightarrow\begin{matrix}
        u_{11}=a_{11}\\
        u_{12}=a_{12}\\
        \vdots\\
        u_{1n}=a_{1n}\\
    \end{matrix}$$

- Primeira coluna de L
  - $$\begin{matrix}
        a_{21}=l_{21}\cdot u_{11}\\a_{31}=l_{31}\cdot u_{11}\\\vdots\\a_{n1}=l_{n1}\cdot u_{11}
        \end{matrix}\Rightarrow\begin{matrix}
            l_{21}=\frac{a_{21}}{u_{11}}\\
            l_{31}=\frac{a_{21}}{u_{31}}\\
            \vdots\\
            l_{n1}=\frac{a_{n1}}{u_{11}}\\
        \end{matrix}$$

- Segunda linha de U
  - $$\begin{matrix}
      a_{22}=l_{21}\cdot u_{12}+u_{22}\\
      a_{23}=l_{21}\cdot u_{13}+u_{23}\\
      \vdots\\
      a_{2n}=l_{21}\cdot u_{1n}+u_{2n}\\
      \end{matrix}\Rightarrow
      \begin{matrix}
        u_{22}=a_{22}-l_{21}\cdot u_{12}\\
        u_{23}=a_{23}-l_{21}\cdot u_{13}\\
        \vdots\\
        u_{2n}=a_{2n}-l_{21}\cdot u_{1n}\\
      \end{matrix}
      $$
- Segunda linha de L
  - $$
        \begin{matrix}
        a_{32}=l_{31}\cdot u_{12}+l_{32}\cdot u_{22}\\
        a_{42}=l_{41}\cdot u_{12}+l_{42}\cdot u_{22}\\
        \vdots\\
        a_{n2}=l_{n1}\cdot u_{12}+l_{n2}\cdot u_{22}\\
        \end{matrix}\Rightarrow
        \begin{matrix}
            l_{32}=\frac{a_{32}-l_{31}\cdot u_{12}}{u_{22}}\\
            l_{42}=\frac{a_{42}-l_{41}\cdot u_{12}}{u_{22}}\\
            \vdots\\
            l_{n2}=\frac{a_{n2}-l_{n1}\cdot u_{12}}{u_{22}}\\
        \end{matrix}
        $$

### Algoritmo

$$
u_{ij}=a_{ij}-\sum_{k-1}^{i-1}l_{ik}\cdot u_{kj},(i<=j)\\
l_{ij}=\frac{a_{ij}-\sum_{k=1}^{j-1}l_{ik}\cdot u_{kj},(i>j)}{u_{jj}}
$$

