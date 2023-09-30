function [ portiHRdata, portiHeartPre, portiSkinRaw ] = myDoReadData( filename )

%DOREADDATA reads data from a Portilab Poly5 document (.S00)
%   Reads all data (portiHRdata) and seperately stores the data relevant to
%   further processing (HeartPre, SkinRaw)

    portiHRdata = tms_read(filename)

    portiSkinRaw = portiHRdata.data{7};
    portiHeartPre = portiHRdata.data{8}; %
    
end

