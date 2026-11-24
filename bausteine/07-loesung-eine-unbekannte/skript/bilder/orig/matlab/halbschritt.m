function [x, y] = halbschritt(F, I, h, y0)
    x = (I(1):h:I(2))';
    m = length(x);
    n = length(y0);
    y = zeros(m, n);
    y(1, :) = y0';
    for i = 1:length(x)-1
        xi = x(i);
        yi = y(i, :)';
        k1 = F(xi, yi);
        k2 = F(xi + h / 2, yi + h / 2 * k1);
        yp = (yi + h * k2)';
        y(i + 1, :) = yp;
    end    
end

