# Solução de sistemas lineares

## O que vimos até agora

- Decomposição LU
  - No fundo é utilizado para calcular determinantes

## O que veremos

- Eliminação de Gauss
- Eliminação de Gauss com pivotamento
- Decomposição de Cholesky
  - Decomposição LU de matrizes especiais

## Próxima aula

- Mal condicionamento
- Cálculo de matriz inversa


## Método de elimição de Gauss

Seja um sistema $Ax=b$ dado por:
$$
\begin{equation}
    \begin{bmatrix}
        a_{11}& a_{12}&\dots& a_{1n}\\ 
        a_{21}& a_{22}&\dots& a_{2n}\\ 
        a_{31}& a_{32}&\dots& a_{3n}\\ 
        \vdots&&\\
        a_{n1}& a_{n2}&\dots& a_{nn}\\ 
    \end{bmatrix}
    \begin{bmatrix}
        x_{1}\\
        x_{2}\\
        x_{3}\\
        \vdots\\
        x_{n}\\
    \end{bmatrix}=
    \begin{bmatrix}
        b_{1}\\
        b_{2}\\
        b_{3}\\
        \vdots\\
        b_{n}\\
    \end{bmatrix}
\end{equation}
$$