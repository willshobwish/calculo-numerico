## Método das secantes

A vantagem do método das secantes é não precisar realizar $f'(x)$, e também calcular o seu valor numérico. Há varias maneiras de modificar o método de Newton para eliminar essa desvantagem. Uma modificação consiste em substituir $f'(x_k)$ pelo quociente das diferenças. 
$$
\begin{equation}
    f'(x_{k})=\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}
\end{equation}
$$

onde $x_k$ e $x_{k-1}$ são duas aproximações quaisquer para a raiz de $\bar{x}$