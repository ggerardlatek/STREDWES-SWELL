%This script read .S00 file of each subject and save them as .mat into "dataset" fold.
%S00 physiological data must be first downloaded into Swell_DB_S00_raw fold before use
%(https://ssh.datastations.nl/dataset.xhtml?persistentId=doi:10.17026/dans-x55-69zp)

for subj = 1:25

    files = dir(fullfile('Swell_DB_S00_raw',strcat('pp',num2str(subj),'*.S00')));
    for file = files'
        portiHRdata = tms_read(file);
        if subj>=10
           k=4;
        else 
           k=3;
        end  
        eval([strcat('raw_',file.name(1:k),'_',file.name(end-5:end-4),'.mat'), ' = portiHRdata;']);

    end
    clear file files portiHRdata k
    save(fullfile('dataset',strcat('s',num2str(subj),'_physio_raw.mat')))
    clear 
    
end


