function deblurredImage = deblurringMenu(blurredImage)
% Menu with the options to deblur a blurred image

fprintf('\n--> DEBLURRING STEP');
fprintf('\nSelect the deblurring methodology:\n');
fprintf('\n  1 - Wiener Filter');
answer = input('\n\nAnswer: ');

switch answer
    case 1
        % Wiener Filter
        deblurredImage = wienerDeblur(blurredImage);
    otherwise
        fprintf('Invalid option! Choose a valid one...\n');
        deblurredImage = deblurringMenu(blurredImage);
end