clear, clc;
load result_of_the_model&manully_labeled/CSPC2020label_02_by_manurally.mat
l = length(sqi)
for i = 1:l
    if sqi(i) == 2
        sqi(i) = 1;
    elseif sqi(i) == 1
        sqi(i) = 0;
    end
        
end

save("result_of_the_model&manully_labeled/CSPC2020label_02_0_1_by_manurally.mat", "sqi") 