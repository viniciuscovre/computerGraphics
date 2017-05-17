function answer = blurringMenu(fileName)
% Menu with the options to blur the input image

fprintf('Select the type of blur for %s:\n', fileName);
fprintf('\n  1 - Gaussian Blur');
fprintf('\n  2 - Motion Blur Simulation');
fprintf('\n  3 - Skip blurring step');
answer = input('\n\nAnswer: ');
