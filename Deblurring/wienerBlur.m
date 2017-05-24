function outputImg = wienerBlur(inputImage)

if nargin ~= 1
    error('Invalid number of input arguments!');
    pause
end

outputImg = wiener2(inputImage, [5 5]);