## Integração númerica

$$
\begin{align*}
    A\approx\sum^{n}_{k=0}f(c_k)\cdot\Delta X_k\Rightarrow A=\lim_{n\rightarrow+\infty}\sum^{n}_{k=0}f(\bar{c_{k}})\Delta X_k=F(X_n)-F(X_0)
\end{align*}
$$

### Fórmulas de Newton-Cotes

$$
\begin{align*}
    \int_{a}^{b}f(x)dx\approx \sum^{n}_{k=0}A_kf(x_k)
\end{align*}
$$

Considere $[a,b]$ e uma partição $x_k$ tal que $h=x_{k+1}-x_k$

$$
\begin{align*}
    \int^{a}_{b}f(x)dx\approx\int_{a}^{b}Pn(x)dx
\end{align*}
$$

## Fórmulas dos trapézios

Utilizamos um polinômio de interpolação de grau $n=1$

$$
\begin{align*}
    P_1(x)=y_0\cdot\frac{ffdsfsd}{dsfsdf}
\end{align*}
$$