function [x, y] = euler(F, I, h, y0)
    [x, y] = odesolve(F, I, h, y0, 'Euler');
end

