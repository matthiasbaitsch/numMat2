function sf = sfRungeKutta(F, h)
    function yp = step(x, y)
        k1 = F(x, y(:));
        k2 = F(x + h / 2, y(:) + h / 2 * k1(:));
        k3 = F(x + h / 2, y(:) + h / 2 * k2(:));
        k4 = F(x + h, y(:) + h * k3(:));        
        yp = y(:) + h / 6 * (k1(:) + 2 * k2(:) + 2 * k3(:) + k4(:));
    end
    sf = @step;
end

