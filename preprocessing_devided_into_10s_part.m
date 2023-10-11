clear all; close all;clc;
load A02.mat
% load A04.mat
number_seg=floor(length(ecg)/4000);
ecgpart=zeros(number_seg,4000);
for i =1: number_seg
    ecgpart(i,1:4000)=ecg(1+4000*(i-1):4000*i);  % 4000 = frequency(400Hz) x time(10s)
end
save("ecgpart_02.mat", "ecgpart") 
ecgpart=[];
load A04.mat
number_seg=floor(length(ecg)/4000);
ecgpart=zeros(number_seg,4000);
for i =1: number_seg
    ecgpart(i,1:4000)=ecg(1+4000*(i-1):4000*i);
end
save("ecgpart_04.mat", "ecgpart") 
