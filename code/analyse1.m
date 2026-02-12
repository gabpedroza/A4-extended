figure
hold on
disp('data_ch1');
disp(data_ch1);
disp('data_ch2');
disp(data_ch2);
disp('t');
disp(t);
plot(t,data_out,t,data_ch1,t,data_ch2)
title('Time-domain plot')
xlabel('Time (seconds)')
ylabel('Signal (volts)')
legend('Generated Signal','Channel 1','Channel 2')

hold off
