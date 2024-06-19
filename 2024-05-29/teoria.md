## Integração númerica

$$
    A\approx\sum^{n}_{k=0}f(c_k)\cdot\Delta X_k\Rightarrow A=\lim_{n\rightarrow+\infty}\sum^{n}_{k=0}f(\bar{c_{k}})\Delta X_k=F(X_n)-F(X_0)
$$

### Fórmulas de Newton-Cotes

$$
    \int_{a}^{b}f(x)dx\approx \sum^{n}_{k=0}A_kf(x_k)
$$

Considere $[a,b]$ e uma partição $x_k$ tal que $h=x_{k+1}-x_k$

$$
    \int^{a}_{b}f(x)dx\approx\int_{a}^{b}Pn(x)dx
$$

## Fórmulas dos trapézios

Utilizamos um polinômio de interpolação de grau $n=1$

$$
    \int_{x_0}^{x_1}f(x)dx\approx\frac{h}{2}(y_0+y_1)
$$