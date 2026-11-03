function sf = sfEuler(F, h)
    function yp = step(x, y)
        k = F(x, y(:));
        yp = y(:) + h * k(:);
    end
    sf = @step;
end

