xBarra = 2.0;
x_1 = 2.2;
tol=1.0e-03;
error = 1.0;
IterMax = 10;
iter = 1;
while (error > tol && iter<IterMax)

  %x = x_1*x_1 - 2.0;
  x = sqrt(x_1 + 2);
  x1 = sqrt(x + 2);
  error = abs(x - x_1)/abs(x);

  %Calculo dos erros:
  eNewNew = abs(x1 - xBarra);
  eNew = abs(x - xBarra);
  eOld = abs(x_1 - xBarra);

  %Calculo da ordem de convergencia:
  p = log(eNewNew/eNew)/log(eNew/eOld);
  fprintf("%f\n", p);

  x_1 = x;
  x = x1;
  iter = iter + 1;

endwhile

fprintf("%f\n", x);
