function [x, y] = halbschritt(F, I, h, y0)
    [x, y] = odesolve(F, I, h, y0, 'Halbschritt');
end

