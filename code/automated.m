initialise;
setiorates(2, 300);

diary myFlattop2Diary;
data_out = sweep(1,100);
run;
analyse2;
transfer;

data_out = sine(9.2);
run;
analyse2;
transfer;

load('random_signal_10s.mat');
data_out = 20*random_data_out;
run;
analyse2;
transfer;


data_out = sine(9.2,13.6);
run;
analyse2;

data_out = sine(9.2,50);
run;
analyse2;


diary off;
type myFlattop2Diary;
