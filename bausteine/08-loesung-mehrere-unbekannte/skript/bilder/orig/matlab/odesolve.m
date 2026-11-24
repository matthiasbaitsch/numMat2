function [x, y] = odesolve(F, I, h, y0, m)
    
    % step function
    if strcmp(m, 'Euler')
        sf = sfEuler(F, h);
    elseif strcmp(m, 'Halbschritt')
        sf = sfHalbschritt(F, h);
    elseif strcmp(m, 'Runge Kutta')
        sf = sfRungeKutta(F, h);
    else
        error('Unknown Method');
    end
    
    % allocate
    x = I(1):h:I(2);
    N = length(x);
    y = zeros(N, length(y0));
    
    % solve
    y(1, :) = y0;
    for i = 1:(N-1)
       y(i+1, :) = sf(x(i), y(i, :)); 
    end
end

