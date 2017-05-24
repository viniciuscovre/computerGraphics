function deblurredImage = deblurringMenu(blurredImage)
% Menu with the options to deblur a blurred image

fprintf('\n--> DEBLURRING STEP');
fprintf('\nSelect the deblurring methodology:\n');
fprintf('\n  1 - Lucy-Richardson Algorithm'); % for Gaussian Blur
fprintf('\n  2 - Wiener Deconvolution'); % for Wiener Blur (good for Motion Blur)
fprintf('\n  3 - Motion Deblur (using Wiener Deconvolution)'); % for Motion Blur
fprintf('\n  4 - Blind Deconvolution'); % test for all cases
answer = input('\n\nAnswer: ');

switch answer
    case 1
        % Lucy-Richardson Algorithm
        deblurredImage = lucyDeblur(blurredImage);
    case 2
        % Wiener Filter
        deblurredImage = wienerDeblur(blurredImage);
    case 3
        % Wiener Filter
        deblurredImage = motionDeblur(blurredImage);
    case 4
        % Blind Deblurring
        deblurredImage = blindDeblur(blurredImage);
    otherwise
        fprintf('Invalid option! Choose a valid one...\n');
        deblurredImage = deblurringMenu(blurredImage);
end