load('testrun.mat');
disp(data_ch2)
fid = fopen('log.txt','w')
fprintf(fid, 'Value = %.3f\n', disp(x))
fclose(fid)