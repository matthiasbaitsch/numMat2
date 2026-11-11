function plotSlopeField(F, xrange, yrange, delta)    
    
    % Size of plotting rectangle
    lx = diff(xrange);
    ly = diff(yrange);    

    % Points in x-direction and y-direction
    nx = ceil(lx / delta) + 1;
    ny = ceil(ly / delta) + 1;        
    px = linspace(xrange(1), xrange(2), nx);
    py = linspace(yrange(1), yrange(2), ny);
    
    % Points on grid
    [xa, ya] = meshgrid(px, py);
    xa = reshape(xa, [], 1);
    ya = reshape(ya, [], 1);    
    
    % Length of slope line
    s = 0.4 * min(lx / nx, ly / ny);
    
    % Slope lines
    xl = zeros(2, length(xa));
    yl = zeros(2, length(xa));
    for i = 1:length(xa)
        x  = xa(i);
        y  = ya(i);    
        ys = F(x, y);
        as = sqrt(ys^2 + 1);        
        dx = s *  1 / as;
        dy = s * ys / as;        
        xl(:, i) = [x - dx, x + dx];
        yl(:, i) = [y - dy, y + dy];
    end
    
    % Plot
    plot(xl, yl, 'color', 'blue');
end

