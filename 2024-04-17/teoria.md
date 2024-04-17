## Decomposição de Cholesky

Quase igual a decomposição LU
$$
\begin{equation}
    A=L\cdot U=L(D\cdot U*)
\end{equation}$$ 
$$
\begin{cases}
        u_{ij}=\frac{u_{ij}}{u_{ii}},i=1,2,3,\cdots,n\\
        d_{ii}=u_{ii},i=1,2,3,\cdots,n
\end{cases}
$$

Se A for simétrica, isto é:
$A^t=A$
$$
\begin{align}
    A=LDU^*\\
    A^T=(LDU^*)^T=U^{T*}D\cdot L^{T}\Rightarrow U^*=L^T\\
    A=L\cdot D\cdot L^T
\end{align}$$
Se A for definida positiva
$$\begin{align}
    A=L\cdot D^{\frac{1}{2}}D^{\frac{1}{2}}L^T\\
    A=L\cdot D^{\frac{1}{2}}(L\cdot D^{\frac{1}{2}})^T\\
    G=LD^{\frac{1}{2}}\\
    G^T=(LD^{\frac{1}{2}})^T\\
    \therefore A=G\cdot G^T
\end{align}$$

$$
\begin{align}
    Ax=b\\
    (G\cdot G^T)x=b\\
    G\cdot (G^Tx)=b\\
    G^Tx=y\\
    \begin{cases}
        Gy=b\\
        G^Tx=y
    \end{cases}
\end{align}
$$


$$
\begin{bmatrix}
    a_{11}&a_{11}&\cdots&a_{1n}\\
    a_{11}&a_{11}&\cdots&a_{2n}\\
    \vdots&\vdots&\ddots&\vdots\\
    a_{11}&a_{11}&\cdots&a_{3n}\\
    a_{11}&a_{11}&\cdots&a_{nn}\\

\end{bmatrix}
$$  

### Algoritmo

#### 1ª coluna

$$
\begin{align}
    G_{11}^2=a_{11}\Rightarrow G_{11}=\sqrt{a_{11}}
\end{align}$$

#### Generalizando

$$\begin{align}
    G_{ii}=\sqrt{a_{ii}-\sum^{i-1}_{k=1}G_{ik}^{2}},i=2,3\dots,n\\
    G_{ij}=\frac{a_{ij}-\sum^{j-1}_{k=1}G_{ik}G_{jk}}{G_{jj}},i=j+1,2,3,\dots,n
\end{align}$$

## Inversa de matriz
