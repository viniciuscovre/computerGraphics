function outputImg = blindDeblur(inputImage)

if nargin ~= 1
    error('Invalid number of input arguments!');
    pause
end

INITPSF = ones([9 9]);

% PSF = fspecial('motion',13,45);
% INITPSF = ones(size(PSF));

outputImg = deconvblind(inputImage,INITPSF,15);