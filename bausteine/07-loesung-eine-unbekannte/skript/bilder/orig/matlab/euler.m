function [x, y] = euler(F, xrange, h, y0)
    x = xrange(1):h:xrange(2);
    y = zeros(1, length(x));
    
    y(1) = y0;    
    for i = 1:length(x)-1
       y(i+1) = y(i) + h * F(x(i), y(i));
    end
end

