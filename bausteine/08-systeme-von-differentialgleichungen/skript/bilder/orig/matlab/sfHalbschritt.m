function sf = sfHalbschritt(F, h)
    
    function yp = step(x, y)
        k1 = F(x, y(:));
        k2 = F(x + h / 2, y(:) + h / 2 * k1(:));        
        yp = y(:) + h * k2(:);
    end
    
    sf = @step;
end

