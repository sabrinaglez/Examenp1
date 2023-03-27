% Matriz de coeficientes
A = [0.25, 0.15, 0; 0.45, 0.5, 0.75; 0.3, 0.35, 0.25];

% Vector de valores independinetes
B = [1.5; 5; 3];

% Solución del sistema de las ecuaciones lineales
C = A \ B;

fprintf('La cantidad diaria que se debe producir de cada tipo de fertilizante es:\n');
fprintf('Tipo A: %.3f toneladas\n', C(1));
fprintf('Tipo B: %.3f toneladas\n', C(2));
fprintf('Tipo C: %.3f toneladas\n', C(3));