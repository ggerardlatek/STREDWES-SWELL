%This script read .S00 file of each subject and save them as .mat into "Data_raw" fold.
%S00 physiological data must be first downloaded into Swell_DB_S00_raw fold before use
%(https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/dans-x55-69zp)

for subj = 1:25

    files = dir(strcat('../raw_data/pp',num2str(subj),'*.S00'));
    for file = files'
        portiHRdata = tms_read(strcat('../raw_data/',file.name));
        if subj>=10
           k=4;
        else 
           k=3;
        end  
        eval([strcat('raw_',file.name(1:k),'_',file.name(end-5:end-4),'.mat'), ' = portiHRdata;']);

    end
    clear file files portiHRdata k
    save(strcat('../dataset/s',num2str(subj),'_physio_raw.mat'))
    clear 
    
end


