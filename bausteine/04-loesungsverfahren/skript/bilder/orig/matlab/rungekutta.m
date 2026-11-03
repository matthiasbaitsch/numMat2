function [x, y] = rungekutta(F, I, h, y0)
    x = (I(1):h:I(2))';
    m = length(x);
    n = length(y0);
    y = zeros(m, n);
    y(1, :) = y0';    
    for k = 1:length(x)-1
        xk = x(k);
        yk = y(k, :)';
        k1 = F(xk, yk);
        k2 = F(xk + h / 2, yk + h / 2 * k1);
        k3 = F(xk + h / 2, yk + h / 2 * k2);
        k4 = F(xk + h, yk + h * k3);
        y(k + 1, :) = (yk + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))';
    end    
end

